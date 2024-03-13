class Employee: 
    def __init__(self,eid,name,sal): 
        self.emp_id=eid
        self.emp_name=name
        self.emp_salary=sal

    def display(self): 
        print("Employee id:",self.emp_id)
        print("Employee name:",self.emp_name)
        print("Employee salary:",self.emp_salary)
class changes: 
    @staticmethod
    def increment(obj): 
        obj.emp_salary=obj.emp_salary+2000
        obj.display()

e1=Employee(101,"shantanu",50000)
changes.increment(e1)
changes.increment(e1)
