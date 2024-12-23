from src.data.api_models.get_payments_request_model import GetPaymentsRequestModel
from src.data.api_models.update_payment_request_model import UpdatePaymentRequestModel
from src.database.models import payments_model


class PaymentsController:
    def get_payments(self, page_number:int = 0, request_model: GetPaymentsRequestModel = None):
        return payments_model.get_payments(page_number=page_number, request_model=request_model)

    def store_payments(self, data_frame):
        return payments_model.store_payments(data_frame)

    def update_payment(self, payment_id:str, request_model: UpdatePaymentRequestModel):
        result = payments_model.update_payment(payment_id=payment_id, request_model=request_model)
        return result

