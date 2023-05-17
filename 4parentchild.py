class Parent():
    def __init__(self,name,age,):
        self.name=name
        self.age=age

    def view(self):
        
        print(self.name,self.age)

class Child(Parent):
    def __init__(self,name,age):
        Parent.__init__(self,name,age)
        self.lastname="m"

s1=Child("jk",21)
s1.view()