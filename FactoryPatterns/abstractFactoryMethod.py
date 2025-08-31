from enum import Enum
from abc import ABC, abstractmethod

class Project(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def assignTo(self):
        pass
class ITProject(Project):
    def __init__(self):
        pass

    def assignTo(self):
        print("this ITProject")


class UIProject(Project):
    def __init__(self):
        pass

    def assignTo(self):
        print("this UIProject")



# 员工
class Employee(ABC):
    static_id = 0 #直接定义在类中的是类属性，python中就是静态属性

    def __init__(self):
        pass

    @abstractmethod
    def registerAccount(self):  # 当出现新员工时，注册账户,暂时只给这一种指定任务
        pass

class Programmer(Employee):  # 程序员类
    
    def __init__(self):
        self.employee_id = 0
        

    def registerAccount(self):
        Employee.static_id += 1
        self.employee_id = Employee.static_id

class Designer(Employee):

    def __init__(self):
        self.employee_id = 0

    def registerAccount(self):
        Employee.static_id += 1
        self.employee_id = Employee.static_id


# 部门
class Department(ABC):
    def __init__(self):
        pass
    # 创建员工

    @abstractmethod
    def createEmployee(self):# 创建员工
        pass


    @abstractmethod
    def createProject(self):
        pass



class ITDepartment(Department):
    def __init__(self):
        pass

    def createEmployee(self) -> Programmer:
        employee = Programmer()
        employee.registerAccount()
        return employee

    def createProject(self):
        itproject = ITProject()
        itproject.assignTo()
        return


class UIDepartment(Department):
    def __init__(self):
        pass

    def createEmployee(self) -> Designer:
        employee = Designer()
        employee.registerAccount()
        return employee
    def createProject(self):
        UIproject = UIProject()
        UIproject.assignTo()
        return

if __name__ == "__main__":
    print(f"----------")

    itDepartment = ITDepartment()
    employee = itDepartment.createEmployee()
    itDepartment.createProject()
    print(f"----------{employee.employee_id}")
    uiDepartment = UIDepartment()
    employee1 = uiDepartment.createEmployee()
    uiDepartment.createProject()
    print(f"----------{employee1.employee_id}")
