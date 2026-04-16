# app/api/v1/routes/registration_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.database import get_session
from app.services.registration_service import RegistrationService
from app.repositories.registrations import RegistrationRepository
from app.api.v1.models.registration import RegistrationCreate

router = APIRouter(prefix="/registrations", tags=["Registrations"])


def get_service():
    return RegistrationService(RegistrationRepository())


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_registration(
    payload: RegistrationCreate,
    session: Session = Depends(get_session),
    service: RegistrationService = Depends(get_service),
):
    try:
        return service.create_registration(session, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))