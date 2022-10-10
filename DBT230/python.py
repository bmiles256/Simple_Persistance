import os
import pickle

class Employee:
    def __init__(self, id, firstName, lastName, hireYear):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.hireYear = hireYear

    def __str__(employee):
        return ("\nEmployee ID: " + employee.id + "\nFirst Name: " + employee.firstName + 
        "\nLast Name: " + employee.lastName + "\nHire Year: " + employee.hireYear)

    def make_emp(emp):
        string = emp.split()
        id = string[0]
        fName = string[1]
        lName = string[2]
        hireYear = string[3]
        trim_id = id.replace(",", "")
        trim_fName = fName.replace(",", "")
        trim_lName = lName.replace(",", "")
        trim_hireYear = hireYear.replace(",", "")
        empl = Employee (trim_id, trim_fName, trim_lName, trim_hireYear)
        return empl

#------------------------------------------------------------------------------
Simple_Path = r'C:\Users\NEra3\Desktop\Current Quarter\Sprint 1\Databases 2\Sample Data\assignment1Data\people\simple'

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

#------------------------------------------------------------------------------
Long_Path = r'C:\Users\NEra3\Desktop\Current Quarter\Sprint 1\Databases 2\Sample Data\assignment1Data\people\long'

def add_employee(id, first, last, year):
    location_file = Long_Path
    file_name = id + ".txt"
    newFileLocation = os.path.join(location_file, file_name)
    print(newFileLocation)
    newFile = open(newFileLocation, "w")
    newFile.write(id + "," + first + "," + last +"," + year)
    newFile.close()

def delete_employee(id):
    file_name = str(id) + ".txt"
    file_location = os.path.join(Long_Path, file_name)
    if os.path.exists(file_location):
        os.remove(file_location)
        print("File Deleted!")
    else: 
        print("File not found!")

def update_employee(id, firstName, lastName, year):
    file_name = str(id) + ".txt"
    file_path = Long_Path + file_name
    if os.path.isfile(file_path):
            file_reference = open(file_path, "w")
            string_to_write = ", ".join([str(id), firstName, lastName, str(year),])
            file_reference.write(string_to_write)
            file_reference.close()
#------------------------------------------------------------------------------
Serialize_Path = r'C:\Users\NEra3\Desktop\Current Quarter\Sprint 1\Databases 2\Sample Data\assignment1Data\people\long serialized'

def serializeAllEmployees():
    file_path = Long_Path
    for file in os.listdir(file_path):
        f = os.path.join(file_path, file)
        if os.path.isfile(f):
            file_reference = open(f, "r")
            emp = file_reference.read()
            empl = Employee.make_emp(emp)
            string = emp.split()
            id = string[0]
            trim_id = id.replace(",", "")
            new_file_location = open (Serialize_Path + trim_id + ".ser", 'wb')
            print(id)
            pickle.dump(empl, new_file_location)
            file_reference.close()
            new_file_location.close()

def getSerializedEmployee(id):
    file_name = str(id) + ".ser"
    file_path = Serialize_Path + file_name
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            emp = pickle.load(f)
            print(emp)
            return emp
    else: { print("does not exist")}

ID3 = input("Enter id: ")
getSerializedEmployee(ID3)


#print_people_details(Simple_Path)
#print_employee(Simple_Path)
