from lab16 import Employee
from lab16 import ShiftSupervisor

def main():
    # this section allows users to input required data
    EmployeeName = input("Enter the name: ")
    EmployeeNumber = int(input("Enter the ID number: "))
    annualSalary = float(input("Enter Annual Salary: "))
    annualProductionBonus = float(input("Enter Annual Production Bonus: "))

    print("\n\n\nShift Supervisor Information:\n")

    # this section will call the parent class and it's attributes
    emp1 = Employee(EmployeeName, EmployeeNumber)
    emp1.printname()
    emp1.printidnum()

    # this section will call the child class and it's attributes
    emp1 = ShiftSupervisor(annualSalary, annualProductionBonus)
    emp1.salary(annualSalary)
    emp1.annualProd(annualProductionBonus)
main()