from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from db import get_connection
from auth_dependancy import get_current_user

router = APIRouter()

class Book(BaseModel):
    title: str
    author: str
    published_date: str
    pages: int

@router.get("/books", dependencies=[Depends(get_current_user)])
def get_books():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, author, published_date, pages FROM books")
    books = cur.fetchall()
    cur.close()
    conn.close()
    return books

@router.get("/books/{book_id}", dependencies=[Depends(get_current_user)])
def get_book(book_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE id=%s", (book_id,))
    book = cur.fetchone()
    cur.close()
    conn.close()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/books", dependencies=[Depends(get_current_user)])
def create_book(book: Book):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books (title, author, published_date, pages) VALUES (%s, %s, %s, %s) RETURNING id",
        (book.title, book.author, book.published_date, book.pages)
    )
    row = cur.fetchone()         
    book_id = row["id"]   
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Book created", "book_id": book_id}


@router.put("/books/{book_id}", dependencies=[Depends(get_current_user)])
def update_book(book_id: int, book: Book):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM books WHERE id=%s", (book_id,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")

    cur.execute(
        "UPDATE books SET title=%s, author=%s, published_date=%s, pages=%s WHERE id=%s",
        (book.title, book.author, book.published_date, book.pages, book_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Book updated"}

@router.delete("/books/{book_id}", dependencies=[Depends(get_current_user)])
def delete_book(book_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM books WHERE id=%s", (book_id,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")

    cur.execute("DELETE FROM books WHERE id=%s", (book_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Book deleted"}



