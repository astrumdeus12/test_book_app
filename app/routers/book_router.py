from typing import List, Optional
from fastapi import APIRouter
from ..dto.book_dto import BookSchema
from ..dao.models.book_model import Book, Status
from ..dao.services.book_services import create_book,change_book_status, get_all_books, search_books, delete_book



book_router = APIRouter(prefix='/book')

@book_router.post('book/')
async def add_new_book(book : BookSchema):
    result = await create_book(book)
    return f'Вы добавили новую книгу: \n {result}'


@book_router.get('book/all')
async def read_all_books():
    result =  await get_all_books()
    return result


@book_router.get('book/search', response_model = List[Book] | str)
async def read_books_criteria(title: Optional[str] = None,
                              author: Optional[str] = None, 
                              year: Optional[int] = None):
    result = await search_books(title, author, year)
    return result


@book_router.delete('book/delete')
async def delete_book_by_id(book_id : int):
    result = await delete_book(book_id)
    return result


@book_router.patch('book/update')
async def change_status(book_id :int, new_status : Status):
    result = await change_book_status(book_id, new_status)
    return result

