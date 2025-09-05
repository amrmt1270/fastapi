from fastapi import APIRouter
from schemas.item import Item

router = APIRouter()
@router.get("/items/", response_model = dict)
async def read_items():
    return {'message': '商品一覧を表示', 'items' : []}

@router.post('/items/{item_id}', response_model = dict)
async def create_item(item: Item) :
    return {'message' : '商品を作成しました', 'item':item}

@router.put('/items/{item_id}')
async def update_item(item_id : int, item:Item) :
    return {'message' : '商品を更新しました',
            'item_id' : item_id, 'item': item}

@router.delete('/items/{item_id}', response_model = dict)
async def delte_item(item_id : int):
    return {'message' : '商品を削除しました',
            'item_id' : item_id}


