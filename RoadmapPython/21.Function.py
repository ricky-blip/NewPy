# Function

print(5*"=" + "Structur Function" + 5*"=")
# How To Define Function
def function():
    Total = 2
    print(f'U\'R Number is = {Total}') 

# How to print Function
function()

print("\n" + 5*"=" + "Function inside Function" + 5*"=")
def handphone():
    print("Iphone")

def smartphone():
    handphone() #-> call another function

smartphone()

print("\n" + 5*"=" + "Input Argument" + 5*"=")
def stocksmartphone(Dollar):
    price = 1000
    TotalPrice = Dollar*price
    print(f"Price Smartphone now = ${TotalPrice}")

stocksmartphone(2)

print("\n" + 5*"=" + "Function With Argument" + 5*"=")

print("\n" + 5*"-" + "Simple Argument")
def student(name1):
    print(f"Name This Student = {name1}")
student('Ricky')

print("\n" + 5*"-" + "Keyword Argument")
def Teacher(name2,subject):
    print(f"Name This Teacher = {name2}")
    print(f"Subject This Teacher = {subject}")
Teacher(name2='Ali',subject='Science')
Teacher(subject='Steven',name2='Nuke')

print("\n" + 5*"-" + "Default Argument")
def janitor(name,shift=2,temprament='yes'): #value default in argument
    print(f"Name This Janitor = {name}")
    print(f"Shift This Janitor = {shift}")
    print(f"This Janitor Temprament ? {temprament}")
janitor('Joko')

print("\n" + 5*"=" + "Function With Return Value" + 5*"=")
def quadrate(argument):
    total = argument**2
    print(f"Value Quadrate from {argument} is = {total}")
    return total

a = quadrate(1)
print(f"Value a is = {a}")

print("\n" + 5*"=" + "Function With Return Value and multiple argument" + 5*"=")
def sum(argument1,argument2):
    totalsum = argument1 + argument2
    print(f"{argument1} + {argument2} = {totalsum}")
    return totalsum # if you wanna access out from function

def times(argument3,argument4):
    totaltimes = argument3 * argument4
    print(f"{argument3} x {argument4} = {totaltimes}")
    return totaltimes # if you wanna access out from function

b = sum(1,2)
print(f"Value : {b}")
c = times(3,3)
print(f"Value : {c}")

d = times(3,sum(5,5))
print(f"Value : {d}")

print("\n" + 5*"=" + "Lambda Function" + 5*"=")
# Normal Function
def totallambda(x,y):
    z = x+y
    return z

result = totallambda(2,2)
print(f"Value Result : {result}")

# Lambda Function
flambda = lambda argument: print(argument)

flambda('HALO')

flambda2 = lambda k,l: k*l

print(f"Result Lambda2: {flambda2(5,5)}")

flambda3 = lambda o,m: o*m
iu = flambda3(10,10)
print(f"Result Lambda3: {iu}")

