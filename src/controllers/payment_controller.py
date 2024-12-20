from src.models.payee_model import Payee as PayeeModel


class PaymentController:
    def __init__(self):
        self.model = PayeeModel()
    def get_payments(self):
        return self.model.get_payments()

    def update_payment(self, payment_id: int):
        return self.model.update_payment()

    def delete_payment(self, payment_id: int):
        return self.model.delete_payment()

    def create_payment(self):
        return self.model.create_payment()

    def upload_evidence(self):
        return self.model.upload_evidence()

    def download_evidence(self, evidence_id: int):
        return self.model.download_evidence()
