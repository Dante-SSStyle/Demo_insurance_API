from fastapi import APIRouter, File
from pydantic import Json
from app.classes import UploadedData
from app.models import CalculateData

router = APIRouter()


@router.post("/upload", description="Отправить json с данными")
async def upload_data(data: Json):
    return await UploadedData.upload_data(data)


@router.post("/upload_file", description="Получить данные из .json файла")
async def upload_file(file: bytes = File(...)):
    return await UploadedData.upload_file(file)


@router.post("/calculate", description="Рассчитать стоимость страхования")
async def calculate(data: CalculateData):
    return await UploadedData.calculate_data(data)
