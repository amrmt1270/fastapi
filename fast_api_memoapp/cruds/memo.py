from datetime import datetime, timezone
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import schemas.memo as memo_schema
import models.memo as memo_model

async def insert_memo(
    db_session: AsyncSession,
    memo_data: memo_schema.InsertAndUpdateMemoSchema
) -> memo_model.Memo:
    """
    新しいメモを登録
    """
    print('=== 新規登録：開始 ===')
    new_memo = memo_model.Memo(**memo_data.model_dump())
    try:
        db_session.add(new_memo)
        await db_session.commit()
        await db_session.refresh(new_memo)
        print(">>> データ追加完了")
        return new_memo
    except Exception as e:
        await db_session.rollback()
        print("!!! 追加失敗:", e)
        raise

async def get_memos(db_session: AsyncSession) -> list[memo_model.Memo]:
    """
    すべてのメモを取得（新しいID順）
    """
    print('=== 全件取得：開始 ===')
    result = await db_session.execute(
        select(memo_model.Memo).order_by(memo_model.Memo.memo_id.desc())
    )
    memos = result.scalars().all()
    print('>>> データ全件取得完了')
    return memos

async def get_memo_by_id(
    db_session: AsyncSession,
    memo_id: int
) -> memo_model.Memo | None:
    """
    主キーで1件取得
    """
    print('=== 1件取得：開始 ===')
    result = await db_session.execute(
        select(memo_model.Memo).where(memo_model.Memo.memo_id == memo_id)
    )
    memo = result.scalars().first()
    print('>>> データ取得完了')
    return memo

async def update_memo(
    db_session: AsyncSession,
    memo_id: int,
    target_data: memo_schema.InsertAndUpdateMemoSchema
) -> memo_model.Memo | None:
    """
    メモを更新
    """
    print('=== データ更新：開始 ===')
    memo = await get_memo_by_id(db_session, memo_id)
    if not memo:
        print('>>> 対象なし（更新スキップ）')
        return None

    memo.title = target_data.title
    memo.description = target_data.description
    # モデルに updated_at 列がある前提。なければ削除してください。
    if hasattr(memo, "updated_at"):
        memo.updated_at = datetime.now(timezone.utc)

    try:
        await db_session.commit()
        await db_session.refresh(memo)
        print('>>> データ更新完了')
        return memo
    except Exception as e:
        await db_session.rollback()
        print("!!! 更新失敗:", e)
        raise

async def delete_memo(
    db_session: AsyncSession,
    memo_id: int
) -> memo_model.Memo | None:
    """
    メモを削除
    """
    print('=== データ削除：開始 ===')
    memo = await get_memo_by_id(db_session, memo_id)
    if not memo:
        print('>>> 対象なし（削除スキップ）')
        return None

    try:
        await db_session.delete(memo)
        await db_session.commit()
        print('>>> データ削除完了')
        return memo
    except Exception as e:
        await db_session.rollback()
        print("!!! 削除失敗:", e)
        raise
