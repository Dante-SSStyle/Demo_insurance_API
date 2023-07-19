from datetime import date
from pydantic import BaseModel


class CalculateData(BaseModel):
    cargo_type: str
    date: date
