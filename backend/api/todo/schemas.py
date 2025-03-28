from pydantic import BaseModel

class TodoBase(BaseModel):
    text: str
    done: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    text: str | None = None
    done: bool | None = None

class TodoInDB(TodoBase):
    id: int

    class Config:
        from_attributes = True
