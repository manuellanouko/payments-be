from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

@dataclass
class PaymentDTO:
    payment_id: Optional[int]
    payee_first_name: Optional[str]
    payee_last_name: Optional[str]
    payee_payment_status: Optional[str]
    payee_added_date_utc: Optional[str]
    payee_due_date: Optional[str]
    payee_address_line_1: Optional[str]
    payee_address_line_2: Optional[str]
    payee_city: Optional[str]
    payee_country: Optional[str]
    payee_province_or_state: Optional[str]
    payee_postal_code: Optional[str]
    payee_phone_number: Optional[str]
    payee_email: Optional[str]
    discount_percent: Optional[float]
    tax_percent: Optional[float]
    due_amount: Optional[float]
    currency: str = "USD"

    @classmethod
    def from_dict(cls, data: dict) -> PaymentDTO:
        return PaymentDTO(
            payment_id=data["payment_id"],
            payee_first_name=data["payee_first_name"],
            payee_last_name=data["payee_last_name"],
            payee_payment_status=data["payee_status"],
            payee_added_date_utc=data["payee_added_date_utc"],
            payee_due_date=data["payee_due_date"],
            payee_address_line_1=data["payee_address_line_1"],
            payee_address_line_2=data["payee_address_line_2"],
            payee_city=data["payee_city"],
            payee_country=data["payee_country"],
            payee_province_or_state=data["payee_province_or_state"],
            payee_postal_code=data["payee_postal_code"],
            payee_phone_number=data["payee_phone_number"],
            payee_email=data["payee_email"],
            discount_percent=data["discount_percent"],
            tax_percent=data["tax_percent"],
            due_amount=data["due_amount"],
        )
