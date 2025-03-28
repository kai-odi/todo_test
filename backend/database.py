from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from backend import settings

engine = create_async_engine(
    f"postgresql+asyncpg://{settings.settings.DB_USER}:{settings.settings.DB_PASSWORD}"
    f"@{settings.settings.DB_HOST}:{settings.settings.DB_PORT}/{settings.settings.DB_NAME}"
)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
