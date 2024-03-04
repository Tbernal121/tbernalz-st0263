from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List 
import uuid
import json
import httpx

app = FastAPI()

class idRequest(BaseModel):
    id: str

class PServer(BaseModel):
    ip_address: str
    file_index: List[str]


# Base de datos
pservers = {
  "83db576d-642f-48d2-9e5a-26f93a8602b1": {
    "ip_address": "192.12.32.45", 
    "file_index": [
      "Shakira.mp3", "billieJean.mp3", "gotasDeAguaDulce.mp3"
    ]
  },
  "405a0a35-f7f5-4921-ab88-7f7ddb217a50": {
    "ip_address": "192.12.32.46",
    "file_index": [
      "billieJean.mp3"
    ]
  },
  "1ed4493a-3652-418c-a1bc-45ff10323546": {
    "ip_address": "192.12.32.48",
    "file_index": [
      "Innerbloom.mp3", "Shakira.mp3"
    ]
  }
}

# Ruta para que un PServer haga login
@app.get("/api/v1/login")
async def login(request: Request):
  unique_id = str(uuid.uuid4())
  client_ip = request.client.host
  pservers[unique_id] = {"ip_address": client_ip, "file index":""}
  return {"Message": "PServer registrado exitosamente", "id": unique_id}


# Ruta para que un PServer haga logut
@app.post("/api/v1/logout")
async def logout(request: idRequest):
  if request.id not in pservers:
      raise HTTPException(status_code=400, detail="PServer no encontrado")
  del pservers[request.id]
  return {"Message": "Pserver retirado exitosamente"}


# Ruta para revisar los peers que se encuentran conectados
@app.get("/api/v1/check_peers_status")
async def check_peers_status():
    # Crear una lista para almacenar el estado de cada PServer
    status_list = []
    # Iterar sobre cada PServer en el diccionario pservers
    for id, pserver in pservers.items():
        # Intentar hacer una solicitud HTTP al PServer
        try:
            response = httpx.get(f"http://{pserver['ip_address']}/status", timeout=5)
            # Si el PServer responde, asumir que está en línea
            status = "online" if response.status_code == 200 else "offline"
        except httpx.RequestError:
            # Si hay un error al hacer la solicitud, asumir que el PServer está fuera de línea
            status = "offline"
        status_info = {
            "id": id,
            "ip_address": pserver["ip_address"],
            "status": status,
        }
        # Añadir el estado a la lista
        status_list.append(status_info)
    print(status_list)
    # Devolver la lista de estados
    return status_list


@app.get("/api/v1/{file_name}")
async def get_peers_by_file_name(file_name: str):
    # Crear una lista para almacenar los PServers que tienen el archivo
    peers_with_file = []
    # Iterar sobre cada PServer en el diccionario pservers
    for id, pserver in pservers.items():
        # Si el PServer tiene el archivo, añadirlo a la lista
        if file_name in pserver["file_index"]:
            peers_with_file.append({
                "id": id,
                "ip_address": pserver["ip_address"],
            })
    # Si no se encontró ningún PServer con el archivo, devolver un error
    if not peers_with_file:
        raise HTTPException(status_code=404, detail="Archivo no encontrado en ningún PServer")
    # Devolver la lista de PServers que tienen el archivo
    return peers_with_file


@app.patch("/api/v1/update_list/{id}")
async def update_files_list(id: str, fileList: List[str]):
    if id not in pservers:
        raise HTTPException(status_code=404, detail="PServer no encontrado")
    pservers[id]["file_index"] = fileList
    return {"Updated File List": pservers[id]["file_index"]}

app.post("/api/v1/login")