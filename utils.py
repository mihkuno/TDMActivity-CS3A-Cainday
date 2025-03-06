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
