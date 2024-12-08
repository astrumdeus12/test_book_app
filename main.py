from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.routers.book_router import book_router
import uvicorn
from app.dao.database import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app : FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(book_router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        
        status_code=422,
        content={"message": "Введен неверный тип данных."},
    )


uvicorn.run(app)

