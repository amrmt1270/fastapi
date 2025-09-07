from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import schemas.memo as memo_schema
import models.memo as memo_model
from datetime import datetime

async def insert_memo(
        db_session:AsyncSession,
        memo_data :memo_schema.InsertAndUpdateMemoSchema)-> memo_model.Memo :
    """
        新しいメモをデータベースに登録する関数
        Args:
            db_session(AsyncSession): 非同期dbセッション
            memo_data (InsertAndUpdateMemoSchema) :作成するメモのデータ
        Returns :
            Memo : 作成されたメモのモデル
    """
    print('=== 新規登録：開始 ===')
    new_memo = memo_model.Memo(**memo_data.model_dump())
    db_session.add(new_memo)
    await db_session.commit()
    await db_session.refresh(new_memo)
    print(">>>データ追加完了")
    return new_memo

async def get_memos(db_session :AsyncSession) -> list[memo_model.Memo] :
    """
        データベースからすべてのメモを取得する関数
        Args :
            db_session (AsyncSession) : 非同期DBセッション
        Returns:
            list[Memo] : 取得されたすべてのメモのリスト
    """
    print('===全権取得：開始===')
    result = await db_session.execute(select(memo_model.Memo))
    memos = result.scalars().all()
    print('>>>データが全件取得完了')
    return memos

async def get_memo_by_id(db_session : AsyncSession,
                        memo_id : int) -> memo_model.Memo | None:
    """
        データベースから特定のメモを一件取得する関数
        Args :
            db_session (AsyncSession): 非同期型DBセッション
            memo_id (int) : 取得するメモのID(プライマリーキー)
        Returns :
            Memo | None : 取得されたメモのモデル、メモが存在しない場合はNoneを返す
    """
    print('=== 1件取得：開始 ===')
    result = await db_session.execute(
        select(memo_model.Memo).where(memo_model.Memo.memo_id == memo_id))
    memo = result.scalars().first()
    print('>>> データ取得完了')
    return memo

async def update_memo(db_session: AsyncSession, 
                    memo_id : int,
                    target_data : memo_schema.InsertAndUpdateMemoSchema) -> memo_model.Memo | None:
    """
        データベースのメモを更新する関数
        Args :
            db_session (AsyncSession) : 非同期DBセッション
            memo_id (int) : 更新するメモのID
            target_data (InsertAndUpdateMemoSchema): 更新するデータ
        Returns :
            Memo | None : 更新されたメモのモデル, メモが存在しない場合はNoneを返す
    """
    print('=== データ更新 開始===')
    memo = await get_memo_by_id(db_session, memo_id)
    if memo :
        memo.title = target_data.title
        memo.description = target_data.description
        memo.update_at = datetime.now()
        await db_session.commit()
        await db_session.refresh(memo)
        print('>>>データ更新完了')
    return memo

async def delete_memo(db_session :AsyncSession,
                    memo_id : int) -> memo_model.Memo | None:
    """
        データベースのメモを削除する関数
        Args :
            db_session (AsyncSession)
            memo_id : int
        Returns :
            Memo | None 削除されたメモのモデル、メモが存在しない売位はNone を返す
    """
    print('=== データ削除: 開始===')
    memo = await get_memo_by_id(db_session, memo_id)
    if memo :
        await db_session.delete(memo)
        await db_session.commit()
        print('>>> データ削除完了')
    return memo 
