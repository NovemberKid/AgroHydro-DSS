from fastapi import APIRouter, HTTPException
from app.services.field_service import (
    get_all_fields,
    get_field_by_id
)


router = APIRouter(
    prefix="/fields",
    tags=["Fields"]
)


@router.get("/")
def list_fields():
    return get_all_fields()


@router.get("/{field_id}")
def get_field(field_id: str):
    field = get_field_by_id(field_id)

    if field is None:
        raise HTTPException(
            status_code=404,
            detail="Field not found"
        )

    return field