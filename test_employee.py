from employee import get_employee_details
import pytest
def test_get_employee_details():
    # Sample data for testing
    name = "John"
    emp_id = "A100"
    department = "HR"
    salary = 45000

    # Expected formatted output
    expected = "Employee Name: John, Employee ID: A100, Department: HR, Salary: 45000"

    # Assert the function output matches expected
    assert get_employee_details(name, emp_id, department, salary) == expected
