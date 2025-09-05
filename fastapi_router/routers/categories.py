from fastapi import FastAPI, APIRouter
from schemas.category import Category

router = APIRouter()

@router.get('/categories/', response_model = dict)
async def read_categories():
    return {'message' : 'カテゴリーを表示', 'categories' : []}

@router.post('/categories/', response_model = dict)
async def create_category(category :Category):
    return {'message': 'カテゴリーを作成しました', 'category' : category}


@router.put('/categories/{category_id}', response_model = dict)
async def update_category(category_id :int, category : Category):
    return {'message' : 'カテゴリを更新しました',
            "category_id" : category_id, 'category' : category}

@router.delete('/categories/{category_id}', response_model = dict)
async def delete_category(category_id: int):
    return {'message': 'カテゴリを削除しました', 
            'category_id': category_id}
