import uvicorn
from fastapi import FastAPI

from src.controllers.payments_controller import PaymentsController

from src.data.api_models.get_payments_request_model import GetPaymentsRequestModel
from src.data.api_models.update_payment_request_model import UpdatePaymentRequestModel
from src.utils.normalise_payments_data import normalise_payments_data

app = FastAPI()

# Allow access to frontend app
# START ================================================================================================================
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:4200",
    "https://localhost:4200",
    "https://payments-fe-00f4df096687.herokuapp.com/",
    "https://payments-fe-00f4df096687.herokuapp.com/",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# END ==================================================================================================================

controller = PaymentsController()


@app.get("/")
async def root():
    # Load payments from file
    dataframe = normalise_payments_data()
    controller.store_payments(dataframe)
    return {"message": "Welcome to the Payments Management System"}


# PAYMENT APIS
@app.get("/payments")
async def get_payments(page_number:int = 0, request_model: GetPaymentsRequestModel = None):
    return controller.get_payments(page_number=page_number, request_model=request_model)

@app.put("/payment")
async def update_payment(payment_id:str, request_model: UpdatePaymentRequestModel):
    return controller.update_payment(payment_id=payment_id, request_model=request_model)


if __name__ == "__main__":
    # Start the server
    uvicorn.run(app, host="0.0.0.0", port=8000)
