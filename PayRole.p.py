
from re import IGNORECASE
from tokenize import group
import traceback
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
    Employee.grossPay = int(Employee.hourlyRate)*int(Employee.totalHours)
    Employee.incomeTax = Employee.grossPay*(int(Employee.taxRate)/100)
    Employee.netPay = Employee.grossPay - Employee.incomeTax

    return Employee

def CalculatePays (Employees):
    for Employee in Employees:
        Employee.grossPay = int(Employee.hourlyRate)*int(Employee.totalHours)
        Employee.incomeTax = Employee.grossPay*(int(Employee.taxRate)/100)
        Employee.netPay = Employee.grossPay - Employee.incomeTax

    return Employees

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

def DisplayEmployees (Employees):
    for Employee in Employees:
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
        groupTotalHrs=groupTotalHrs+int(employee.totalHours)
        groupTotalTax=groupTotalTax+int(employee.incomeTax)
        groupTotalNet=groupTotalNet+int(employee.netPay)

    print("\n# of Employees:\t"+str(count)+"\nGroup Hours:\t"+str(groupTotalHrs)+"\nGroup Tax:\t$"+str(groupTotalTax)+"\nGroup Net:\t$"+str(groupTotalNet))

def saveEmpList(EmpList):
    f = open("payrole", "a")
    for emp in EmpList:
        f.write("%s|%s|%s\t|%s\t\t|%s\t\t|%s\n" %(str(emp.fromdate.strftime("%m/%d/%Y")),str(emp.todate.strftime("%m/%d/%Y")),str(emp.name),str(emp.totalHours),str(emp.hourlyRate),str(emp.taxRate)))
    
def readEmpList():
    f=open("payrole","r")
    print(f.read())

def runPayrole():
    count = 0
    payroleList = []
    shortList = []
    date_format = "%m/%d/%Y"

    f = open("payrole","r")
    next(f)
    for line in f:
        print(line)
        if count > 0:
            cleandata = line.replace("\t","")
            empdata = cleandata.rsplit("|")
            emp = Employee(empdata[2])
            emp.fromdate = datetime.datetime.strptime(empdata[0],date_format) 
            emp.todate = datetime.datetime.strptime(empdata[1],date_format) 
            emp.name = empdata[2]
            emp.totalHours = empdata[3]
            emp.hourlyRate = empdata[4]
            emp.taxRate = empdata[5]
            payroleList.append(emp)
        count+=1

    print("Payrole list")

    while True:
        payRoleRange = input("Enter all or the date you want to go as far back for payrole data\t")
        if payRoleRange == "all":
            CalculatePays(payroleList)
            GroupTotals(payroleList)
            DisplayEmployees(payroleList)
            break
        else:
            try:
                startdate = datetime.datetime.strptime(payRoleRange,date_format) 
                for employee in payroleList:
                    if employee.fromdate >= startdate:
                        shortList.append(employee) 
                if len(shortList) == 0:
                    print("No Employees in this list")
                else:
                    CalculatePays(shortList)
                    GroupTotals(shortList)
                    DisplayEmployees(shortList)
                break
            except ValueError:
                    print("Incorrect date format, should be mm/dd/yyyy or enter all\n")
                    traceback.print_exc

ans = ""
x = 1
while x == 1:
    
    payperiod = datesWorked()
    CalculatePay(EmpTaxRate(EmpHrRate(EmpWorkHours(EmpNameList(EmpList,payperiod)))))

    ans = input("\nenter anything to continue. if you want to exit type: end\n")
    if ans == "end" or ans == "End":
        x = 0

saveEmpList(EmpList)
"""readEmpList()"""
runPayrole()

