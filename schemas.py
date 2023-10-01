from pydantic import BaseModel

class ToDoRequest(BaseModel):
    title: str
    completed: bool
    priority: int

class ToDoResponse(BaseModel):
    title: str
    completed: bool
    priority: int
    id: int

    class Config:
        orm_mode = True