from fastapi import APIRouter

from app.api.endpoints import income_taxes_calculator 

api_router = APIRouter()
api_router.include_router(income_taxes_calculator.router, tags=["income_taxes_calculator"])