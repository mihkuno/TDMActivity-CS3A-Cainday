# Salary Deduction Calculator 💰

A simple Python application that calculates salary deductions for Philippine employees, including SSS, PhilHealth, Pag-IBIG, and tax deductions.

## 📋 Overview

This application helps Filipino employees calculate their net salary after standard government-mandated deductions. It provides a clear breakdown of all deductions and the resulting take-home pay.

## ✨ Features

-  Calculate SSS (Social Security System) contributions
-  Calculate PhilHealth (health insurance) contributions
-  Calculate Pag-IBIG (Home Development Mutual Fund) contributions
-  Calculate tax deductions
-  Validate user input to prevent errors
-  Display a comprehensive salary breakdown

## 🚀 Getting Started

### Prerequisites

-  Python 3.6 or higher

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/salary-deduction-calculator.git
   cd salary-deduction-calculator
   ```

2. No additional dependencies are required for the base functionality.

## 🔧 Usage

Run the main script to start the calculator:

```bash
python main.py
```

Follow the prompts to enter your monthly salary. The application will display a breakdown of your deductions and net salary.

### Example Output

```
Enter your monthly salary: 30000

Salary Breakdown:
-----------------------------
Gross Salary:       30000.0
SSS Deduction:      1200
PhilHealth Deduction: 750.0
Pag-IBIG Deduction: 100
Tax Deduction:      1875
-----------------------------
Total Deductions:   3925.0
Net Salary:         26075.0
-----------------------------
```

## 🧪 Testing

The application includes test cases to ensure the deduction calculations are working correctly. To run the tests:

```bash
python -m unittest utils_test.py
```

The test suite includes cases for:

-  Low salary (₱10,000)
-  Mid-level salary (₱30,000)
-  High salary (₱80,000)
-  Zero salary (₱0)
-  Negative salary (₱-5,000) - validation test

## 📁 Project Structure

-  `main.py` - The main application file with user interface
-  `utils.py` - Contains all the deduction calculation functions
-  `utils_test.py` - Test cases for the deduction functions

## 🔍 Deduction Details

-  **SSS**: Fixed contribution amount of ₱1,200
-  **PhilHealth**: 5% of the salary (employer-employee share, so 2.5% for employee)
-  **Pag-IBIG**: Fixed contribution amount of ₱100
-  **Tax**: Currently uses a fixed amount of ₱1,875 for demonstration

## 🛠️ Development

### Project Roles

| **Group Member**    | **Role**                  |
| ------------------- | ------------------------- |
| **stayfocuz**       | Documenter 📚             |
| **boymaoyyyy**      | Refactoring Specialist 🔧 |
| **moky12345**       | QA/Tester 🧪              |
| **LOCKWERK**        | Security Specialist 🔒    |
| **johnmarestimada** | Security Specialist 🔐    |
| **mihkuno**         | Project Manager 📊        |

## 📝 Todo / Future Improvements

-  Implement a progressive tax calculation based on actual tax brackets
-  Add more flexible SSS contribution tiers based on salary
-  Implement a GUI interface
-  Add option to calculate annual deductions
-  Create a reporting feature to track salary over time
-  Add documentation for contribution limits

## ⚠️ Known Issues

-  Tax calculation is currently simplified and fixed
-  Validation for extreme edge cases may need improvement

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributors

Thanks to all team members for their contributions to this project.
