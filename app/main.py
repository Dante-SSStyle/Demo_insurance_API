from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from app.database.models import DATABASE_URL
from app.routers import cargo_type_router, insurance_router, data_router

app = FastAPI(
    title='Insurance API',
    description='REST API сервис по расчёту стоимости страхования',
    docs_url='/docs',
    redoc_url='/doc'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=["*"]
)

app.include_router(
    cargo_type_router,
    prefix="/api/cargo",
    tags=["Cargo"],
    dependencies=[]
)

app.include_router(
    insurance_router,
    prefix="/api/insurance",
    tags=["Insurance"],
    dependencies=[]
)


app.include_router(
    data_router,
    prefix="/api",
    tags=["Data"],
    dependencies=[]
)


@app.on_event('startup')
async def startup():
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={'models': ['app.database.models']}
    )
    await Tortoise.generate_schemas()


@app.on_event('shutdown')
async def shutdown():
    await Tortoise.close_connections()
