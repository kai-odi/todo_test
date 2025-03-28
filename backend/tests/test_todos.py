from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/tests/.env.test")

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from backend.main import app
from backend.database import get_db
from backend.api.todo import models
from httpx import AsyncClient

DATABASE_URL = "sqlite+aiosqlite:///:memory:"
Base = models.Base

engine_test = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = async_sessionmaker(engine_test, expire_on_commit=False)

@pytest.fixture(scope="session")
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture()
async def db_session(prepare_database):
    async with TestingSessionLocal() as session:
        yield session

@pytest_asyncio.fixture()
async def client(db_session: AsyncSession):
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(base_url="http://0.0.0.0:8000") as ac:
        yield ac

    app.dependency_overrides.clear()

@pytest.mark.asyncio
async def test_create_todo(client: AsyncClient):
    response = await client.post("/todos/", json={"text": "Test todo"})
    assert response.status_code == 201
    data = response.json()
    assert data["text"] == "Test todo"
    assert data["done"] is False

@pytest.mark.asyncio
async def test_read_todos(client: AsyncClient):
    await client.post("/todos/", json={"text": "Read test"})
    response = await client.get("/todos/")
    assert response.status_code == 200
    todos = response.json()
    assert any(todo["text"] == "Read test" for todo in todos)

@pytest.mark.asyncio
async def test_update_todo(client: AsyncClient):
    response = await client.post("/todos/", json={"text": "To be updated"})
    todo_id = response.json()["id"]
    patch = await client.patch(f"/todos/{todo_id}", json={"done": True})
    assert patch.status_code == 202
    assert patch.json()["done"] is True

@pytest.mark.asyncio
async def test_delete_todo(client: AsyncClient):
    response = await client.post("/todos/", json={"text": "To be deleted"})
    todo_id = response.json()["id"]
    delete = await client.delete(f"/todos/{todo_id}")
    assert delete.status_code == 202
    get = await client.get("/todos/")
    assert all(todo["id"] != todo_id for todo in get.json())
