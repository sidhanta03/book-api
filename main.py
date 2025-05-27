from fastapi import FastAPI
from routes import user, book

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "Book API is running 🚀"}

app.include_router(user.router)
app.include_router(book.router)






