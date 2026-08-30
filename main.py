from fastapi import FastAPI
from app.controllers import auth_controller, patient_controller, admin_controller, doctor_controller

app = FastAPI(
    title="Hospital Appointment System API",
    version="1.0.0",
)

app.include_router(auth_controller.router)
app.include_router(patient_controller.router)
app.include_router(admin_controller.router)
app.include_router(doctor_controller.router)