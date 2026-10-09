from fastapi import Form,FastAPI,File, UploadFile
from typing import List
app=FastAPI()

@app.post("/upload-bytes")
def upload_bytes(file:bytes=File(...)):
    return {"file_size":len(file)}

@app.post("/upload-file")
def upload_file(file:UploadFile):
    return {"filename":file.filename,"file_content_type":file.content_type}

@app.post("/upload-multiple")
def upload_multi(files:List[UploadFile]):
    return {"files_name":[f.filename for f in files]}