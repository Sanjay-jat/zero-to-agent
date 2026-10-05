from fastapi import FastAPI
from fastapi import Path,Query

app=FastAPI()

@app.get('/items/{item_id}')
def get_items(item_id:int=Path(ge=0,le=1000)):
    return {"item_id":item_id}

@app.get("/items")
def items(q:str|None=Query(None,min_length=5,max_length=50,title="query")):
    return {"q":q}