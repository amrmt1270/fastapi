from fastapi import FastAPI

app = FastAPI()

#GETかつエンドポイント[/]で呼ばれる関数
@app.get("/")
async def get_hello():
    return {'message' : 'Hello, World!'}

