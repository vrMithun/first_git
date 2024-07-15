class person:
    def __init__(self,fname,lname):
        self.fname=fname+lname
        self.lname=lname,
    def get_fname(self):
        print(self.fname)
class student(person):
    def __init__(self,fname,lname,age):
        person. __init__(self,fname,lname)
        self.age=age           
    def get_age(self):
        print(self.age,self.lname,self.fname)
print(person.__module__)       