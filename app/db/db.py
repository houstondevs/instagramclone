from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine

from app.settings.config import DATABASE_URL


engine = create_async_engine(DATABASE_URL, echo=True, future=True)
Base = declarative_base()


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
