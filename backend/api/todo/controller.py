from fastapi import HTTPException
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.api.todo import models, schemas


class TodoController:
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def delete(self, todo_id: int):
        db_todo = await self.__db.get(models.Todo, todo_id)
        if not db_todo:
            raise HTTPException(404, "Todo not found")
        await self.__db.delete(db_todo)
        await self.__db.commit()

    async def update(self, todo_id: int, todo):
        db_todo = await self.__db.get(models.Todo, todo_id)
        if not db_todo:
            raise HTTPException(404, "Todo not found")
        if todo.text is not None:
            db_todo.text = todo.text
        if todo.done is not None:
            db_todo.done = todo.done

        await self.__db.commit()
        await self.__db.refresh(db_todo)
        return db_todo

    async def get(self):
        result = await self.__db.execute(
            select(models.Todo).order_by(desc(models.Todo.id))
        )
        return result.scalars().all()

    async def create(self, todo: schemas.TodoCreate):
        db_todo = models.Todo(**todo.dict())
        self.__db.add(db_todo)
        await self.__db.commit()
        await self.__db.refresh(db_todo)
        return db_todo
