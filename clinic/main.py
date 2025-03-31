from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import time
from enum import Enum

app = FastAPI()

class Timestamp(BaseModel):
    id: int
    timestamp: int


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    kind: DogType
    pk: Optional[int] = None  


dogs_db = []
dog_id_counter = 1


@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}


@app.post("/post", response_model=Timestamp)
def get_post():
    return Timestamp(id=1, timestamp=int(time.time()))


@app.get("/dog", response_model=List[Dog])
def get_dogs(kind: Optional[DogType] = None):
    if kind:
        return [dog for dog in dogs_db if dog.kind == kind]
    return dogs_db


@app.post("/dog", response_model=Dog)
def create_dog(dog: Dog):
    global dog_id_counter
    dog.pk = dog_id_counter
    dog_id_counter += 1
    dogs_db.append(dog)
    return dog


@app.get("/dog/{pk}", response_model=Dog)
def get_dog_by_pk(pk: int):
    for dog in dogs_db:
        if dog.pk == pk:
            return dog
    raise HTTPException(status_code=404, detail="Dog not found")


@app.patch("/dog/{pk}", response_model=Dog)
def update_dog(pk: int, updated_dog: Dog):
    for dog in dogs_db:
        if dog.pk == pk:
            dog.name = updated_dog.name
            dog.kind = updated_dog.kind
            return dog
    raise HTTPException(status_code=404, detail="Dog not found")
