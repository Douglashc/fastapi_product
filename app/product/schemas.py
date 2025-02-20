
from sqlmodel import Field, SQLModel, Session, select
from datetime import datetime
from app.category.schemas import CategoryRead
from app.brand.models import Brand
from app.brand.schemas import BrandRead
from typing import Optional
from pydantic import field_validator
from app.db import engine

class ProductBase(SQLModel):
    title: str = Field(default=None)
    price: int = 0
    description: Optional[str] = None
    image: Optional[str] = None

class ProductRead(ProductBase):
    id: int
    created_at: Optional[datetime]
    category: Optional[CategoryRead] = None
    brand: Optional[BrandRead] = None

# Modelo para crear un nuevo producto (hereda de TaskBase)
class ProductCreate(ProductBase):
    category_id: Optional[int] = None
    brand_id: Optional[int] = None
    @field_validator("brand_id")
    @classmethod
    def validate_brand(cls, value):
        session = Session(engine)
        query = select(Brand).where(Brand.id == value)
        result = session.exec(query).first()
        if not result:
            raise ValueError(f"Brand Id:{value} doesn't exist")
        return value

class ProductUpdate(ProductBase):
    title: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None
    image: Optional[str] = None
    category_id: Optional[int] = None 
    brand_id: Optional[int] = None
