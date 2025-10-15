
# ejecutar (.venv) PS C:\Users\carolina.carrera\Desktop\Tema1Python\ejemplo> fastapi dev main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}


