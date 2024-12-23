from enum import Enum


class PaymentStatus(Enum):
    COMPLETED = "completed"
    DUE_NOW = "due_now"
    OVERDUE = "overdue"
    PENDING = "pending"


class PaymentFilterColumns(Enum):
    FILTER_FIRST_NAME = "payee_first_name"
    FILTER_LAST_NAME = "payee_last_name"
    FILTER_STATUS = "payee_payment_status"
    FILTER_ADDRESS = "payee_address_line_1"
    FILTER_ADDRESS_LINE_2 = "payee_address_line_2"
    FILTER_CITY = "payee_city"
    FILTER_COUNTRY = "payee_country"
    FILTER_PROVINCE_OR_STATE = "payee_province_or_state"
    FILTER_POSTAL_CODE = "payee_postal_code"
    FILTER_PHONE_NUMBER = "payee_phone_number"
    FILTER_EMAIL = "payee_email"
    FILTER_CURRENCY = "currency"

    @staticmethod
    def get_all():
        return [
            PaymentFilterColumns.FILTER_FIRST_NAME.value,
            PaymentFilterColumns.FILTER_LAST_NAME.value,
            PaymentFilterColumns.FILTER_STATUS.value,
            PaymentFilterColumns.FILTER_CITY.value,
            PaymentFilterColumns.FILTER_COUNTRY.value,
            PaymentFilterColumns.FILTER_PROVINCE_OR_STATE.value,
            PaymentFilterColumns.FILTER_POSTAL_CODE.value,
            PaymentFilterColumns.FILTER_PHONE_NUMBER.value,
            PaymentFilterColumns.FILTER_EMAIL.value,
            PaymentFilterColumns.FILTER_CURRENCY.value,
        ]
