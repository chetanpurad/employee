def get_employee_details(name, emp_id, department, salary):
    return (
        f"Employee Name: {name}, "
        f"Employee ID: {emp_id}, "
        f"Department: {department}, "
        f"Salary: {salary}"
    )


if __name__ == "__main__":
    # Calling the method without any user input
    result = get_employee_details("Chetan", "E101", "IT", 50000)
    print(result)
