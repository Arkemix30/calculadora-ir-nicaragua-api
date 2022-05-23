
from app.schemas import IncomeTaxesResponse, Salary, Deductions
def calculate(salary: str)-> IncomeTaxesResponse:
    salary = float(salary)
    monthly_inss_deduction = float(salary * 0.07)
    net_salary_without_deduction = float(salary - monthly_inss_deduction)
    anual_net_salary = float(net_salary_without_deduction * 12)

    print(anual_net_salary)
    if anual_net_salary >= 1 and anual_net_salary <= 100000:
        resp_salary = {
            "gross_monthly_salary" : salary,
            "gross_annual_salary" : (salary*12),
            "monthly_salary_with_inss" : net_salary_without_deduction,
            "annual_salary_with_inss" : anual_net_salary,
            "net_monthly_salary" : net_salary_without_deduction,
            "net_annual_salary" : anual_net_salary,

        }
        resp_deduction = {
            "monthly_inss_deduction" : monthly_inss_deduction,
            "annual_inss_deduction" : monthly_inss_deduction*12,
            "monthly_income_taxes_deduction" : 0,
        }
    elif anual_net_salary > 100000 and anual_net_salary <= 200000:
        base_income_taxes = 0
        excess = 100000 
        annual_salary_without_excess = anual_net_salary - excess
        annual_income_taxes_deduction = annual_salary_without_excess * 0.15
        annual_income_taxes_deduction = annual_income_taxes_deduction + base_income_taxes
        monthly_income_taxes_deduction = annual_income_taxes_deduction/12
        net_monthly_salary = (net_salary_without_deduction - monthly_income_taxes_deduction)

        resp_salary = {
            "gross_monthly_salary" : salary,
            "gross_annual_salary" : (salary*12),
            "monthly_salary_with_inss" : net_salary_without_deduction,
            "annual_salary_with_inss" : anual_net_salary,
            "net_monthly_salary" : net_monthly_salary ,
            "net_annual_salary" : net_monthly_salary*12,

        }
        resp_deduction = {
            "monthly_inss_deduction" : monthly_inss_deduction,
            "annual_inss_deduction" : monthly_inss_deduction*12,
            "monthly_income_taxes_deduction" : monthly_income_taxes_deduction,
            "annual_income_taxes_deduction" : annual_income_taxes_deduction,
        }
    elif anual_net_salary > 200000 and anual_net_salary <= 350000:
        base_income_taxes = 15000
        excess = 200000 
        annual_salary_without_excess = anual_net_salary - excess
        annual_income_taxes_deduction = annual_salary_without_excess * 0.20
        annual_income_taxes_deduction = annual_income_taxes_deduction + base_income_taxes
        monthly_income_taxes_deduction = annual_income_taxes_deduction/12
        net_monthly_salary = (net_salary_without_deduction - monthly_income_taxes_deduction)

        resp_salary = {
            "gross_monthly_salary" : salary,
            "gross_annual_salary" : (salary*12),
            "monthly_salary_with_inss" : net_salary_without_deduction,
            "annual_salary_with_inss" : anual_net_salary,
            "net_monthly_salary" : net_monthly_salary ,
            "net_annual_salary" : net_monthly_salary*12,

        }
        resp_deduction = {
            "monthly_inss_deduction" : monthly_inss_deduction,
            "annual_inss_deduction" : monthly_inss_deduction*12,
            "monthly_income_taxes_deduction" : monthly_income_taxes_deduction,
            "annual_income_taxes_deduction" : annual_income_taxes_deduction,
        }
    elif anual_net_salary > 350000 and anual_net_salary <= 500000:
        base_income_taxes = 45000
        excess = 350000 
        annual_salary_without_excess = anual_net_salary - excess
        annual_income_taxes_deduction = annual_salary_without_excess * 0.25
        annual_income_taxes_deduction = annual_income_taxes_deduction + base_income_taxes
        monthly_income_taxes_deduction = annual_income_taxes_deduction/12
        net_monthly_salary = (net_salary_without_deduction - monthly_income_taxes_deduction)

        resp_salary = {
            "gross_monthly_salary" : salary,
            "gross_annual_salary" : (salary*12),
            "monthly_salary_with_inss" : net_salary_without_deduction,
            "annual_salary_with_inss" : anual_net_salary,
            "net_monthly_salary" : net_monthly_salary ,
            "net_annual_salary" : net_monthly_salary*12,

        }
        resp_deduction = {
            "monthly_inss_deduction" : monthly_inss_deduction,
            "annual_inss_deduction" : monthly_inss_deduction*12,
            "monthly_income_taxes_deduction" : monthly_income_taxes_deduction,
            "annual_income_taxes_deduction" : annual_income_taxes_deduction,
        }
    elif anual_net_salary > 500000:
        base_income_taxes = 82500
        excess = 500000 
        annual_salary_without_excess = anual_net_salary - excess
        annual_income_taxes_deduction = annual_salary_without_excess * 0.30
        annual_income_taxes_deduction = annual_income_taxes_deduction + base_income_taxes
        monthly_income_taxes_deduction = annual_income_taxes_deduction/12
        net_monthly_salary = (net_salary_without_deduction - monthly_income_taxes_deduction)

        resp_salary = {
            "gross_monthly_salary" : salary,
            "gross_annual_salary" : (salary*12),
            "monthly_salary_with_inss" : net_salary_without_deduction,
            "annual_salary_with_inss" : anual_net_salary,
            "net_monthly_salary" : net_monthly_salary ,
            "net_annual_salary" : net_monthly_salary*12,

        }
        resp_deduction = {
            "monthly_inss_deduction" : monthly_inss_deduction,
            "annual_inss_deduction" : monthly_inss_deduction*12,
            "monthly_income_taxes_deduction" : monthly_income_taxes_deduction,
            "annual_income_taxes_deduction" : annual_income_taxes_deduction,
        }
    
    resp = IncomeTaxesResponse(
            salary = Salary(**resp_salary),
            deductions = Deductions(**resp_deduction)
        )
    return resp