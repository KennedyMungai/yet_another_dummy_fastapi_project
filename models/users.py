from datetime import date
from enum import Enum
from typing import List

from pydantic import BaseModel, ValidationError


class Gender(str, Enum):
    """The gender enum class

    Args:
        str (String): String
        Enum (Enum): The enums
    """
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"


class Person(BaseModel):
    """The Person model

    Args:
        BaseModel (Pydantic): The base class for all pydantic models
    """
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]
