""" #Data Types
#Numbers 1, 2, 3
def add(x,y):
    print(x + y)
add(1,2)
#strings "a,b,c"
name = "Mark"
def greeting(person):
    print(person)
greeting(name)
#1 and "1" are not the same
add("1","2")
#unidentified/null

#booLeans
tenure = False
def is_tenured(status):
    if(status == True):
        print("They have tenure")
    else:
        print("they are not tenured")

is_tenured(tenure)"""

""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) 

print(values[0])
print(values[6])  """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" day_of_week = "Monday"
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "temp is"
print(f"The {x}")

temp = 68
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """
#if the temp is above 68 it is warm; if it is 68 it is perfect; if it is below 68 it is cold
