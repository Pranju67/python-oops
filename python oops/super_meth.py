class car:
   def __init__(self,type):
      self.type = type

   @staticmethod
   def start():
      print("Car started..")
    
   @staticmethod
   def stop():
      print("Car stopped")
    
class ToyotaCar(car):
   def __init__(self,name,type):
      super().__init__(type)
      self.name = name

car1 = ToyotaCar("prius","electric")
print(car1.name,car1.type)
car1.start()
car1.stop()
   