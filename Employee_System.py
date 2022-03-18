class Employee_Sys:
    def __init__(self):
        pass
    def Add_Emp(self,name,age,salary):
        name = name.strip()
        with open("DB.txt","r") as f:
            lines = f.readlines()
            for i in lines:
                line = i.split()
                if line[0] == name:
                    print("\nThis employee already exist!")
                    break
            else:
                with open("DB.txt","a") as f:
                    f.write(f"{name}\t{age}\t{salary}\n")
    def Print_Emp(self):
        with open("DB.txt","r") as f:
            if f.read() == "":
                print("NO employees at the moment!")
            else:
                f.seek(0)
                lines = f.read().splitlines()
                for i in lines:
                    line = i.split()
                    for _ in range(len(lines)):
                        print(f"Employee: {line[0]} has age {line[1]} and salary {line[2]}")
    def Delete_By_Age(self,age_from , age_to):
        flag = True
        with open("DB.txt","r") as f:
            lines = f.readlines()
            for idx,val in enumerate(lines):
                line = val.split()
                if int(line[1]) >= age_from and int(line[1]) <= age_to:
                    print(f"\tDeleting {line[0]}")
                    lines.pop(idx)
                    with open("DB.txt" , "w") as f2:
                        f2.writelines(lines)
                    flag = False
        if flag:
            print("No employee match the age range!")
    def Update_Salary(self,name,new_salary):
        name = name.strip()
        with open("DB.txt","r") as f:
            lines = f.readlines()
            for idx,val in enumerate(lines):
                line = val.split()
                if line[0] == name:
                    lines[idx] = f"{line[0]}\t{line[1]}\t{new_salary}\n"
                    with open("DB.txt" , "w") as f2:
                        f2.writelines(lines)
                    break
            else:
                print("\nThere is no employee with this name!")

if __name__ == "__main__":
    with open("DB.txt","w") as f:
        pass
    while True:
        Emp = Employee_Sys()
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
            age = int(input("Enter Age: "))
            salary = int(input("Enter Salary: "))
            Emp.Add_Emp(name,age,salary)
        elif Choice == "2":
            print("\n\tEmployess list\n")
            Emp.Print_Emp()
        elif Choice == "3":
            age_from = int(input("Enter age from: "))
            age_to = int(input("Enter age to: "))
            Emp.Delete_By_Age(age_from,age_to)
        elif Choice == "4":
            name = input("Enter the name: ")
            new_salary = int(input("Enter the new salary: "))
            Emp.Update_Salary(name,new_salary)
        else:
            break