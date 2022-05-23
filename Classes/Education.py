from enum import Enum


class University(Enum):
    KU = 1
    DTU = 2

class Education():
    def __init__(self, EducationID: int, Title: str, University: University) -> None:
        self.EducationID = EducationID
        self.Title = Title
        self.University = University