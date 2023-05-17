class Parent1:
    def fn1(self):
        print("1")

class Parent2(Parent1):
    def fn2(self):
        print('2')

class Child(Parent2):
    def fn3(self):
        print('3')


ob=Child()
ob1=Parent2()
ob1.fn1()
ob1.fn2()
ob.fn1()
ob.fn2()
ob.fn3()