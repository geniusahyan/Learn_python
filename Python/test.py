# create inheritence in python
# class Parent:
#     def __init__(self, name):
#         self.name = name
#     def display(self):
#         print("Parent")
# class Child(Parent):
#     def display(self):
#         super().display()
#         print("Child")
# child1=Child('John')
# child1.display()


# class Parentc:
#     def myfunction(self):
#         print('parent c fn callded')
# class Childc(Parentc):
#     def myfun2(self):
#         print('child called')
        
# c1 = Childc()
# c1.myfunction()        
# c1.myfun2()   

# class A:
#     def myfuna(self):
#         print('class A')
# class B(A):
#     def myfunb(self):
#         print('class B')
            
# class C(B):
#     def myfunc(self):
#         print('class C')
            
# child = C()
# child.myfunc()

# class A1:
#         def myfuna(self):
#             print('class A1')
# class A2:
#         def myfunb(self):
#             print('class A2')
# class A3(A1,A2):
#         def myfunc(self):
#             print('class A3')
            
# child = A3()
# child.myfunc()


# class A1:
#         def myfuna(self):
#             print('class A1')
# class A2(A1):
#         def myfunb(self):
#             print('class A2')
# class A3(A1):
#         def myfunc(self):
#             print('class A3')
            
# child2 = A2()
# child3 = A3()
# child2.myfuna()
# child3.myfuna()


# class A1:
#         def myfuna(self):
#             print('class A1')
# class A2(A1):
#         def myfunb(self):
#             print('class A2')
# class A3(A1):
#         def myfunc(self):
#             print('class A3')
            
# class A4(A2,A3):
#         def myfund(self):
#             print('class A4')
            
# chb = A4()
# chb.myfuna()
# chb.myfunb()
# chb.myfunc()
# chb.myfund()


# Polimorphism
# class Animal:
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         return 'woff'
# class Cat(Animal):
#     def sound(self):
#         return 'meow'
# animal = Animal()
# dog = Dog()
# cat = Cat()
# animal.sound()
# dog.sound()
# cat.sound()


# class MO:
#      def myfun(self):
#          print('fun whit no arg')
#      def myfun(self,a):
#          print('fun whit 1 arg')
#      def myfun(self,a,b):
#          print(a+b)

# m = MO()
# m.myfun(10,20)
# class MO1:
#      def myfun(self,a):
#          print('mo1 called')
# class MO2(MO1):
#      def myfun(self,a):
#          print('mo2 called')
#          super().myfun('name')
# class MO3(MO2):
#      def myfun(self,a):
#          print('mo3 called')
#          super().myfun('name')
         
# m=MO3()
# m.myfun('name')


# class RBI:
#     def Interset(self):
#         pass
    
# class SBI(RBI):
#     def Interset(self):
#         print('sbi interest is 5%')

# class HDFC(SBI):
#     def Interset(self):
#         print('hdfc interest is 2%')

# s = SBI()
# h = HDFC()

# s.Interset()
# h.Interset()


# class Animal:
#     def move(self):
#         pass
    
# class Dog(Animal):
#     def move(self):
#         print('i can bark')

# class Snack(Animal):
#     def move(self):
#         print('i can hisss')

# d = Dog()
# s = Snack()

# d.move()
# s.move()

# Encapsulation in pythion
# class A:
#     def __init__(self,a):
#         self.__a=a
    
#     def showA(self):
#         print('privete',self.__a)
        
# class B(A):
#     def __init__(self,b):
#         super().__init__(b)
    
#     def showB(self):
#         print('privete',self.__a)
        
# obj = B(20)
# print(obj.showA())

# class A:
#     def __init__(self,a):
#         self._a=a
    
#     def showA(self):
#         print('protected',self._a)
        
# class B(A):
#     def __init__(self,b):
#         super().__init__(b)
    
#     def showB(self):
#         print('protected',self._a)
        
# obj = B(20)
# obj.showA()

