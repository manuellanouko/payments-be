import uvicorn
from fastapi import FastAPI

from src.controllers.payments_controller import PaymentsController
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
    dataframe = normalise_payments_data()
    controller.store_payments(dataframe)
    return {"message": "Welcome to the Payments Management System"}


# PAYMENT APIS
@app.get("/payments")
async def get_payments(page_number:int = 0):
    return controller.get_payments(page_number=page_number)


# if __name__ == "__main__":
#     # Load payments from file
#     # dataframe = normalise_payments_data()
#     # controller.store_payments(dataframe)
#     # Start the server
#     uvicorn.run(app, host="0.0.0.0", port=8000)
