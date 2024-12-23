import datetime
import logging
from bson.objectid import ObjectId

from fastapi import HTTPException
from pydantic import BaseModel, ConfigDict

from src.data.api_models.update_payment_request_model import UpdatePaymentRequestModel
from src.data.enums.payment_enums import PaymentStatus, PaymentFilterColumns
from src.data.api_models.get_payments_request_model import GetPaymentsRequestModel
from src.database.config import DBConfig
from typing import Optional

DATE_TIME_FORMAT = "%Y-%M-%DT%H:%M:%SZ"
DBCONFIG = DBConfig()
PAYMENTS_COLLECTION = DBCONFIG.get_payments_collection()
LOGGER = logging.getLogger(__name__)
PAGE_SIZE = 15


class PaymentsModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    payee_first_name: Optional[str] = None
    payee_last_name: Optional[str] = None
    payee_payment_status: Optional[PaymentStatus] = None
    payee_added_date_utc: Optional[datetime.datetime] = None
    payee_due_date: Optional[datetime.date] = None
    payee_address_line_1: str
    payee_address_line_2: Optional[str]
    payee_city: str
    payee_country: str
    payee_province_or_state: Optional[str]
    payee_postal_code: str
    payee_phone_number: str
    payee_email: str
    currency: str
    discount_percent: Optional[float] = 0.0
    tax_percent: Optional[float] = 0.0
    due_amount: float
    total_due: Optional[float] = 0.0



def get_payments(page_number:int = 0, request_model: GetPaymentsRequestModel = None):
    filters = request_model.filters if request_model else None
    search_text = request_model.search_text if request_model else None
    if not request_model or (request_model and request_model.are_filters_valid):
        try:
            # Add the user's filters
            db_filters = filters or {}
            # Add search filters
            if search_text:
                search_filters = {
                    "$or": [{field: {"$regex": search_text}} for field in PaymentFilterColumns.get_all() if field not in db_filters],
                }
                if filters and search_filters:
                    db_filters = {
                        "$and": [
                            filters,
                            search_filters,
                        ]
                    }
                else:
                    db_filters = search_filters

            print(db_filters)
            # Query DB
            total_count = PAYMENTS_COLLECTION.count_documents(db_filters)
            response = PAYMENTS_COLLECTION.find(db_filters).skip(page_number*PAGE_SIZE).limit(PAGE_SIZE)
            return {
                "payments": [to_dict(payment) for payment in response],
                "total_count": total_count,
            }
        except Exception as e:
            LOGGER.exception("MODEL ERROR: get_payments")
            return HTTPException(status_code=500, detail=str(e))
    else:
        return HTTPException(status_code=404, detail="Invalid filters")

def store_payments(data_frame):
    try:
        # First delete all payments data
        PAYMENTS_COLLECTION.delete_many({})
        # Reload payments data
        response = PAYMENTS_COLLECTION.insert_many(data_frame.to_dict('records'))
        return {
            "status_code": 200,
            "message": f"Inserted IDs: {response.inserted_ids}",
        }
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

def update_payment(payment_id:str, request_model: UpdatePaymentRequestModel):
    try:
        filters: dict = {"_id": ObjectId(payment_id)}
        update_fields = {
            "payee_payment_status": request_model.payee_payment_status,
            "payee_due_date": request_model.payee_due_date,
            "due_amount": request_model.due_amount,
        }
        result = PAYMENTS_COLLECTION.update_one(filters, {"$set": update_fields})
        updated_payment = PAYMENTS_COLLECTION.find_one(filters)
        return to_dict(updated_payment)
    except Exception as e:
        LOGGER.exception(f"MODEL ERROR: update_payment: {payment_id}, payload: {request_model}")
        return HTTPException(status_code=500, detail=str(e))


def to_dict(payment: PaymentsModel):
    # Change the payee_payment_status to “due_now” if payee_due_date is today
    payee_due_date = datetime.datetime.strptime(payment["payee_due_date"], '%Y-%m-%d').date()
    today = datetime.date.today()
    payee_payment_status = payment["payee_payment_status"]
    if today == payee_due_date:
        payee_payment_status = PaymentStatus.DUE_NOW.value
    elif today > payee_due_date:
        # Change the payee_payment_status to “overdue” if payee_due_date smaller than today.
        payee_payment_status = PaymentStatus.OVERDUE.value
    # Calculate total due
    discount_percent: float = payment["discount_percent"]
    tax_percent: float = payment["tax_percent"]
    due_amount: float = payment["due_amount"]
    total_due: float = round(((due_amount * (1 - (discount_percent/100))) * (1 + (tax_percent/100))), 2)

    return {
        "id": str(payment["_id"]),
        "payee_first_name": payment["payee_first_name"],
        "payee_last_name": payment["payee_last_name"],
        "payee_payment_status": payee_payment_status,
        "payee_added_date_utc": datetime.datetime.fromtimestamp(payment["payee_added_date_utc"]).strftime(DATE_TIME_FORMAT),
        "payee_due_date": payment["payee_due_date"],
        "payee_address_line_1": payment["payee_address_line_1"],
        "payee_address_line_2": payment["payee_address_line_2"],
        "payee_city": payment["payee_city"],
        "payee_country": str(payment["payee_country"]),
        "payee_province_or_state": payment["payee_province_or_state"],
        "payee_postal_code": str(payment["payee_postal_code"]),
        "payee_phone_number": str(payment["payee_phone_number"]),
        "payee_email": payment["payee_email"],
        "currency": payment["currency"],
        "discount_percent": discount_percent,
        "tax_percent": tax_percent,
        "due_amount": due_amount,
        "total_due": total_due,
    }
