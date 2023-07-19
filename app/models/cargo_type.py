from typing import List
from pydantic import BaseModel, Field
from .insurance import Insurance


class CargoTypeBase(BaseModel):
    id: int


class CargoTypeCreate(BaseModel):
    type: str = Field(min_length=1, max_length=60)
    price: float


class CargoTypeExtract(CargoTypeBase):
    pass


class CargoTypeUpdate(CargoTypeBase):
    type: str = Field(min_length=1, max_length=60)
    price: float


class CargoTypeDelete(CargoTypeBase):
    pass


class CargoType(CargoTypeBase):
    type: str = Field(min_length=1, max_length=60)
    price: float
    insurances: List[Insurance]

    class Config:
        orm_mode = True
