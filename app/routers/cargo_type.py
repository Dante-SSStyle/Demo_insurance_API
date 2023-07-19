from fastapi import APIRouter
from app.classes import CargoType
from app.models import CargoTypeExtract, CargoTypeCreate, CargoTypeUpdate, CargoTypeDelete

router = APIRouter()


@router.post("/", description="Создать груз")
async def create_cargo(cargo: CargoTypeCreate):
    return await CargoType.create(cargo)


@router.get("/", description="Получить все типы грузов")
async def get_all_cargo():
    return await CargoType.read_all()


@router.get("/{cargo_type_id}", description="Получить конкретный груз")
async def get_cargo(cargo_type_id: int):
    return await CargoType.read(CargoTypeExtract(id=cargo_type_id))


@router.put("/", description="Обновить данные груза")
async def update_cargo(cargo: CargoTypeUpdate):
    return await CargoType.update(cargo)


@router.delete("/", description="Удалить груз")
async def delete_cargo(cargo: CargoTypeDelete):
    return await CargoType.delete(cargo)
