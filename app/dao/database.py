from beanie import init_beanie
import motor.motor_asyncio
from config import DATABASE_URL
from .models.book_model import Book

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
    await init_beanie(database=client.Clustermongo,
                      document_models=[Book])