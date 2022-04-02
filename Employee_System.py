class Employee_Sys:
    def __init__(self):
        self.filename = None
        pass
    def Add_Emp(self,name,age,salary):
        name = name.strip()
        age = int(age)
        salary = int(salary)
        with open(self.filename,"r") as f:
            lines = f.readlines()
            for i in lines:
                line = i.split()
                if line[0] == name:
                    print("\nThis employee already exist!")
                    break
            else:
                with open(self.filename,"a") as f:
                    f.write(f"{name}\t{age}\t{salary}\n")
    def Print_Emp(self):
        with open(self.filename,"r") as f:
            if f.read() == "":
                print("NO employees at the moment!")
            else:
                f.seek(0)
                lines = f.read().splitlines()
                for i in lines:
                    line = i.split()
                    print(f"Employee: {line[0]} has age {line[1]} and salary {line[2]}")
    def Delete_By_Age(self,age_from , age_to):
        age_from = int(age_from)
        age_to = int(age_to)
        flag = True
        with open(self.filename,"r") as f:
            lines = f.readlines()
            for idx,val in enumerate(lines):
                line = val.split()
                if int(line[1]) >= age_from and int(line[1]) <= age_to:
                    print(f"\n\tDeleting {line[0]}")
                    lines.pop(idx)
                    with open(self.filename , "w") as f2:
                        f2.writelines(lines)
                    flag = False
        if flag:
            print("No employee match the age range!")
    def Update_Salary(self,name,new_salary):
        name = name.strip()
        new_salary = int(new_salary)
        with open(self.filename,"r") as f:
            lines = f.readlines()
            for idx,val in enumerate(lines):
                line = val.split()
                if line[0] == name:
                    lines[idx] = f"{line[0]}\t{line[1]}\t{new_salary}\n"
                    with open(self.filename , "w") as f2:
                        f2.writelines(lines)
                    break
            else:
                print("\nThere is no employee with this name!")
    def validate_int(self,inp):
        inp = str(inp)
        inp = inp.strip()
        if inp.isdecimal():
            return True
        return False
    def Export_file(self,filename = "DB.txt"):
        self.filename = filename.strip()
        try:
            open(self.filename , "r")
        except FileNotFoundError:
            open(self.filename, "w")
    def Validate_file_name(self,inp):
        inp = str(inp)
        if inp.endswith(".txt"):
            return True
        return False
if __name__ == "__main__":
    Emp = Employee_Sys()
    while True:
        fname =  input("Enter the file you want to export data from (Default file DB.txt will be created) , Please note that the file extention must be .txt: ")
        if Emp.Validate_file_name(fname):
            break
    Emp.Export_file(fname)
    while True:
        print("\nProgram Options:")
        print("1) Add a new employee")
        print("2) List all employees")
        print("3) Delete by age range")
        print("4) Update salary by name")
        print("5) End the program")
        Option_list = ["1","2","3","4","5"]
        Choice = input("Enter your choice (from 1 to 5): ")
        while Choice not in Option_list:
            print("Invalid input!")
            Choice = input("Enter your choice (from 1 to 5): ")
        if Choice == "1":
            print("\nEnter employee data:")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            salary = input("Enter Salary: ")
            if Emp.validate_int(age) and Emp.validate_int(salary):
                Emp.Add_Emp(name,age,salary)
            else:
                print("\nThe age and salary must be integers! try again!")
        elif Choice == "2":
            print("\n\tEmployess list\n")
            Emp.Print_Emp()
        elif Choice == "3":
            age_from = input("Enter age from: ")
            age_to = input("Enter age to: ")
            if Emp.validate_int(age_from) and Emp.validate_int(age_to):
                Emp.Delete_By_Age(age_from,age_to)
            else:
                print("\nThe range of age must be integers! try again!")
        elif Choice == "4":
            name = input("Enter the name: ")
            new_salary = input("Enter the new salary: ")
            if Emp.validate_int(new_salary):
                Emp.Update_Salary(name,new_salary)
            else:
                print("\nThe new salary must be integer! try again!")
        else:
            break