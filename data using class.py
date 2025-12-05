class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

p = Programmer("tushar", 12000, 25)
print(p.name, p.salary, p.age, p.company)
