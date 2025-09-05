from fastapi import FastAPI,HTTPException
from books_schemas import BookSchema, BookResponseSchema


app = FastAPI()

books : list[BookResponseSchema] = [
    BookResponseSchema(id = 1, title = 'Python 入門', category = 'technical'),
    BookResponseSchema(id = 2, title = '初めてのプログラミング', category= 'technical'),
    BookResponseSchema(id = 3, title = 'すすむ巨人', category = 'comics'),
    BookResponseSchema(id = 4, title = 'DBおやじ', category = 'comics'),
    BookResponseSchema(id = 5, title = '週刊ダイヤモンド', category= 'magazine'),
    BookResponseSchema(id = 6, title = 'ザ・社長', category = 'magazine')
]

@app.post("/books/")
def create_book(book:BookSchema):
    new_book_id = max([book.id for book in books], default = 0) + 1
    new_book = BookResponseSchema(id = new_book_id, **book.model_dump())
    books.append(new_book)
    return new_book


@app.get("/books/", response_model= list[BookResponseSchema])
def read_books():
    return books

@app.get('/books/{book_id}', response_model = BookResponseSchema)
def read_book(book_id : int):
    for book in books :
        if book.id == book_id :
            return book
    raise HTTPException(status_code=404, detail = 'Book not found')

@app.put("/books/{book_id}", response_model=BookResponseSchema)
def update_book(book_id :int, book :BookSchema) :
    for index, exisiting_book in enumerate(books) :
        if exisiting_book.id == book_id :
            updated_book = BookResponseSchema(id = book_id, **book.model_dump())
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail = "Book Not Found")

@app.delete("/books/{book_id}", response_model = BookResponseSchema)
def delete_book(book_id : int):
    for index, book in enumerate(books):
        if book.id == book_id :
            books.pop(index)
            return book
    raise HTTPException(status_code=404, detail = 'Book Not Found')