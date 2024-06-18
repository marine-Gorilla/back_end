from fastapi import FastAPI
from model import Client

app = FastAPI()

@app.post("/client/send")
def client_create(client : Client):
    return client
