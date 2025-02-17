from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    email: str
    position: str

class Service(BaseModel):
    name: str
    description: str
