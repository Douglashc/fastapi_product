from datetime import datetime
from sqlalchemy import Column, DateTime,func
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from app.product.models import Product

class Brand(SQLModel, table=True):
    __tablename__ = "product_brand"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    description: str | None = Field(default=None)

    products: List["Product"] = Relationship(back_populates="brand")

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