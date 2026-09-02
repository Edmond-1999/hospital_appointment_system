from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.controllers.patient_controller import router as patient_controller
from app.config.database import create_db_and_tables
from app.controllers.auth_controller import router as auth_controller
from app.controllers.admin_controller import router as admin_controller


@asynccontextmanager
async def lifespan(_app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(auth_controller)
app.include_router(patient_controller)
app.include_router(admin_controller)