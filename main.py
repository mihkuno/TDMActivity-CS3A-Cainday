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
        # Compute total deductions and breakdown
        total_deductions, sss, philhealth, pagibig, tax = utils.compute_total_deductions(salary)
        
        # Compute net salary
        net_salary = utils.compute_net_salary(salary, total_deductions)
        
        # Check if deductions exceed salary
        if net_salary < 0:
            raise ValueError("Total deductions exceed the salary. Please check the deduction rates.")

    except Exception as e:
        print(f"Error during deduction calculation: {e}")
        return  # Exit the function if an error occurs in deduction computations

    # Display the salary breakdown to the user
    print("\nSalary Breakdown:")
    print("-----------------------------")
    print("Gross Salary:      ", salary)
    print("SSS Deduction:     ", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:     ", tax)
    print("-----------------------------")
    print("Total Deductions:  ", total_deductions)
    print("Net Salary:        ", net_salary)
    print("-----------------------------")

# Ensure the script runs only when executed directly, not when imported as a module
if __name__ == "__main__":
    main()
