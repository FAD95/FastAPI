# Python 
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, Body

app = FastAPI()

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    address: Optional[str] = None
    phone: Optional[str] = None
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person.dict()