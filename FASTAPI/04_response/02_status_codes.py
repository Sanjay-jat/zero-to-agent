from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item():
    return {"message": "item created"}

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    return

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}