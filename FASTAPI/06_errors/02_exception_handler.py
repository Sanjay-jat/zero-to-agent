from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse

app=FastAPI()
items_db = {1: "Laptop", 2: "Mouse", 3: "Keyboard"}

class ItemNotFound(Exception):
    def __init__(self,item_id:int):
        self.item_id=item_id

@app.exception_handler(ItemNotFound)
async def handler(request:Request,exc:ItemNotFound):
    return JSONResponse(status_code=404,content={"error": f"Item {exc.item_id} not found in system"})

@app.get("/products/{product_id}")
def get_products(product_id:int):
    if product_id not in items_db:
        raise ItemNotFound(product_id)
    return {"item_id": product_id, "name": items_db[product_id]}