from typing import List, Optional
from app.models.trips import Trips
from app.repositories.trip import TripRepositoryImpl


class TripService:

    def __init__(self, trip_repo: TripRepositoryImpl):
        self.trip_repo = trip_repo

    # =========================
    # READ OPERATIONS
    # =========================

    def list_trips(self) -> List[Trips]:
        return self.trip_repo.list()

    def get_trip(self, trip_id: int) -> Trips:
        trip = self.trip_repo.get(trip_id)

        if not trip:
            raise ValueError(f"Trip with id {trip_id} not found")

        return trip

    # =========================
    # WRITE OPERATIONS
    # =========================

    def create_trip(self, trip: Trips) -> Trips:
        # business rule example (can expand later)
        if trip.cost < 0:
            raise ValueError("Trip price cannot be negative")

        return self.trip_repo.create(trip)


    def delete_trip(self, trip_id: int) -> bool:
        success = self.trip_repo.delete(trip_id)

        if not success:
            raise ValueError(f"Trip with id {trip_id} not found")

        return success