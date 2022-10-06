import os

class Employee:
    def __init__(self, id, firstName, lastName, hireYear):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.hireYear = hireYear

    def __str__(employee):
        return ("\nEmployee ID: " + employee.id + "\nFirst Name: " + employee.firstName + "\nLast Name: " + employee.lastName + "\nHire Year: " + employee.hireYear)

Simple_Path = r'C:\Users\NEra3\Desktop\Current Quarter\Sprint 1\Databases 2\Sample Data\assignment1Data\people\simple'

Simple_


def print_people_details(path):
    files = os.listdir(path)
    for files in files:
        if os.path.isfile(os.path.join(path, files)):
            f = open(os.path.join(path, files), 'r')
            for x in f:
                print(x)
            f.close()

def print_employee(path):
    files = os.listdir(path)
    for files in files:
        if os.path.isFile(os.path.join(path, files)):
            f = open(os.path.join(path, files), 'r')
            for x in f:
                string = x
                information = string.split()
                id = information[0]
                fName = information[1]
                lName = information[2]
                hireYear = information[3]
                employee = Employee(id,fName,lName,hireYear)
                print(employee)
            f.close()

def add_employee(id, first, last, year):
    nfile = os.write("%s.csv " % id, "w")

#def delete_employee(id):

#def update_employee(id, firstName, lastName, year):

#def serializeAllEmployees():

#def getSerialized(id):


print_people_details(Simple_Path)
print_employee(Simple_Path)
