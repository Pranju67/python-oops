#                       class method
# Aim -> To change class attribute name using ChangeName method 

class Person:
    name = "Rakesh"

    
    # def ChangeName(self,name):
    #     self.name = name
        # Person.name = name 1st way
        # self.__class__.name = "rahul"  2nd way

    @classmethod                 # Original class method
    def ChangeName(cls,name):
        cls.name = name

p1 = Person()
p1.ChangeName("Rajesh")
print(p1.name)
print(Person.name)

