
from cgi import test
from tokenize import group
from unicodedata import name
import datetime


class Employee:
    name = ""
    todate = ""
    fromdate=""
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

def datesWorked():
    payperiod = {"fromDate":"","todate":""}
    while True:
        while True:
            try:
                date_string = input("Enter starting workday of pay period for employee:\t")
                date_format = "%m/%d/%Y"
                fromdate = datetime.datetime.strptime(date_string,date_format) 
                payperiod.update({"fromdate": fromdate})
                break
            except ValueError:
                print("Incorrect date format, should be mm/dd/yyyy")

        while True:
            try:
                date_string = input("Enter last workday of pay period for employee:\t")
                date_format = "%m/%d/%Y"
                todate = datetime.datetime.strptime(date_string,date_format) 
                payperiod.update({"todate":todate})
                break
            except ValueError:
                print("Incorrect date format, should be mm/dd/yyyy")
        
        if todate < fromdate:
            print("end date cannot be before start date")
        
        elif todate > fromdate:
            break

    return payperiod

def EmpNameList (EmpList,payperiod):
    count = 0
    name = input("Enter Employee's name\t")
    while name.isalpha == False:
        name = input("Name must contain letters")
    emp = Employee(name)
    emp.fromdate = payperiod.get("fromdate")
    emp.todate = payperiod.get("todate")  

    EmpList.append(emp)
    return emp

def EmpWorkHours (Employee):
    hours = input("Enter hours worked for "+str(Employee.name)+"\t" )
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
    print("Pay Period Start date:\t"+str(Employee.fromdate.strftime("%m/%d/%Y")))
    print("Pay Period End Date:\t"+str(Employee.todate.strftime("%m/%d/%Y")))
    print("Employee Name:\t"+str(Employee.name))
    print("Hours worked:\t"+str(Employee.totalHours))
    print("Hourly Rate:\t"+str(Employee.hourlyRate))
    print("Tax Rate:\t."+str(Employee.taxRate))
    print("GrossPay:\t$"+str(Employee.grossPay))
    print("Income Tax:\t$"+str(Employee.incomeTax))
    print("Net Pay:\t$"+str(Employee.netPay))

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
    print("\n# of Employees:\t"+str(count)+"\nGroup Hours:\t"+str(groupTotalHrs)+"\nGroup Tax:\t$"+str(groupTotalTax)+"\nGroup Net:\t$"+str(groupTotalNet))


ans = ""
x = 1
while x == 1:
    
    payperiod = datesWorked()
    DisplayEmployee(CalculatePay(EmpTaxRate(EmpHrRate(EmpWorkHours(EmpNameList(EmpList,payperiod))))))



    ans = input("\nenter anything to continue. if you want to exit type: end\n")
    if ans == "end" or ans == "End":
        x = 0

GroupTotals(EmpList)
