from typing import Optional
from beanie.operators import  Set 
from ...dto.book_dto import BookSchema
from ..models.book_model import Book, Status


async def get_book_with_max_id(): 
    'The alternitive of autoincrement, return max id if it exist'
    
    book = await Book.find().sort(-Book.id).to_list()
    return book[0].id if book else None 


async def create_book(book : BookSchema):
    new_id = await get_book_with_max_id()
    new_book = Book(id= new_id+1 if new_id else 1, author=book.author, title=book.title, year=book.year)
    await new_book.insert()
    return new_book


async def delete_book(book_id : int):
    'delete book by id'
    
    book = await Book.get(document_id=book_id)
    if book:
        await book.delete()
        return f'Книга с id: {book_id} удалена.'
    else:
        return f'Книги с id: {book_id} не существует.'


async def get_all_books():
    result = await Book.find_all().to_list()
    return result
    
    
async def search_books(title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None):
    'searching books by creterias'
    
    query = {}
    
    if title:
        query["title"] = {"$regex": title, "$options": "i"}  
    if author:
        query["author"] = {"$regex": author, "$options": "i"}  
    if year:
        query["year"] = year 

    books = await Book.find(query).to_list()  
    if books:
        return books
    else:
        return 'По вашему запросу ничего не найдено'


async def change_book_status(book_id:int, new_status : Status):
    book = await Book.get(document_id=book_id)
    if book:
        await book.update(Set({Book.status : new_status}))
        await book.save()
        return f'Для книги с id: {book_id}  установлен статус: {new_status}.'
    else:
        return f'Книги с id: {book_id} не существует.'
    