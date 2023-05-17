class Parent1:
    def fn1(self):
        print("1")

class Parent2():
    def fn2(self):
        print('2')

class Child(Parent1,Parent2):
    def fn3(self):
        print('3')


ob=Child()
ob.fn1()
ob.fn2()
ob.fn3()