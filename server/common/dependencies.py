from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from .settings import POSTGRES_URL,JWT_EXPIRE,JWT_SECRET,JWT_METHOD


async_engine = create_async_engine(POSTGRES_URL)


async def db_session():
    async with AsyncSession(async_engine) as session:
        yield session


AsyncDBSession:AsyncSession = Depends(db_session)