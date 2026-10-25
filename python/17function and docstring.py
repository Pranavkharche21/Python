a = 9
b = 8
c = sum((a,b)) #built in function

def function1():
    print("hello you are in function1")

function1()

def function2(a,b):
   average = (a+b)/2
   return average
v = function2(5,7)
print(v)

def function3(c,d):
   """this will give the output for average number """

   average = (c+d)/2
   return average
print(function3.__doc__)