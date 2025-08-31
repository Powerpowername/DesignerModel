# 工厂方法模式还需要将不同子类对象的创建对象下放到子类工厂
# 当出现新的员工时（产品时）秩序要添加新的子类工厂
from enum import Enum
from abc import ABC, abstractmethod

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


    # 登记注册业务流程
    def onBoard(self):
        employee = self.createEmployee()
        employee.registerAccount()
        return employee



class ITDepartment(Department):
    def __init__(self):
        pass

    def createEmployee(self) -> Programmer:
        return Programmer()




class UIDepartment(Department):
    def __init__(self):
        pass

    def createEmployee(self) -> Designer:
        print("this is UIDepartment createEmployee means")
        return Designer()


if __name__ == "__main__":
    print(f"----------")

    itDepartment = ITDepartment()
    employee = itDepartment.onBoard()

    print(f"----------{employee.employee_id}")

    employee1 = itDepartment.onBoard()

    print(f"----------{employee1.employee_id}")
