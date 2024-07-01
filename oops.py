class A:
    def __init__(self,a,b):
        self.A=a
        self.__B=b
    def printB(self):
        print(self.__B)
ob1=A(2,5)
print(ob1.A)
print(ob1.printB())