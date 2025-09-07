from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from schemas.memo import InsertAndUpdateMemoSchema, MemoSchema, ResponseSchema
from fastapi.middleware.cors import CORSMiddleware
from routers.memo import router as memo_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins = ['http://127.0.0.1:5500',
                    "http://localhost:5500"],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

app.include_router(memo_router)

@app.exception_handler(ValidationError)
async def validation_exception_handler(exc: ValidationError):
    return JSONResponse(
        status_code = 422, 
        content = {'detail': exc.errors(),
                'body' : exc.model ,
                }
    )