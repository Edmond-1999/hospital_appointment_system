from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.controllers.user_controller import router as user_controller
from app.controllers.patient_controller import router as patient_controller
from app.config.database import create_db_and_tables


@asynccontextmanager
async def lifespan(_app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(user_controller)
app.include_router(patient_controller)