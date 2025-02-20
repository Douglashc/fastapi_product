
from fastapi import APIRouter, status

from app.db import SessionDep
from app.category.models import Category
from app.category.schemas import CategoryCreate, CategoryUpdate
from app.category.service import CategoryService

router = APIRouter()
service = CategoryService()


# CREATE CATEGORY
# ----------------------
@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
async def create_product_category(
    category_data: CategoryCreate,
    session: SessionDep
    ):
    return service.create_category(category_data, session)

# GET ONE CATEGORY SELECTED
# ----------------------
@router.get("/{product_category_id}", response_model=Category)
async def get_product_category(
    product_category_id: int,
    session: SessionDep
):
    return service.get_category(product_category_id,session)

# UPDATE CATEGORY SELECTED
# ----------------------
@router.patch("/{product_category_id}", response_model=Category, status_code=status.HTTP_201_CREATED)
async def update_product_category(
    product_category_id: int,
    product_category_data: CategoryUpdate,
    session: SessionDep
):
    
    return service.update_category(product_category_id, product_category_data, session)

# GET ALL CATEGORIES
# ----------------------
@router.get("/", response_model=list[Category])
async def get_categories(
    session: SessionDep
):
    return service.get_categories(session)

# DELETE CATEGORY SELECTED
# ----------------------
@router.delete("/{product_category_id}")
async def delete_category(
    product_category_id: int,
    session: SessionDep,
):
    return service.delete_category(product_category_id, session)