
from sqlmodel import Field, Relationship, Session, SQLModel, select
from typing import Optional

class ProductBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    status: bool = True

# Modelo para crear un nuevo producto (hereda de TaskBase)
class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass
