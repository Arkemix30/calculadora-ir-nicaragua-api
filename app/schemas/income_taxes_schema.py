
from typing import Optional

from pydantic import BaseModel


class Salary(BaseModel):
    gross_monthly_salary: Optional[float] = 0
    gross_annual_salary: Optional[float] = 0
    monthly_salary_with_inss: Optional[float] = 0
    annual_salary_with_inss: Optional[float] = 0
    net_monthly_salary: Optional[float] = 0
    net_annual_salary: Optional[float] = 0


class Deductions(BaseModel):
    monthly_inss_deduction: Optional[float] = 0
    annual_inss_deduction: Optional[float] = 0
    monthly_income_taxes_deduction: Optional[float] = 0
    annual_income_taxes_deduction: Optional[float] = 0


class IncomeTaxesResponse(BaseModel):
    salary: Salary
    deductions: Deductions


class IncomeTaxesBody(BaseModel):
    gross_monthly_salary: float
