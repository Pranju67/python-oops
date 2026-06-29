
class Student():
   
        # default constructor
   def __init__(self):
      pass
   
        # parameterised constructor
   def __init__(self,name,marks):    # constructor
      self.name = name           # data of each object is different it is defined by (self.)
      self.marks = marks         # self.marks defined marks for objects
      
      # Methods
   def Welcome(self):
      print ("Welcome ", self.name)

   def get_marks(self):
      print(self.marks)

   @staticmethod 
   def hello():
      print ("hello")
      

s1 = Student ("karan",97)       #()-> to call the constructor
print(s1.name,s1.marks)
s1.Welcome()
s1.get_marks()
s1.hello()


# Inheritance 
class Car:

   @staticmethod
   def Start():
      print ("Car started...")
   
   @staticmethod
   def Stop():
      print("Car stopped")

class ToyotaCar (Car):
   def __init__(self,brand):
      self.brand = brand

class Fortuner (ToyotaCar):       # Multi level inheritance
   def __init__(self,type):
      self.type = type

# c1 = ToyotaCar("Fortuner")
# c2 = ToyotaCar("Pirus")
c1 = Fortuner ("Petrol")
print (c1.type)
c1.Start()


