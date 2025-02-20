
from sqlmodel import Field, SQLModel
from typing import Optional

class ProductBase(SQLModel):
    title: str = Field(default=None)
    price: int = 0
    description: Optional[str] = None
    image: Optional[str] = None

# Modelo para crear un nuevo producto (hereda de TaskBase)
class ProductCreate(ProductBase):
    category_id: Optional[int] = None

class ProductUpdate(ProductBase):
    title: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None
    image: Optional[str] = None
    category_id: Optional[int] = None 
