'''
print("7"+"4") #comment in python
print("hello",type("hello"))
print("hey",2,'a',sep="~")
'''
# some important modules
# OS module
# pypdf module
# time module
# shutil module
# request module

#some operators
'''
a=12
b=45
c=2
d=5
print("the sum of the two number is :",a+b)
print("the sub of the two numbers is :",a-b)
print("the floor division of two numbers is :",d//c)  #  remover the digit after the decimal
print("the exponential multiplication of two numbers is :",c**d)
'''

# input in python
'''
a=input("enter the name :")
print("my name is :",a)

x=input()
y=input()
print(x+y) 
print(int(x)+float(y))
print("Hello,"+  a)
name = "Dipanshu"
print(name[0:-3])
print(len(name))
'''

# conditional statement
'''
a=int(input("enter your age : "))
print("your age is : ",a)
if(a<18):
    print("you can't drive")
elif(a==18):
    print("Ek mahine or ruk jaa ")
else:
    print("you can drive")
'''

# Match case statement
'''
x = int(input("ENTER THE NUMBER : "))
match x:
    case 0:
        print("x is 0 ")
    case 2:
        print("x is 2 ")
    case _ if (x = 5):
        print("x is 5 ")
    case _:
    print("x is not a valid no.")

'''

#for loop
'''
colors = ["red","green","blue"]
for color in colors :
    print(color)

    for  i in color:
        print(i)
print("-------------")
for i in range(11):
    print(i)
print("-------------")

for k in range(10,-1,-2):
    print(k)
print("-------------")

'''
#while loop
'''
i=0
while(i<=10):
    print(i)
    i+=1
'''

#Break and Continue statement
'''
for i in range(11):
    if(i==5)
        break      
    print(i)
'''
'''
for i in range(10):
    if(i%2!=0):
        continue
    print(i)
'''
#Functions
'''
def greatest(a,b):
    if(a>b):
        print(a," is greater")
    else:
        print(b," is greater")

greatest(3,6)

def islesser(a,b):
    pass
'''

#String formatting
'''
letter = "hey my name is {} and I'm from {}
name = "Harry"
country = "india"
print(letter.format(name,country))
print(f"hey my name is {name} and i'm from {country}")
print(f"hey my name is {{name}} and i'm from {{country}}")   ---- to show the exact thing

'''

#DocString
'''def name(s):
    ''' '''this funcn prints the string''' '''
    print(s)

name("dipanshu")
print(name.__doc__)'''

#Recursion
'''def factorina(n):
    if( n==0 or n==1):
        return 1
    else:
        return n*factorina(n-1)
    
print(factorina(5))'''

'''def fibonacci(n):
    if(n==1 or n==0):
        return n
    f1= fibonacci(n-1)
    f2= fibonacci(n-2)
    return f1+f2

print(fibonacci(6))
    '''

#Sets
'''
s1={1,4,6,7,3}
s2={3,3,6,2,6,8,4}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
set={1,3,5}
set.add(6)  #---- add the element in the set
print(set)
set.remove(1)
print(set)
del set   #---- del method used to delete the entire set

if 3 in s1:
    print("3 is present")
else:
    print("3 is not present")
'''
#Dictionary
'''info={'name':'dipanshu','age':21}
print(info)
print(info.keys())
print(info['age'])
print(info.get('name')) 
print(info.items())

for key,value in info.items():
    print(f"the value corresponding to the key {key} is {value}")
'''

#else in loop 

'''for i in range(6):
    print(i)
    if(i==5):
        break   #if the loop is break then the else block does not run 
                #it only runs after the whole iteration is executed completely

else:
    print("heyy guys")'''

#Exception Handling
'''a=input("enter the number: ")
try:
    for i in range(6):
        print(f"{int(a)}X{i+1} = {int(a)*(i+1) }")
except Exception as e:
    print(e)
    
# except :
#     print("invalid input")
    
print("program is completed")'''

#Raising custom error
'''
a= input("enter the string : ")
if(a!="quit"):
    raise ValueError("the string is different ")
else:
    print("the program is successfully executed")
    
'''

#short hand if-else
'''
a=2
b=5
print(a) if a>b else print("both a and b are equal ") if a==b else print(b)
'''
#Enumerate function

    # --it allows you to loop over a sequence like list,tuple or string and 
    # get the index and value of each element at same time
'''
fruits=['apple','mango','banana']

for index, fruit in enumerate(fruits):
    print(index,fruit)
    
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)
    '''

# How import works
'''import math
print(math.sqrt(9))'''

    #import own created funcn 
'''import kbc'''

    #----from keyword
'''
from math import sqrt,pi,floor
    #from keyword is used to import a specific methods form a library
print(sqrt(9))
print(floor(2.534))
print(pi)
'''
    #----as keyword
'''
from math import pi,sqrt as s
    #as keyword is used to rename the built-in functions 
print(s(9)*pi)
'''

    #----dir function
'''
import math
    # dir funcn gives all the functionns present inside the liberary
print(dir(math))
'''
# if__name__=="__main__":
'''this idiom is used to stop the execution of the programs other than the
    imported functions'''

# OS module
'''
import os

os.mkdir("Downloads") # create folder 
os.rename("Downloads","Tutorial")
folder =os.listdir("1 java/13 LinkedList") # list the file inside the folder
print(folder)
'''

#Lambda function

'''
average = lambda x,y : (x+y)/2
print(average(3,4))
'''

# Map,Filter and reduce
'''
    # map
numbers =[1,2,3,4,5 ]

double = map(lambda x : x*2 , numbers)
print(list(double))

    # filter
even =list(filter(lambda x: x % 2 == 0, numbers))
print(even)

    # reduce
from functools import reduce
sum = reduce(lambda x , y: x+y , numbers)
print(sum)

'''

#----------------------------------------------- OOPs in python----------------------------------------------------------

    # Class and Object
    
'''
class person:
    name ="Dipanshu"
    occupation = "software engineer"
    
    def info(self):
        print(f"{self.name} is a {self.occupation} ")
    
obj1 = person()
obj1.name = "Rohan"
obj1.info()
'''
    #Constructor 
        # it helps to initialise the object 
        # it called every time whenever we call an object

'''
class Student:
    def info(self):
        print(f"{self.name} is enrolled in {self.course}")
    
    def __init__(self,name,course): # constructor is created 
        self.course = course
        self.name = name

obj1 = Student("rohan","bsc")
obj2 = Student(1,2)
obj1.info()
obj2.info()
'''

# Decorators
'''
def greet(fx):
    print('good morning')
    # fx()

@greet
def hello():
    print("hello world")
    '''
# Inheritance

'''
class Employee:
    def __init__(self,name,id):  #constructor
        self.name = name
        self.id = id
        
    def show(self):
        print(f"The id of {self.name} is {self.id}")
        
class Programmer(Employee):
    def showLanguage(self):
        print("the default language is python")    
    
e1 = Programmer("rohan",23)
print(e1.name)
e1.show()
e1.showLanguage()
'''
# class variable and instance variable 

'''
class Employee:
    companyName = "Google" #------- this is class variable which is associated with the class
    def __init__(self,name,salary) :
        self.name = name       # ----this
        self.salary = salary   #-----this
    def showDetails(self):
        print(f"The salary of the {self.name} is Rs. {self.salary} and he/she works in the company {self.companyName}")
        
emp1 = Employee("Dipanshu",10000000)
emp1.salary = 20000000       #----and this are the instance variable which are associated with the objec/instance
emp1.companyName = "Google India"
emp1.showDetails()
emp2 = Employee("rohan",200000)
emp2.showDetails()
'''

# Super Keyword
    #--- it is used to refer to the parent class. 
    # It especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent class.
    
'''
class Employee:
    def __init__(self,name,id) :
        self.name = name
        self.id = id
        
    def details(self):
        print(f"the id of {self.name} is {self.id}")
class programmer(Employee):

    def __init__(self, name, id,lang):
        super().__init__(name, id)       # called a parent class constructor for name and id
        self.lang = lang
        super().details()  #---prints the detail method for e2 obj
        
e1 = Employee("rohan",34)
e2 = programmer("harry",323,"java")

print(e2.name , e2.id)

'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

# Walrus Operatior ( := )

#-- It allows you to assign a value to a variable within an expression.
# This could be useful when you need to use a value multiple time in a loop ,but don't want to repeat the calculation

# foods=list()
# while True:
#     food = input("what food do you like :")
#     if(food!="quit"):
#         foods.append(food)
        
'''
foods = list()                                           #-----same program by using walrus operator
while(food:= input("what food do you like : "))!="quit":
    foods.append(food)
    
print(foods)
'''
# Shutil module

'''
import shutil
shutil.move("Fio.txt","2 Python/Fio.txt")
shutil.copytree("1 Java","java")
'''

#Generators
# special type of functions that allows you to create an iterable sequence of value
'''
def my_generator():
    for i in range(50):
        yield i
        
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

for j in gen :
    print (j)
    '''
    
#Function Caching
    # --It is a technique for improving the performance of a program by storing the result of
    # a function call so that you can reuse the result instead of recomputin them everytime the function is called.
'''
import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*4

print(fx(2))
print(fx(4))
print(fx(6))
print(fx(3))
'''


#Multithreading
    # --It allows multiple thread of execution to run concurrently within a single process...
'''
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleep for {seconds} sec.")
    time.sleep(seconds)
    return seconds
    
def main():
    time1 = time.perf_counter()
    # normal code
    # func(4)
    # func(6)
    # func(5)

    # same code using threads
    t1 = threading.Thread(target=func,args=[4])
    t2 = threading.Thread(target=func,args=[6])
    t3 = threading.Thread(target=func,args=[5])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    time2 = time.perf_counter()
    print(time2-time1)

def poolingDemo():
    with ThreadPoolExecutor as executor:
        list = [3,4,5,2,1]  
        results = executor.map(func,list)
    
        for result in results:
            print(result)
    
# poolingDemo()
main()

'''
print('hello')