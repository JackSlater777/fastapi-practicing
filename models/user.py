from pydantic import BaseModel


class User(BaseModel):
    id: int
    role: str
    name: str
