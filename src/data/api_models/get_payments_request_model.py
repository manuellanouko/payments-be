from typing import Optional
from pydantic import BaseModel
from src.data.enums.payment_enums import PaymentFilterColumns


class GetPaymentsRequestModel(BaseModel):
    filters: Optional[dict]
    search_text: Optional[str]

    @property
    def are_filters_valid(self) -> bool:
        if self.filters:
            for key in self.filters.keys():
                if key not in PaymentFilterColumns.get_all():
                    return False
        return True