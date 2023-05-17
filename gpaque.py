class Student():
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno

    def view(self):
        print("name=",self.name,'\n','age=',self.age,'\n','rollno=',self.rollno)

class Sub(Student):
    def __init__(self,name,age,rollno,marks):
        Student.__init__(self,name,age,rollno)
        self.marks=marks

    def gpaclac(self):
        total=sum(self.marks)
        gpa=(total/len(self.marks))/10
        print(gpa)
        return gpa
    

marks=[90,80,90,70,100]
jk=Sub("jay",21,15,marks)
jk.view()
jk.gpaclac()

