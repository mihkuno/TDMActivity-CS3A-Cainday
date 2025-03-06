# Importing the utils module, which contains functions for computing deductions
import utils  

def main():
    try:
        # Prompt the user to enter their monthly salary
        salary = input("Enter your monthly salary: ")
        salary = float(salary)  # Convert the input to a floating-point number

        # Validate that the entered salary is not negative
        if salary < 0:
            raise ValueError("Salary cannot be negative.")  # Raise an error for negative salary
    
    except ValueError as e:
        # Handle invalid salary input (e.g., non-numeric or negative values)
        print(f"Error: {e}. Please enter a valid positive number for the salary.")
        return  # Exit the function if salary input is invalid

    try:
        # Compute various salary deductions using functions from the utils module

        # Compute SSS (Social Security System) contribution
        sss = utils.compute_sss()

        # Compute PhilHealth (health insurance) contribution based on the salary
        philhealth = utils.compute_philhealth(salary)

        # Compute Pag-IBIG (Home Development Mutual Fund) contribution
        pagibig = utils.compute_pagibig()

        # Compute tax deductions based on applicable tax rates
        tax = utils.compute_tax()

        # Ensure all deduction values are valid (i.e., not None or unexpected values)
        if any(v is None for v in [sss, philhealth, pagibig, tax]):
            raise ValueError("One of the deduction calculations returned an invalid value.")
    
    except Exception as e:
        # Handle any errors that may occur during deduction calculations
        print(f"Error during deduction calculation: {e}")
        return  # Exit the function if an error occurs in deduction computations

    try:
        # Calculate the total amount of deductions from the salary
        deductions = sss + philhealth + pagibig + tax
        
        # Compute the net salary after all deductions have been applied
        net_salary = salary - deductions
        
        # Check if the deductions exceed the gross salary, which shouldn't happen
        if net_salary < 0:
            raise ValueError("Total deductions exceed the salary. Please check the deduction rates.")
    
    except ValueError as e:
        # Handle cases where the net salary calculation results in an error
        print(f"Error: {e}")
        return  # Exit the function if there is an issue in calculations

    # Display the salary breakdown to the user if all calculations were successful
    print("\nSalary Breakdown:")
    print("-----------------------------")
    print("Gross Salary:      ", salary)
    print("SSS Deduction:     ", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:     ", tax)
    print("-----------------------------")
    print("Total Deductions:  ", deductions)
    print("Net Salary:        ", net_salary)
    print("-----------------------------")

# Ensure the script runs only when executed directly, not when imported as a module
if __name__ == "__main__":
    main()
