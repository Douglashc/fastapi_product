from typing import Optional
from sqlmodel import Field, SQLModel

class CategoryBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryRead(SQLModel):
    id: int
    name: str
    description: Optional[str] = None