from utils import *

def main():
    try:
        # Get the monthly salary, and handle the case for invalid input.
        salary = input("Enter your monthly salary: ")
        salary = float(salary)  # Attempt to convert input to float.
        
        # Check if salary is negative
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid positive number for the salary.")
        return  # Exit if salary input is invalid
    
    try:
        # Calculate deductions
        sss = compute_sss()
        philhealth = compute_philhealth(salary)
        pagibig = compute_pagibig()
        tax = compute_tax()
        
        # Ensure the returned values are valid numbers (just in case the computation functions return None)
        if any(v is None for v in [sss, philhealth, pagibig, tax]):
            raise ValueError("One of the deduction calculations returned an invalid value.")
        
    except Exception as e:
        print(f"Error during deduction calculation: {e}")
        return  # Exit if an error occurs in computation functions

    try:
        # Calculate deductions and net salary
        deductions = sss + philhealth + pagibig + tax
        net_salary = salary - deductions
        
        # Handle edge case of negative net salary (if deductions somehow exceed salary)
        if net_salary < 0:
            raise ValueError("Total deductions exceed the salary. Please check the deduction rates.")
        
    except ValueError as e:
        print(f"Error: {e}")
        return  # Exit if any calculation goes wrong

    # Display the results if everything went fine
    print("Gross Salary:", salary)
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)


if __name__ == "__main__":
    main()



