import pytest
from unittest.mock import MagicMock

from app.services.trip_service import TripService
from app.models.trips import Trips

@pytest.fixture
def mock_repo():
    return MagicMock()


@pytest.fixture
def trip_service(mock_repo):
    return TripService(trip_repo=mock_repo)


# =========================
# TEST: LIST TRIPS
# =========================

def test_list_trips(trip_service, mock_repo):
    mock_repo.list.return_value = [
        Trips(id=1, title="Zoo Trip", cost=50),
        Trips(id=2, title="Museum Trip", cost=30),
    ]

    result = trip_service.list_trips()

    assert len(result) == 2
    mock_repo.list.assert_called_once()


# =========================
# TEST: GET TRIP SUCCESS
# =========================

def test_get_trip_success(trip_service, mock_repo):
    mock_trip = Trips(id=1, title="Zoo Trip", cost=50)
    mock_repo.get.return_value = mock_trip

    result = trip_service.get_trip(1)

    assert result.id == 1
    assert result.title == "Zoo Trip"
    mock_repo.get.assert_called_once_with(1)


# =========================
# TEST: GET TRIP NOT FOUND
# =========================

def test_get_trip_not_found(trip_service, mock_repo):
    mock_repo.get.return_value = None

    with pytest.raises(ValueError) as exc:
        trip_service.get_trip(1)

    assert "Trip with id 99 not found" in str(exc.value)


# =========================
# TEST: CREATE TRIP SUCCESS
# =========================

def test_create_trip_success(trip_service, mock_repo):
    trip = Trips(name="Zoo Trip", cost=50)

    mock_repo.create.return_value = trip

    result = trip_service.create_trip(trip)

    assert result.cost == 50
    mock_repo.create.assert_called_once_with(trip)


# =========================
# TEST: CREATE TRIP NEGATIVE COST
# =========================

def test_create_trip_negative_cost(trip_service, mock_repo):
    trip = Trips(title="Invalid Trip", cost=-10)

    with pytest.raises(ValueError) as exc:
        trip_service.create_trip(trip)

    assert "Trip price cannot be negative" in str(exc.value)


# =========================
# TEST: DELETE TRIP SUCCESS
# =========================

def test_delete_trip_success(trip_service, mock_repo):
    mock_repo.delete.return_value = True

    result = trip_service.delete_trip(1)

    assert result is True
    mock_repo.delete.assert_called_once_with(1)


# =========================
# TEST: DELETE TRIP NOT FOUND
# =========================

def test_delete_trip_not_found(trip_service, mock_repo):
    mock_repo.delete.return_value = False

    with pytest.raises(ValueError) as exc:
        trip_service.delete_trip(99)

    assert "Trip with id 99 not found" in str(exc.value)