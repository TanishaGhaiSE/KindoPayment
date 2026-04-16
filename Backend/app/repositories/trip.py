from datetime import datetime
from typing import Optional, List
from sqlmodel import Session, select

from app.models.trips import Trips
from app.repositories.interfaces import TripRepository as TripRepositoryInterface


class TripRepositoryImpl(TripRepositoryInterface):

    def __init__(self, session: Session):
        self.session = session

    def get(self, trip_id: int) -> Optional[Trips]:
        return self.session.get(Trips, trip_id)

    def list(self) -> List[Trips]:
        return self.session.exec(select(Trips)).all()


    def create(self, trip: Trips) -> Trips:
        if isinstance(trip.date, str):
            trip.date = datetime.fromisoformat(trip.date).date()
        self.session.add(trip)
        self.session.commit()
        self.session.refresh(trip)
        return trip

    

    def delete(self, trip_id: int) -> bool:
        trip = self.session.get(Trips, trip_id)
        if not trip:
            return False

        self.session.delete(trip)
        self.session.commit()
        return True