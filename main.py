from fastapi import FastAPI
from app.controllers.patient_controller import router as patient_router

app = FastAPI(title="Hospital Appointment System API")

app.include_router(patient_router)