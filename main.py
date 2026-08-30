from fastapi import FastAPI

from app.controllers.user_controller import router as user_router, router
from app.controllers.doctor_controller import router as doctor_router
from app.controllers.patient_controller import router as patient_router

app = FastAPI()

app.include_router(user_router)
app.include_router(doctor_router)
app.include_router(patient_router)