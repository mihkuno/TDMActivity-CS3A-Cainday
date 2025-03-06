# Function to compute SSS (Social Security System) contribution
def compute_sss():
    return 1200  # Fixed amount for SSS contribution

# Function to compute PhilHealth (health insurance) contribution
# PhilHealth contribution is calculated as 5% of the salary, divided by 2 (employer-employee share)
def compute_philhealth(salary):
    return (salary * 0.05) / 2  

# Function to compute Pag-IBIG (Home Development Mutual Fund) contribution
# Pag-IBIG has a fixed contribution amount
def compute_pagibig():
    return 100  # Fixed amount for Pag-IBIG contribution

# Function to compute tax deductions
# This function returns a fixed tax amount for now
def compute_tax():
    return 1875  # Fixed tax deduction

# Function to compute total deductions and return individual deductions
def compute_total_deductions(salary):
    sss = compute_sss()
    philhealth = compute_philhealth(salary)
    pagibig = compute_pagibig()
    tax = compute_tax()
    
    total_deductions = sss + philhealth + pagibig + tax
    return total_deductions, sss, philhealth, pagibig, tax

# Function to compute net salary
def compute_net_salary(salary, deductions):
    return salary - deductions
