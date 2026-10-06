from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name:str
    price:float
    description:str|None=None
    in_stock:bool=True

@app.post("/items")
def add_items(items:Item):

    return {**items.dict(), "received": True}

@app.put("/items/{item_id}")
def update_item(item_id:int,items:Item):
    return {"item_id": item_id, "items": items}