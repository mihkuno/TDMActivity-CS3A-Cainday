import unittest
import utils  # Ensure utils.py is in the same directory or in the Python path

class TestSalaryDeductions(unittest.TestCase):
    
    def test_low_salary(self):
        salary = 10000
        self.assertEqual(utils.compute_sss(), 1200)
        self.assertEqual(utils.compute_philhealth(salary), (salary * 0.05) / 2)
        self.assertEqual(utils.compute_pagibig(), 100)
        self.assertEqual(utils.compute_tax(), 1875)
        total_deductions, sss, philhealth, pagibig, tax = utils.compute_total_deductions(salary)
        self.assertEqual(total_deductions, sss + philhealth + pagibig + tax)
        self.assertEqual(utils.compute_net_salary(salary, total_deductions), salary - total_deductions)

    def test_high_salary(self):
        salary = 50000
        self.assertEqual(utils.compute_sss(), 1200)
        self.assertEqual(utils.compute_philhealth(salary), (salary * 0.05) / 2)
        self.assertEqual(utils.compute_pagibig(), 100)
        self.assertEqual(utils.compute_tax(), 1875)
        total_deductions, sss, philhealth, pagibig, tax = utils.compute_total_deductions(salary)
        self.assertEqual(total_deductions, sss + philhealth + pagibig + tax)
        self.assertEqual(utils.compute_net_salary(salary, total_deductions), salary - total_deductions)
    
    def test_zero_salary(self):
        salary = 0
        self.assertEqual(utils.compute_sss(), 1200)
        self.assertEqual(utils.compute_philhealth(salary), 0.0)
        self.assertEqual(utils.compute_pagibig(), 100)
        self.assertEqual(utils.compute_tax(), 1875)
        total_deductions, sss, philhealth, pagibig, tax = utils.compute_total_deductions(salary)
        self.assertEqual(total_deductions, sss + philhealth + pagibig + tax)
        self.assertEqual(utils.compute_net_salary(salary, total_deductions), salary - total_deductions)

    def test_negative_salary(self):
        salary = -5000
        self.assertEqual(utils.compute_sss(), 1200)
        self.assertEqual(utils.compute_philhealth(salary), (salary * 0.05) / 2)
        self.assertEqual(utils.compute_pagibig(), 100)
        self.assertEqual(utils.compute_tax(), 1875)
        total_deductions, sss, philhealth, pagibig, tax = utils.compute_total_deductions(salary)
        self.assertEqual(total_deductions, sss + philhealth + pagibig + tax)
        self.assertEqual(utils.compute_net_salary(salary, total_deductions), salary - total_deductions)

if __name__ == "__main__":
    unittest.main()