# Proyecto 3 — API con Python - FastAPI

# Instalar servidor local y fastApi desde cmd
# python -m pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

datas = [
    {
    "nombre": "Luis",
    "edad": 10
    }
]

class Data(BaseModel):
    nombre: str
    edad: int

app = FastAPI()

@app.get("/")
def diccionario():
    return datas
    
@app.get("/saludar/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola {nombre}"}

@app.post("/post")
def postData(data: Data):
    datas.append(data)
    return {
        "mensaje": "Dato agregado",
        "data": data
    }



# Ejecutar en el servidor 
# py -m unicorn Api:app --reload, 
# ahora ingresa a http://127.0.0.1:8000 desde el navegador