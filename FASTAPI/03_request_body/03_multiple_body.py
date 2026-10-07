from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Body

app=FastAPI()

class Item(BaseModel):
    name:str
    price:float
    description:str|None=None
    in_stock:bool=True

class User(BaseModel):
    username:str
    email:str

@app.post("/orders")
def order(items:Item,user:User,importance:int=Body(...)):
    return {**items.dict(), **user.dict(),"importance":importance}