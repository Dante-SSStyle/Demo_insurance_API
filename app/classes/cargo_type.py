from app.classes import CommonClass
from app.models import CargoTypeCreate, CargoTypeExtract, CargoTypeUpdate, CargoTypeDelete
from app.database import CargoTypeDB


class CargoType(CommonClass):

    @classmethod
    async def create(cls, cargo_type: CargoTypeCreate) -> CargoTypeDB:
        cargo = CargoTypeDB(
            type=cargo_type.type,
            price=cargo_type.price
        )
        await cargo.save()
        return cargo

    @classmethod
    async def read(cls, cargo_type: CargoTypeExtract) -> CargoTypeDB:
        cargo = await CargoTypeDB.filter(
            id=cargo_type.id
        ).first()
        cls._check404(cargo)
        return cargo

    @classmethod
    async def read_all(cls) -> list[CargoTypeDB]:
        return await CargoTypeDB.all().prefetch_related("insurances")

    @classmethod
    async def update(cls, cargo_type: CargoTypeUpdate) -> CargoTypeDB:
        cargo = CargoTypeDB.filter(id=cargo_type.id).first()
        cls._check404(await cargo)
        await CargoTypeDB.filter(id=cargo_type.id).update(
            type=cargo_type.type,
            price=cargo_type.price
        )
        return await cargo

    @classmethod
    async def delete(cls, cargo_type: CargoTypeDelete) -> CargoTypeDB:
        cargo = await CargoTypeDB.filter(id=cargo_type.id).first()
        cls._check404(cargo)
        await cargo.delete()
        return cargo

