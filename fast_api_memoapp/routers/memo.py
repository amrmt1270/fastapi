from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.memo import InsertAndUpdateMemoSchema, MemoSchema, ResponseSchema
import cruds.memo as memo_crud
import db

router = APIRouter(tags = ['Memos'], prefix='/memos')
@router.post('/', response_model = ResponseSchema)
async def create_memo(memo: InsertAndUpdateMemoSchema, db : AsyncSession = Depends(db.get_dbsession)):
    try:
        await memo_crud.insert_memo(db, memo)
    except Exception as e :
        raise HTTPException(status_code=400, details = 'メモの登録に失敗しました')
    
@router.get('/', response_model = list[MemoSchema])
async def get_memo_list(db : AsyncSession = Depends(db.get_dbsession)):
    memos = await memo_crud.get_memos(db)
    return memos

@router.get('/{memo_id}', response_model = MemoSchema)
async def get_memo_detail(memo_id : int,
                          db:AsyncSession = Depends(db.get_dbsession)):
    memo = await memo_crud.get_memo_by_id(db, memo_id)
    if not memo :
        raise HTTPException(status_code=404, detail = 'メモが見つかりません')
    return memo

@router.put('/{memo_id}', response_model = ResponseSchema)
async def modify_memo(memo_id :int, memo :InsertAndUpdateMemoSchema,
                    db : AsyncSession = Depends(db.get_dbsession)):
    updated_memo = await memo_crud.update_memo(db, memo_id, memo)
    if not updated_memo :
        raise HTTPException(status_code=404, detail = '更新対象が見つかりません')
    return ResponseSchema(message = 'メモが正常に更新されました')

@router.delete('/{memo_id}', response_model = ResponseSchema)
async def remove_memo(memo_id : int,
                      db : AsyncSession = Depends(db.get_dbsession)):
    result = await memo_crud.delete_memo(db, memo_id)
    if not result:
        raise HTTPException(status_code=404, detail = '削除対象が見つかりません')
    return ResponseSchema(message = 'メモが正常に削除されました')