from fastapi import HTTPException, status
from sqlmodel import select

from app.db import SessionDep
from app.category.models import Category
from app.category.schemas import CategoryCreate, CategoryUpdate


class CategoryService:
    no_category:str = "Category doesn't exits"
    # CREATE CATEGORY
    # ----------------------
    def create_category(self, item_data: CategoryCreate, session: SessionDep):
        category_db = Category.model_validate(item_data.model_dump())
        session.add(category_db)
        session.commit()
        session.refresh(category_db)
        return category_db

    # GET ONE CATEGORY
    # ----------------------
    def get_category(self, item_id: int, session: SessionDep):
        category_db = session.get(Category, item_id)
        if not category_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_category
            )
        return category_db

    # UPDATE CATEGORY SELECTED
    # ----------------------
    def update_category(self, item_id: int, item_data: CategoryUpdate, session: SessionDep):
        category_db = session.get(Category, item_id)
        if not category_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_category
            )
        item_data_dict = item_data.model_dump(exclude_unset=True)
        category_db.sqlmodel_update(item_data_dict)
        session.add(category_db)
        session.commit()
        session.refresh(category_db)
        return category_db

    # GET ALL CATEGORIES
    # ----------------------
    def get_categories(self, session: SessionDep):
        return session.exec(select(Category)).all()

    # DELETE CATEGORY SELECTED
    # ----------------------
    def delete_category(self, item_id: int, session: SessionDep):
        category_db = session.get(Category, item_id)
        if not category_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_category
            )
        session.delete(category_db)
        session.commit()
        
        return {"detail": "ok"}