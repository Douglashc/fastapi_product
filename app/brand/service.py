from fastapi import HTTPException, status
from sqlmodel import select

from app.db import SessionDep
from app.brand.models import Brand
from app.brand.schemas import BrandCreate, BrandUpdate


class BrandService:
    no_brand: str = "Brand doesn't exits"

    # CREATE 
    # ----------------------
    def create_brand(self, item_data: BrandCreate, session: SessionDep):
        item_db = Brand.model_validate(item_data.model_dump())
        session.add(item_db)
        session.commit()
        session.refresh(item_db)
        return item_db

    # GET ONE
    # ----------------------
    def get_brand(self, item_id: int, session: SessionDep):
        item_db = session.get(Brand, item_id)
        if not item_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_brand
            )
        return item_db

    # UPDATE
    # ----------------------
    def update_brand(self, item_id: int, item_data: BrandUpdate, session: SessionDep):
        item_db = session.get(Brand, item_id)
        if not item_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_brand
            )
        item_data_dict = item_data.model_dump(exclude_unset=True)
        item_db.sqlmodel_update(item_data_dict)
        session.add(item_db)
        session.commit()
        session.refresh(item_db)
        return item_db

    # GET ALL 
    # ----------------------
    def get_brands(self, session: SessionDep):
        return session.exec(select(Brand)).all()

    # DELETE
    # ----------------------
    def delete_brand(self, item_id: int, session: SessionDep):
        item_db = session.get(Brand, item_id)
        if not item_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        #print(f"Producto {item_db}")
        session.delete(item_db)
        session.commit()
        return {"detail": "ok"}