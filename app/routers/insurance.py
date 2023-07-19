from fastapi import APIRouter
from app.classes import Insurance
from app.models import InsuranceCreate, InsuranceExtract, InsuranceUpdate, InsuranceDelete

router = APIRouter()


@router.post("/", description="Создать данные страховки")
async def create_cargo(insurance: InsuranceCreate):
    return await Insurance.create(insurance)


@router.get("/", description="Получить все данные страховки")
async def get_all_cargo():
    return await Insurance.read_all()


@router.get("/{insurance_id}", description="Получить конкретные данные страховки")
async def get_cargo(insurance_id: int):
    return await Insurance.read(InsuranceExtract(id=insurance_id))


@router.put("/", description="Обновить данные страховки")
async def update_cargo(insurance: InsuranceUpdate):
    return await Insurance.update(insurance)


@router.delete("/", description="Удалить данные страховки")
async def delete_cargo(insurance: InsuranceDelete):
    return await Insurance.delete(insurance)
