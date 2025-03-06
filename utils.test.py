def run_test_cases():
    print("Running Test Cases...\n")

    # Test Case 1: Low Salary (₱10,000)
    salary = 10000
    print("Test Case 1: Salary = ₱10,000")
    print("SSS Deduction:", utils.compute_sss())  # Expected: 1200
    print("PhilHealth Deduction:", utils.compute_philhealth(salary))  # Expected: 250
    print("Pag-IBIG Deduction:", utils.compute_pagibig())  # Expected: 100
    print("Tax Deduction:", utils.compute_tax())  # Expected: 1875
    print()

    # Test Case 2: Mid-Level Salary (₱30,000)
    salary = 30000
    print("Test Case 2: Salary = ₱30,000")
    print("SSS Deduction:", utils.compute_sss())  # Expected: 1200
    print("PhilHealth Deduction:", utils.compute_philhealth(salary))  # Expected: 750
    print("Pag-IBIG Deduction:", utils.compute_pagibig())  # Expected: 100
    print("Tax Deduction:", utils.compute_tax())  # Expected: 1875
    print()

    # Test Case 3: High Salary (₱80,000)
    salary = 80000
    print("Test Case 3: Salary = ₱80,000")
    print("SSS Deduction:", utils.compute_sss())  # Expected: 1200
    print("PhilHealth Deduction:", utils.compute_philhealth(salary))  # Expected: 2000
    print("Pag-IBIG Deduction:", utils.compute_pagibig())  # Expected: 100
    print("Tax Deduction:", utils.compute_tax())  # Expected: 1875
    print()

    # Test Case 4: Zero Salary (₱0)
    salary = 0
    print("Test Case 4: Salary = ₱0")
    print("SSS Deduction:", utils.compute_sss())  # Expected: 1200
    print("PhilHealth Deduction:", utils.compute_philhealth(salary))  # Expected: 0
    print("Pag-IBIG Deduction:", utils.compute_pagibig())  # Expected: 100
    print("Tax Deduction:", utils.compute_tax())  # Expected: 1875
    print()

    # Test Case 5: Negative Salary (₱-5,000) [Should not happen]
    salary = -5000
    print("Test Case 5: Salary = ₱-5,000")
    print("SSS Deduction:", utils.compute_sss())  # Expected: 1200
    print("PhilHealth Deduction:", utils.compute_philhealth(salary))  # Expected: -125 (Invalid case)
    print("Pag-IBIG Deduction:", utils.compute_pagibig())  # Expected: 100
    print("Tax Deduction:", utils.compute_tax())  # Expected: 1875
    print()

    # Test Case 6: High Salary with High Tax (₱200,000)
    salary = 200000
    print("Test Case 6: Salary = ₱200,000")
    print("SSS Deduction:", utils.compute_sss())  # Expected: 1200
    print("PhilHealth Deduction:", utils.compute_philhealth(salary))  # Expected: 4000
    print("Pag-IBIG Deduction:", utils.compute_pagibig())  # Expected: 100
    print("Tax Deduction:", utils.compute_tax())  # Expected: 1875
    print()

    # Test Case 7: Salary with Max SSS Contribution (₱25,000)
    salary = 25000
    print("Test Case 7: Salary = ₱25,000")
    print("SSS Deduction:", utils.compute_sss())  # Expected: 1200
    print("PhilHealth Deduction:", utils.compute_philhealth(salary))  # Expected: 625
    print("Pag-IBIG Deduction:", utils.compute_pagibig())  # Expected: 100
    print("Tax Deduction:", utils.compute_tax())  # Expected: 1875
    print()

    # Test Case 8: Salary with No Tax Deduction (₱15,000)
    salary = 15000
    print("Test Case 8: Salary = ₱15,000")
    print("SSS Deduction:", utils.compute_sss())  # Expected: 1200
    print("PhilHealth Deduction:", utils.compute_philhealth(salary))  # Expected: 375
    print("Pag-IBIG Deduction:", utils.compute_pagibig())  # Expected: 100
    print("Tax Deduction:", utils.compute_tax())  # Expected: 0 (Taxable threshold might exclude this)
    print()

    # Test Case 9: Salary Just Below Taxable Threshold (₱19,999)
    salary = 19999
    print("Test Case 9: Salary = ₱19,999")
    print("SSS Deduction:", utils.compute_sss())  # Expected: 1200
    print("PhilHealth Deduction:", utils.compute_philhealth(salary))  # Expected: 499.97
    print("Pag-IBIG Deduction:", utils.compute_pagibig())  # Expected: 100
    print("Tax Deduction:", utils.compute_tax())  # Expected: 0 (Below taxable threshold)
    print()

    # Test Case 10: Maximum Taxable Salary (₱150,000)
    salary = 150000
    print("Test Case 10: Salary = ₱150,000")
    print("SSS Deduction:", utils.compute_sss())  # Expected: 1200
    print("PhilHealth Deduction:", utils.compute_philhealth(salary))  # Expected: 3000
    print("Pag-IBIG Deduction:", utils.compute_pagibig())  # Expected: 100
    print("Tax Deduction:", utils.compute_tax())  # Expected: 1875
    print()

    print("All test cases executed.\n")

# Run the test cases
if __name__ == "__main__":
    run_test_cases()
