from fastapi import FastAPI

app=FastAPI()

@app.get("/items")
def get_items():
    return {"items": ["a","b","c"]}

@app.post("/items")
def create_items():
    return {"message":"item created"}

@app.put("/items")
def update_items():
    return {"message":"updated"}

@app.delete("/items")
def delete_items():
    return {"message":"item deleted"}