from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World"


# @app.get("/book")
# def read_users(db: Session = Depends(database.get_db)):
#     books = db.query(models.Book).all()
#     return books

from sqlalchemy.orm import joinedload

@app.get("/book")
def read_books(db: Session = Depends(database.get_db)):
    books = db.query(models.Book).options(
        joinedload(models.Book.authors), 
        joinedload(models.Book.genres)
    ).all()

    result = []
    for book in books:
        result.append({
            "id": book.id,
            "title": book.title,
            "copies_available": book.copies_available,
            "total_copies": book.total_copies,
            "publication_year": book.publication_year,
            "authors": [{"id": author.id, "name": author.name} for author in book.authors],
            "genres": [{"id": genre.id, "name": genre.name} for genre in book.genres],
        })
    return result




@app.get("/book/{book_id}")
def read_book(book_id: int, db: Session = Depends(database.get_db)):
    book = db.query(models.Book).options(
        joinedload(models.Book.authors),
        joinedload(models.Book.genres)
    ).filter(models.Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return {
        "id": book.id,
        "title": book.title,
        "copies_available": book.copies_available,
        "total_copies": book.total_copies,
        "publication_year": book.publication_year,
        "authors": [{"id": author.id, "name": author.name} for author in book.authors],
        "genres": [{"id": genre.id, "name": genre.name} for genre in book.genres],
    }


@app.get("/genre")
def read_users(db: Session = Depends(database.get_db)):
    genres = db.query(models.Genre).all()
    return genres


@app.get("/author")
def read_users(db: Session = Depends(database.get_db)):
    Authers = db.query(models.Author).all()
    return Authers
