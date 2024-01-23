from pydantic import BaseModel
from datetime import datetime
from enums.degree import DegreeType
from typing import Optional


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class UserToAdd(BaseModel):
    role: str
    name: str
    degree: Optional[list[Degree]]


class User(UserToAdd):
    id: int
    degree: list[Degree] = []
    # role: str
    # name: str
    # degree: Optional[list[Degree]] = []
