# Shift Supervisor class
print("************ Programmed by ***********")
print("******* Carla Jeanne B. Golena *******")
print("************** BSCOE 1-3 *************\n\n\n")

# Parent Class
class Employee:
    def __init__(self, EmployeeName, EmployeeNumber: int):
        self.EmployeeName = EmployeeName
        self.EmployeeNumber = EmployeeNumber

    # Parent class method for attribute employee name
    def printname(self):
        print("Name: ", self.EmployeeName)

    # Parent class method for attribute employee id
    def printidnum(self):
        print("ID number: ", self.EmployeeNumber)

# Child class
class ShiftSupervisor(Employee):
    # Child class method for attribute annual salary
    def salary(self, annualSalary: float):
        print("Annual Salary: $", annualSalary)

    # Child class method for attribute annual production bonus
    def annualProd(self, annualProductionBonus: float):
        print("Annual Production Bonus: $", annualProductionBonus)