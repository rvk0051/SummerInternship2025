'''
Types of Python Inheritance

There are 5 types of inheritance in python:-

1. Single Inheritance: A child class inherits from one parent class.
2. Multiple Inheritance: A child class inherits from more than one parent class.
3. Multilevel Inheritance: A class is derived from a class which is also derived from another class.
4. Hierarchical Inheritance: Multiple classes inherit from a single parent class.
5. Hybrid Inheritance: A combination of more than one type of inheritance.

'''

# Example:

# 1. Single Inheritance

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

emp = Employee("John", 40000)
print(emp.name, emp.salary)  # Output:- John 40000


# 2. Multiple Inheritance
class Job:
    def __init__(self, salary):
        self.salary = salary

class EmployeePersonJob(Employee, Job):  # multiple inheritance as 'EmployeePersonJob' inherits from
                                         # both 'Employee' and 'Job' classes
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)  # Initialize Employee
        Job.__init__(self, salary)            # Initialize Job

emp2 = EmployeePersonJob("Alice", 50000)
print(emp2.name, emp2.salary)  # Output:- Alice 50000


# 3. Multilevel Inheritance

class Manager(EmployeePersonJob):  # Inherits from 'EmployeePersonJob' which is itself a derived class,
                                # hence multilevel inheritance
    def __init__(self, name, salary, department):
        EmployeePersonJob.__init__(self,name, salary)
        self.department = department

mgr = Manager("Ram", 60000, "HR")
print(mgr.name, mgr.salary, mgr.department)
# Output: Ram 60000 HR


# 4. Hierarchical Inheritance

class AssistantManager(EmployeePersonJob):
    # Inherits from EmployeePersonJob
    # 'AssistantManager' and 'Manager' both classes are inherited from 'EmployeePersonJob' class
    # multiple classes inherited from same class/ have common parent class, that's why hierarchical inheritance.

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  # Explicitly initialize EmployeePersonJob
        self.team_size = team_size

asst_mgr = AssistantManager("Charlie", 45000, 10)
print(asst_mgr.name, asst_mgr.salary, asst_mgr.team_size)
# Output: Charlie 45000 10


# 5. Hybrid Inheritance (Multiple + Multilevel)

class SeniorManager(Manager, AssistantManager):
    # Inherits both Manager and AssistantManager
    # 'Manager' is itself inherited from another class and 'SeniorManager', that's why multiple inheritance
    # and it inherits 2 classes, that's why multiple inheritance
    # As 'SeniorManager' follows multiple kinds of inheritance, it folllows hybrid inheritance

    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name, salary, department)        # Initialize Manager
        AssistantManager.__init__(self, name, salary, team_size)  # Initialize AssistantManager

sen_mgr = SeniorManager("Ram", 70000, "Finance", 20)
print(sen_mgr.name, sen_mgr.salary, sen_mgr.department, sen_mgr.team_size)
# Output: Ram 70000 Finance 20