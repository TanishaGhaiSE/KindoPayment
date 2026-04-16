from app.api.v1.endpoints import payments
from app.api.v1.endpoints import registration
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import trips
from app.core import middleware
from app.core.exception import AppException
from app.db.database import engine, Base

from app.api.v1.endpoints import students


# Lifespan = app bootstrap layer
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("Database initialized")

    yield

    print("App shutting down")


# ✅ App instance (composition root)
app = FastAPI(title="Payment API", lifespan=lifespan)

# ✅ Register routes
app.include_router(trips.router, prefix="/api/v1", tags=["Trips"])
app.include_router(registration.router, prefix="/api/v1", tags=["Registrations"])
app.include_router(payments.router, prefix="/api/v1", tags=["Payments"])
app.include_router(students.router, prefix="/api/v1", tags=["Students"])

app.add_exception_handler(AppException, middleware.app_exception_handler)
app.add_exception_handler(Exception, middleware.generic_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)