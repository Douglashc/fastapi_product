from fastapi import HTTPException, status
from sqlmodel import select
from sqlalchemy.orm import selectinload, joinedload
from app.db import SessionDep
from app.product.models import Product
from app.product.schemas import ProductCreate, ProductUpdate


class ProductService:
    no_product:str = "Product doesn't exits"

    # CREATE PRODUCT
    # ----------------------
    def create_product(self, plan_data: ProductCreate, session: SessionDep):
        product_db = Product.model_validate(plan_data.model_dump())
        session.add(product_db)
        session.commit()
        session.refresh(product_db)
        return product_db

    # GET ONE PRODUCT
    # ----------------------
    def get_product(self, item_id: int, session: SessionDep):
        statement = (
            select(Product)
            .where(Product.id == item_id)
            .options(selectinload(Product.category))
            .options(selectinload(Product.brand))
        )
        
        product_db = session.exec(statement).first()

        if not product_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_product
            )
        return product_db

    # UPDATE PRODUCT SELECTED
    # ----------------------
    def update_product(self, item_id: int, item_data: ProductUpdate, session: SessionDep):
        product_db = session.get(Product, item_id)
        if not product_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_product
            )
        item_data_dict = item_data.model_dump(exclude_unset=True)
        product_db.sqlmodel_update(item_data_dict)
        session.add(product_db)
        session.commit()
        session.refresh(product_db)
        return product_db

    # GET ALL PRODUCTS
    # ----------------------
    def get_products(self, session: SessionDep):
        statement = (
            select(Product)
            .options(selectinload(Product.category))
        )
        return session.exec(statement).all()

    # DELETE PRODUCT SELECTED
    # ----------------------
    def delete_product(self, item_id: int, session: SessionDep):
        product_db = session.get(Product, item_id)
        if not product_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_product
            )
        session.delete(product_db)
        session.commit()

        return {"detail": "ok"}
