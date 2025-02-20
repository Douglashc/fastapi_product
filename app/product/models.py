
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel, Relationship

if TYPE_CHECKING:
    from app.category.models import Category
class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(default=None)
    price: int = 0
    description: str | None = Field(default=None)
    category: str | None = Field(default=None)
    image: str = Field(default=None)

    category_id: Optional[int] = Field(default=None, foreign_key="product_category.id")
    category: Optional["Category"] = Relationship(back_populates="products")

    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=True
        ),
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=func.now(), nullable=True),
    )