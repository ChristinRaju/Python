class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.salary = 0

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, age, monthly_salary):
        super().__init__(name, age)
        self.salary = monthly_salary

    def calculate_salary(self):
        print("Full-time employee salary is:", self.salary)


class PartTimeEmployee(Employee):
    def __init__(self, name, age, hourly_wage, hours_worked):
        super().__init__(name, age)
        self.salary = hourly_wage * hours_worked

    def calculate_salary(self):
        print("Part-time employee salary is:", self.salary)


class ContractEmployee(Employee):
    def __init__(self, name, age, contract_fee):
        super().__init__(name, age)
        self.salary = contract_fee

    def calculate_salary(self):
        print("Contract employee salary is:", self.salary)


print("=== Full-Time Employee ===")
emp1 = FullTimeEmployee("Alice", 30, 50000)
emp1.display_info()
emp1.calculate_salary()

print("\n=== Part-Time Employee ===")
emp2 = PartTimeEmployee("Bob", 24, 300, 40)
emp2.display_info()
emp2.calculate_salary()

print("\n=== Contract Employee ===")
emp3 = ContractEmployee("Charlie", 35, 75000)
emp3.display_info()
emp3.calculate_salary()
