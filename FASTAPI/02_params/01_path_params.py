from fastapi import FastAPI

app=FastAPI()

@app.get("/items/{items_id}")
def get_item_by_id(items_id:int):
    return {"item_id":items_id}

@app.get("/user/me")
def get_user():
    return {"user": "current user"}