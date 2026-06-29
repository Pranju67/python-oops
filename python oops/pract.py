class Student():
    def __init__ (self):
        pass
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average (self):
        sum = 0
        for val in self.marks:
            sum += val
        print ("The average is: ", int(sum/3))

s1 = Student ("Avinash",[93,45,67])
s1.average()
# s2 = Student ("Ahar", 67)
# s3 = Student ("Pravin",87)
# print ("The average of students is: ",average())
        
