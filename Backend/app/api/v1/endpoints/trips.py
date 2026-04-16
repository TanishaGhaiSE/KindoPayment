from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import Session


from app.models.trips import Trips
from app.services.trip_service import TripService
from app.repositories.trip import TripRepositoryImpl as TripRepository
from app.db.database import get_session


router = APIRouter()


# Dependency Injection (Factory)
def get_trip_service(session: Session = Depends(get_session)):
    repo = TripRepository(session)
    return TripService(repo)



@router.get("/trips", response_model=List[Trips])
def get_all_trips(service: TripService = Depends(get_trip_service)):
    trips = service.list_trips()
    return trips

@router.get("/trips/{trip_id}", response_model=Trips)
def get_trip_by_id(
    trip_id: int,
    service: TripService = Depends(get_trip_service),
):
    trip = service.get_trip(trip_id)

    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trip not found",
        )

    return trip


@router.post("/trips", response_model=Trips, status_code=status.HTTP_201_CREATED)
def create_trip(
    trip: Trips,
    service: TripService = Depends(get_trip_service),
):
    created_trip = service.create_trip(trip)
    return created_trip

