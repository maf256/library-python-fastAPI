# from sqlalchemy import Column, Integer, String, DATE
# from database import Base

# class Book(Base):
#     __tablename__ = "book"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     copies_available = Column(Integer)
#     total_copies = Column(Integer)
#     publication_year = Column(Integer)


# class Genre(Base):
#     __tablename__ = "genre"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)



# class Author(Base):
#     __tablename__ = "author"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     biography = Column(String)
#     birthday = Column(DATE)




from sqlalchemy import Column, Integer, String, DATE, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# جداول واسطه برای Many-to-Many
book_authors = Table(
    "book_authors",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("book.id"), primary_key=True),
    Column("author_id", Integer, ForeignKey("author.id"), primary_key=True)
)

book_genres = Table(
    "book_genres",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("book.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genre.id"), primary_key=True)
)

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    copies_available = Column(Integer)
    total_copies = Column(Integer)
    publication_year = Column(Integer)

    # رابطه Many-to-Many
    authors = relationship("Author", secondary=book_authors, back_populates="books")
    genres = relationship("Genre", secondary=book_genres, back_populates="books")

class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    biography = Column(String)
    birthday = Column(DATE)

    # رابطه معکوس با Book
    books = relationship("Book", secondary=book_authors, back_populates="authors")

class Genre(Base):
    __tablename__ = "genre"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # رابطه معکوس با Book
    books = relationship("Book", secondary=book_genres, back_populates="genres")
