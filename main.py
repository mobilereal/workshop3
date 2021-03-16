from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return JSONResponse(content={"message": "Hello,  World"}, status_code=200)


@app.get("/profile/{name}")
def get_path_parameter(name: str):
    print(name)
    return JSONResponse(
        content={"message": f"My name is : {name}"},
        status_code=200,
    )


@app.get("/profile")
def get_query_parameter(start: int = 0, limit: int = 0):
    return JSONResponse(
        content={"message": f"profile start : {start} limit:{limit}"},
        status_code=200,
    )


@app.get("/books")
def get_books():
    dict_books = [
        {
            "book_id": 1,
            "book_name": "harry potter and philosopher's stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "harry potter and the chamber of secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "harry potter and prisoner ofazkaban",
            "page": 251,
        },
    ]


@app.get("/books{book_id}")
def get_books_by_id(book_id: int):
    dict_books = [
        {
            "book_id": 1,
            "book_name": "harry potter and philosopher's stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "harry potter and the chamber of secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "harry potter and prisoner ofazkaban",
            "page": 251,
        },
    ]
    
    book_filter = list(filter(lambda book : book ["book_id"] = book_id,dict_books))
    result = book_filter[0] if len(book_filter) > 0 else []
    return JSONResponse(content={"status": "ok", "data": dict_books}, status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3001, reload=True)