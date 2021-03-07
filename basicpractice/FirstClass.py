class Employee:
    'First Class of Python'
    empCount = 0

    def __init__(self, name, salary):
        'initial method of class'
        self.name = name
        self.salary = salary

    def printEmp(self):
        'Print  Employee'
        print self.name, self.salary


class Developer(Employee):

    def __init__(self):
        Employee.__init__(self, "developer", 1200000)

    def printdev(self):
        print "Im developer"

    def __add__(self, other):
        return 200


print Employee.__dict__

emp1 = Employee('hello', 300)
emp1.printEmp()
emp1.salary = 250
emp1.printEmp()

print emp1.salary
print hasattr(emp1, "age")
print hasattr(emp1, "salary")
if not hasattr(emp1, "age"):
    print "emp1 don't have attribute: %s" % "age"

dev1 = Developer()
dev2 = Developer()
print Developer.__bases__
print dev1.__class__.__bases__
print dev1 + dev2
print dev1 + emp1
