from src.database.models import payments_model


class PaymentsController:
    def get_payments(self, page_number:int = 0):
        return payments_model.get_payments(page_number=page_number)

    def store_payments(self, data_frame):
        return payments_model.store_payments(data_frame)
