import uvicorn
from fastapi import FastAPI
app = FastAPI()


from src.controllers.payment_controller import PaymentController
controller = PaymentController()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# PAYMENT APIs
@app.get("/payments")
async def get_payments():
    return controller.get_payments()

@app.put("/payment/{payment_id}")
async def update_payment(payment_id: int):
    return controller.update_payment(payment_id=payment_id)

@app.delete("/payment/{payment_id}")
async def delete_payment(payment_id: int):
    return controller.delete_payment(payment_id=payment_id)

@app.post("/payment")
async def create_payment():
    return controller.create_payment()

# EVIDENCE APIs
@app.post("/evidence")
async def upload_evidence():
    return controller.upload_evidence()

@app.get("/evidence/{evidence_id}")
async def download_evidence(evidence_id: int):
    return controller.download_evidence(evidence_id=evidence_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
