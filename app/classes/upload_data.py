import json
from datetime import datetime
from typing import List
from fastapi import File
from pydantic import Json
from app.database import CargoTypeDB, InsuranceDB
from app.classes import CommonClass, Insurance
from app.exceptions import ApiException
from app.models import InsuranceCreate, InsuranceUpdate, CalculateData


class UploadedData(CommonClass):

    @classmethod
    async def upload_data(cls, data: Json) -> List[InsuranceDB]:
        date_list = cls.validate_dates(data)
        await cls.process_data(data)
        result = await InsuranceDB.filter(date__in=date_list).all()
        return result

    @classmethod
    async def upload_file(cls, file: bytes = File(...)) -> List[InsuranceDB]:
        data = json.loads(file)
        return await cls.upload_data(data)

    @classmethod
    async def calculate_data(cls, data: CalculateData) -> dict:
        cargo = await CargoTypeDB.filter(type=data.cargo_type).first()
        cls._check_cargo404(cargo, data.cargo_type)

        insurance = await InsuranceDB().filter(cargo_type=cargo, date__lte=data.date).order_by("-date").first()
        if insurance:
            summ = cargo.price * insurance.rate
        else:
            raise ApiException(status_code=400, detail=f"No actual insurance info for this date: {data.date}")

        return {"insurance summ": summ}

    @classmethod
    def validate_dates(self, data: Json) -> List:
        date_list = []
        for date in data.keys():
            try:
                datetime.strptime(date, "%Y-%m-%d").date()
                date_list.append(date)
            except ValueError:
                raise ApiException(status_code=400, detail="Неверный формат даты")
        return date_list

    @classmethod
    async def process_data(cls, data: Json) -> None:
        for date, list_data in data.items():
            for dic in list_data:
                # check keys and cargo
                if {"cargo_type", "rate"} <= dic.keys():
                    cargo = await CargoTypeDB().filter(type=dic["cargo_type"]).first()
                    cls._check_cargo404(cargo, dic["cargo_type"])

                    # process insurances
                    kwargs = {"date": date, "rate": dic["rate"], "cargo_type": cargo.id}
                    ins_data = InsuranceCreate(**kwargs)

                    insurance = await InsuranceDB().filter(cargo_type=cargo, date=date).first()
                    if not insurance:
                        await Insurance.create(ins_data)
                    else:
                        kwargs["id"] = insurance.id
                        ins_data = InsuranceUpdate(**kwargs)
                        await Insurance.update(ins_data)
