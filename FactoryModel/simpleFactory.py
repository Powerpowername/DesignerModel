from enum import Enum

class EmployeeType(Enum):
    Programmer = 0
    Designer = 1

class Employee:
    def __init__(self):
        pass
    def showme(self):
        print("my name is Employee")

class Programmer(Employee): #程序员类
    def __init__(self):
        pass

class Designer(Employee):
    def __init__(self):
        pass

class Department(Employee):
    def __init__(self):
        pass
    # 创建员工
    @staticmethod
    def createEmployee(employeeType : EmployeeType):
        if employeeType == EmployeeType.Programmer:
            return Programmer()
        elif employeeType == EmployeeType.Designer:
            return Programmer()
        else:
            raise ValueError(f"无指定类型{employeeType}员工")# 异常抛出
    
if __name__ == "__main__":
    
    employee = Department.createEmployee(EmployeeType.Programmer)
    print(type(employee))