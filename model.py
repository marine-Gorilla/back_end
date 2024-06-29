from pydantic import BaseModel

class MemberInfo(BaseModel):
    name: str
    berth : int
    address : str
    email: str
    message: str
