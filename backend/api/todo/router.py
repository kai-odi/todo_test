from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from backend.api.todo import schemas
from backend.api.todo.controller import TodoController
from backend.database import get_db

todo_router = APIRouter(prefix="/todos")


@todo_router.post("/", response_model=schemas.TodoInDB, status_code=201)
async def create_todo(todo: schemas.TodoCreate, db: AsyncSession = Depends(get_db)):
    result = await TodoController(db).create(todo)
    return result

@todo_router.get("/", response_model=list[schemas.TodoInDB], status_code=200)
async def read_todos(db: AsyncSession = Depends(get_db)):
    result = await TodoController(db).get()
    return result

@todo_router.patch("/{todo_id}", response_model=schemas.TodoInDB)
async def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: AsyncSession = Depends(get_db)):
    result = await TodoController(db).update(todo_id, todo)
    return result


@todo_router.delete("/{todo_id}", status_code=202)
async def delete_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    await TodoController(db).delete(todo_id)
