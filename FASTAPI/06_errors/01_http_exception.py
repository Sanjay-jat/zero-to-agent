from fastapi import FastAPI
from fastapi import HTTPException

app=FastAPI()

items_db = {1: "Laptop", 2: "Mouse", 3: "Keyboard"}

@app.get("/items/{item_id}")
def get_items(item_id:int):
    if item_id in items_db:
        return {"item_id": item_id, "name": items_db[item_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found", headers={"X-Error": "Item-Not-Found"})

@app.get("/items/{item_id}/discount")
def discount(percent: int,item_id:int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    if percent<0 or percent>100:
        raise HTTPException(status_code=400,detail="Invalid discount percent")
    return {"item_id": item_id, "discount": percent}