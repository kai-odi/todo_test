from sqlalchemy import Column, Integer, String, Boolean

from backend.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    done = Column(Boolean, default=False)
