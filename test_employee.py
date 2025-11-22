from employee import get_employee_details

# 1. Basic test (default sample)
def test_basic_employee():
    expected = "Employee Name: John, Employee ID: A100, Department: HR, Salary: 45000"
    assert get_employee_details("John", "A100", "HR", 45000) == expected

# 2. Sales department employee
def test_employee_sales():
    expected = "Employee Name: Anita, Employee ID: S200, Department: Sales, Salary: 30000"
    assert get_employee_details("Anita", "S200", "Sales", 30000) == expected

# 3. High salary employee
def test_employee_high_salary():
    expected = "Employee Name: Rohit, Employee ID: M500, Department: Management, Salary: 150000"
    assert get_employee_details("Rohit", "M500", "Management", 150000) == expected

# 4. Empty values
def test_employee_empty_values():
    expected = "Employee Name: , Employee ID: , Department: , Salary: 0"
    assert get_employee_details("", "", "", 0) == expected

# 5. Numeric employee ID
def test_employee_numeric_id():
    expected = "Employee Name: Pooja, Employee ID: 100, Department: Finance, Salary: 50000"
    assert get_employee_details("Pooja", 100, "Finance", 50000) == expected

# 6. Float salary
def test_employee_float_salary():
    expected = "Employee Name: Sam, Employee ID: A10, Department: IT, Salary: 45000.75"
    assert get_employee_details("Sam", "A10", "IT", 45000.75) == expected

# 7. Special characters
def test_employee_special_characters():
    expected = "Employee Name: Dr. K@rthik, Employee ID: X#12, Department: R&D, Salary: 90000"
    assert get_employee_details("Dr. K@rthik", "X#12", "R&D", 90000) == expected

# 8. Multiple employees in same test
def test_multiple_employees():
    emp1 = get_employee_details("John", "A1", "IT", 40000)
    emp2 = get_employee_details("Mary", "B2", "HR", 45000)

    assert emp1 == "Employee Name: John, Employee ID: A1, Department: IT, Salary: 40000"
    assert emp2 == "Employee Name: Mary, Employee ID: B2, Department: HR, Salary: 45000"
