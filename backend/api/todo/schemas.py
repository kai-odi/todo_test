from pydantic import BaseModel

class TodoBase(BaseModel):
    text: str
    done: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoInDB(TodoBase):
    id: int

    class Config:
        from_attributes = True
