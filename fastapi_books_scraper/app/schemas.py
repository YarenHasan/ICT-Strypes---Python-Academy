from datetime import datetime
from pydantic import BaseModel, AnyHttpUrl
from typing import Optional
from uuid import UUID


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    url: AnyHttpUrl


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
