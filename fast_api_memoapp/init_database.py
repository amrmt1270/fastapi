import os
from sqlalchemy.ext.asyncio import create_async_engine
from models.memo import Base
import asyncio

base_dir = os.path.dirname(__file__)
DATABASE_URL = 'sqlite+aiosqlite:///' + os.path.join(base_dir, 'memodb.sqlite')

engine = create_async_engine(DATABASE_URL, echo = True)

async def init_db():
    print('=== データベースの初期化を開始 ===')
    async with engine.begin() as conn :
        await conn.run_sync(Base.metadata.drop_all)
        print('既存のテーブルを削除しました')
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__' :
    asyncio.run(init_db())