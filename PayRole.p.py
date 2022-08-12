
from cgi import test
from tokenize import group
from unicodedata import name


class Employee:
    name = ""
    totalHours = 0
    hourlyRate = 0
    taxRate = 0
    grossPay = 0
    incomeTax = 0
    netPay = 0

class Employee:
    def __init__(self,name):
        self.name = name
        self.totalHours = 0
        self.hourlyRate = 0
        self.taxRate = 0
        self.grossPay = 0
        self.incomeTax = 0
        self.netPay = 0


EmpList = []

def EmpNameList (EmpList):
    name = input("Enter Employee's name")
    while name.isalpha == False:
        name = input("Name must contain letters")
    emp = Employee(name)
    EmpList.append(emp)               
    return emp

def EmpWorkHours (Employee):
    hours = input("Enter hours worked for "+str(Employee.name)+" " )
    while hours.isdigit() == False:
        hours = input("Please enter only numbers")

    Employee.totalHours = int(hours)
    return Employee

def EmpHrRate (Employee):
    hrRate = input("Enter "+str(Employee.name)+"'s hourly rate ")
    while hrRate.isdigit==False:

        hrRate = input("Please enter only numbers ")
    Employee.hourlyRate = int(hrRate)
    return Employee

def EmpTaxRate (Employee):
    txRate = input("Enter "+str(Employee.name)+"'s tax rate ")
    while txRate.isdigit==False or  len(txRate)>2:
        txRate = input("tax rate cannot have letters and must be under 100. Please re-enter ")
        
    Employee.taxRate = int(txRate)
    return Employee

def CalculatePay (Employee):
    Employee.grossPay = Employee.hourlyRate*Employee.totalHours
    Employee.incomeTax = Employee.grossPay*(Employee.taxRate/100)
    Employee.netPay = Employee.grossPay - Employee.incomeTax

    return Employee

def DisplayEmployee (Employee):
    print("Employee Name: "+str(Employee.name))
    print("Hours worked: "+str(Employee.totalHours))
    print("Hourly Rate: "+str(Employee.hourlyRate))
    print("Tax Rate: ."+str(Employee.taxRate))
    print("GrossPay: $"+str(Employee.grossPay))
    print("Income Tax: $"+str(Employee.incomeTax))
    print("Net Pay: $"+str(Employee.netPay))

def GroupTotals (EmpList):
    groupTotalHrs = 0
    groupTotalTax = 0
    groupTotalNet = 0
    count = 0
    for employee in EmpList:
        count=count+1
        groupTotalHrs=groupTotalHrs+employee.totalHours
        groupTotalTax=groupTotalTax+employee.incomeTax
        groupTotalNet=groupTotalNet+employee.netPay

    print("\n# of Employees: "+str(count))
    print("Group Hours: "+str(groupTotalHrs))
    print("Group Tax: $"+str(groupTotalTax))
    print("Group Net: $"+str(groupTotalNet))


ans = ""
x = 1
while x == 1:

    DisplayEmployee(CalculatePay(EmpTaxRate(EmpHrRate(EmpWorkHours(EmpNameList(EmpList))))))

    GroupTotals(EmpList)

    ans = input("\nenter anything to continue. if you want to exit type: end\n")
    if ans == "end" or ans == "End":
        x = 0
