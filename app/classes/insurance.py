from app.classes import CommonClass
from app.models import InsuranceCreate, InsuranceExtract, InsuranceUpdate, InsuranceDelete
from app.database import InsuranceDB


class Insurance(CommonClass):

    @classmethod
    async def create(cls, insurance_data: InsuranceCreate) -> InsuranceDB:
        insurance = InsuranceDB(
            date=insurance_data.date,
            rate=insurance_data.rate,
            cargo_type_id=insurance_data.cargo_type
        )
        await insurance.save()
        return insurance

    @classmethod
    async def read(cls, insurance_data: InsuranceExtract) -> InsuranceDB:
        insurance = await InsuranceDB.filter(
            id=insurance_data.id
        ).first()
        cls._check404(insurance)
        return insurance

    @classmethod
    async def read_all(cls) -> list[InsuranceDB]:
        return await InsuranceDB.all().order_by("-date")

    @classmethod
    async def update(cls, insurance_data: InsuranceUpdate) -> InsuranceDB:
        cargo = InsuranceDB.filter(id=insurance_data.id).first()
        cls._check404(await cargo)
        await InsuranceDB.filter(id=insurance_data.id).update(
            date=insurance_data.date,
            rate=insurance_data.rate,
            cargo_type_id=insurance_data.cargo_type
        )
        return await cargo

    @classmethod
    async def delete(cls, insurance_data: InsuranceDelete) -> InsuranceDB:
        cargo = await InsuranceDB.filter(id=insurance_data.id).first()
        cls._check404(cargo)
        await cargo.delete()
        return cargo

