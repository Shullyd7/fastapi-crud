from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, constr, Field
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create FastAPI instance
app = FastAPI()

# SQLAlchemy database setup
DATABASE_URL = "mysql://username:password@localhost/db_name"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()




# Database model
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer)
    isbn = Column(String, index=True)

# Create tables
Base.metadata.create_all(bind=engine)

class BookCreate(BaseModel):
    title: constr(min_length=1) = Field(..., title="Title of the book")
    author: constr(min_length=1) = Field(..., title="Author of the book")
    year: int = Field(..., title="Year of publication")
    isbn: constr(min_length=1) = Field(..., title="ISBN of the book")


class BookUpdate(BaseModel):
    title: str = None
    author: str = None
    year: int = None
    isbn: str = None

class BookOut(BaseModel):
    id: int
    title: str
    author: str
    year: int
    isbn: str

# CRUD operations
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books", response_model=list[BookOut])
def get_books(db = Depends(get_db)):
    return db.query(Book).all()

@app.get("/books/{book_id}", response_model=BookOut)
def get_book(book_id: int, db = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=BookOut)
def create_book(book: BookCreate, db = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: BookUpdate, db = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    for attr, value in book.dict().items():
        if value is not None:
            setattr(db_book, attr, value)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}