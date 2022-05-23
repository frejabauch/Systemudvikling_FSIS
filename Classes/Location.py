from enum import Enum

class LocationType(Enum):
    LectureHall = 1
    Classroom = 2
    StudyHall = 3
    Studyroom = 4

class Location():
    def __init__(self, Address: str, RoomID: int, LocationType: LocationType, Capacity: int) -> None:
        self.Address = Address
        self.RoomID = RoomID
        self.LocationType = LocationType
        self.Capacity = Capacity