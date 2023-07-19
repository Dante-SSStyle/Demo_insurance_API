from datetime import date
from pydantic import BaseModel


class InsuranceBase(BaseModel):
    id: int


class InsuranceCreate(BaseModel):
    date: date
    rate: float
    cargo_type: int


class InsuranceExtract(InsuranceBase):
    pass


class InsuranceUpdate(InsuranceBase):
    date: date
    rate: float
    cargo_type: int


class InsuranceDelete(InsuranceBase):
    pass


class Insurance(InsuranceBase):
    date: date
    rate: float
    cargo_type: int

    class Config:
        orm_mode = True
