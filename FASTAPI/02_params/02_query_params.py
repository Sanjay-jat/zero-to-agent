from fastapi import FastAPI

app=FastAPI()

@app.get("/products")
def products(skip:int=0,limit:int=10):
    return {"skip": skip, "limit": limit}

@app.get("/search")
def search(q:str|None=None):
    if(q):
        return {"q":q}
    else:
        return {"message": "no query given"}

@app.get("/products/{product_id}")
def product_by_id(product_id:int,short:bool= False):
    if(short):
        return {"id": product_id}
    else:
        return {"id": product_id, "detail": "full description"}