from typing import Optional
from pydantic import BaseModel, ConfigDict
from src.data.enums.payment_enums import PaymentStatus


class UpdatePaymentRequestModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    payee_payment_status: Optional[PaymentStatus] = None
    payee_due_date: Optional[str] = None
    due_amount: Optional[float] = None
