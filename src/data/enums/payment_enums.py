from enum import Enum


class PaymentStatus(Enum):
    COMPLETED = "completed"
    DUE_NOW = "due_now"
    OVERDUE = "overdue"
    PENDING = "pending"
