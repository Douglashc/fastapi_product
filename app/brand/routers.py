
from fastapi import APIRouter, status

from app.db import SessionDep
from app.brand.models import Brand
from app.brand.schemas import BrandUpdate, BrandCreate
from app.brand.service import BrandService

router = APIRouter()
service = BrandService()


# CREATE BRAND
# ----------------------
@router.post("/", response_model=Brand, status_code=status.HTTP_201_CREATED)
async def create_product_brand(
    product_brand_data: BrandCreate,
    session: SessionDep
    ):
    return service.create_brand(product_brand_data, session)

# GET ONE BRAND SELECTED
# ----------------------
@router.get("/{product_brand_id}", response_model=Brand)
async def get_product_brand(
    product_brand_id: int,
    session: SessionDep
):
    return service.get_brand(product_brand_id,session)

# UPDATE BRAND SELECTED
# ----------------------
@router.patch("/{product_brand_id}", response_model=Brand, status_code=status.HTTP_201_CREATED)
async def update_product_brand(
    product_brand_id: int,
    product_brand_data: BrandUpdate,
    session: SessionDep
):
    
    return service.update_brand(product_brand_id, product_brand_data, session)

# GET ALL BRANDS
# ----------------------
@router.get("/", response_model=list[Brand])
async def get_product_brands(
    session: SessionDep
):
    return service.get_brands(session)

# DELETE BRAND SELECTED
# ----------------------
@router.delete("/{product_brand_id}")
async def delete_product_brand(
    product_brand_id: int,
    session: SessionDep,
):
    return service.delete_brand(product_brand_id, session)