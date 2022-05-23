from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from app.schemas import IncomeTaxesResponse, IncomeTaxesBody
from app.utils import calculate

router = APIRouter()


@router.post("/calculate_income_taxes", response_model=IncomeTaxesResponse)
def calculate_income_taxes(body: IncomeTaxesBody) -> Any:
    if not body.gross_monthly_salary:
        raise HTTPException(status_code=400, detail="gross_monthly_salary not specified")
    try:
        resp = calculate(salary=body.gross_monthly_salary)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error when calculating income tax")
    return resp
