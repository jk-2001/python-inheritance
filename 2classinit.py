class Student():
    def __init__(self,dept,dob,year):
        self.dept=dept
        self.dob=dob
        self.year=year
         


jk=Student("cse",2001,3)
ad=Student("aids",2003,3)

jk.grade="a"
print(jk.grade)
print(ad.__dict__)