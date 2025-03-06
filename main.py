from utils import *

def main():
    salary = float(input("Enter your monthly salary: "))
    
    sss = compute_sss()
    philhealth = compute_philhealth(salary)
    pagibig = compute_pagibig()
    tax = compute_tax()

    deductions = sss + philhealth + pagibig + tax
    net_salary = salary - deductions

    print("Gross Salary:", salary)
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)


if __name__ == "__main__":
    main()



