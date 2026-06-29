# operators and dunder functions
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNum(self):
        print(self.real,"i +" ,self.img, "j")
    
    # __add__ -> dunder function is function which logic has already assigned to add complex numbers
    def __add__(num1, num2):          
        newReal = num1.real + num2.real
        newImg = num1.img + num2.img
        return Complex(newReal, newImg)
    
num1 = Complex(1,2)
num2 = Complex(3,4)
num1.showNum()
num2.showNum()

# num3 = num1.add(num2)   # Using normal add function
# num3.showNum()  

num3 = num1 + num2
num3.showNum()