from typing import Optional
from sqlmodel import Field, SQLModel

class BrandBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)

class BrandRead(SQLModel):
    id: int
    name: str
    description: Optional[str] = None

class BrandCreate(BrandBase):
    pass

class BrandUpdate(BrandBase):
    pass