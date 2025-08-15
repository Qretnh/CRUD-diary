from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NoteBase(BaseModel):
    """Базовый контент заметки"""

    title: str = Field(..., examples=["Моя заметка"])
    content: Optional[str] = Field(None, examples=["Содержимое заметки"])


class NoteCreate(NoteBase):
    """Схема для создания заметки"""

    pass


class NoteUpdate(BaseModel):
    """Схема для частичного обновления заметки"""

    title: Optional[str] = Field(None, examples=["Обновлённое название"])
    content: Optional[str] = Field(None, examples=["Обновлённое содержание"])
    is_done: Optional[bool] = Field(None, examples=[True])


class NoteRead(NoteBase):
    id: int
    is_done: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class DeleteResponse(BaseModel):
    status: str
    detail: str
