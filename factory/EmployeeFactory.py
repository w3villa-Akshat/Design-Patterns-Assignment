class Employee:
    def info(self):
        return "Generic Employee"


class FullTimeEmployee(Employee):
    def info(self):
        return "Full-Time Employee"


class PartTimeEmployee(Employee):
    def info(self):
        return "Part-Time Employee"


class InternEmployee(Employee):
    def info(self):
        return "Intern Employee"


class EmployeeFactory:
    def create_employee(self, emp_type):
        emp_type = emp_type.lower()
        if emp_type == "fulltime":
            return FullTimeEmployee()
        elif emp_type == "parttime":
            return PartTimeEmployee()
        elif emp_type == "intern":
            return InternEmployee()
        else:
            raise ValueError("Unknown employee type")