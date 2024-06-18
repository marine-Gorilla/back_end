from pydantic import BaseModel

class Client(BaseModel):
    name :str
    phone_number : int
    berth : int
    address : int
    sex : int
