from fastapi import APIRouter

from backend.api.todo.router import todo_router

routers = APIRouter()

routers.include_router(todo_router)
