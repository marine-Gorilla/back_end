from fastapi import FastAPI
from insure.database import get_db

app = FastAPI()


@app.post("/client/{name}/{berthday}/{ph_num}/{contents}")
def client_create(name:str,berthday:int,ph_num:int,contents:int):
    client_information = [name,berthday,ph_num,contents]
    return get_db(client_information)

@app.get("/client/{client_num}")
def client_info(client_num:int):
    return client_num