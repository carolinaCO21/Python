from routers import user
from routers import tienda, empleado, auth_users
from fastapi import FastAPI, HTTPException

from fastapi.staticfiles import StaticFiles

app= FastAPI()

# Routers
app.include_router(tienda.router)
app.include_router(empleado.router)
app.include_router(user.router)
app.include_router(auth_users.router)
#app.mount("/static", StaticFiles(directory="static"), name="static")


# http://127.0.0.1:8000/static/imagenes/solid.png
@app.get("/")
def root():
    return {"Hello": "World"}