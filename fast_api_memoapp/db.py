import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

base_dir = os.path.dirname(__file__)
DATABSE_URL = 'sqlite+aiosqlite:///' + os.path.join(base_dir, 'memodb.sqlite')

engine = create_async_engine(DATABSE_URL, echo = True)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_ = AsyncSession
)

async def get_dbsession():
    async with async_session() as session :
        yield session