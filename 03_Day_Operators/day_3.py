#Day 3 Exercises
age = 19
height = 175.1
complex = 10j + 10

base = float(input("Enter base: "))
height = float(input("Enter height:"))
area = 0.5 * base * height
print("The area of the triangle is", area )

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c= int(input("Enter side c: "))
perimeter = a+b+c
print("The perimeter of the triangle is", perimeter)

lenght = int(input("lenght: "))
width = int(input("width: "))
area = lenght * width
perimeter = 2* (lenght + width)
print(area , perimeter)

radius = float(input("radius: "))
area = 3.14 * radius**2
circum = 2 * 3.14 * radius
print(area, circum)
x = 2/2
print("X intercept =", x)

import math
x1 = 2
y1 = 2 
x2 = 6
y2 = 10

slope = (y2-y1) / (x2-x1)
e_dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("Slope in 9 ", slope, "Euclidean distance: ",e_dist)
print("Slope in 9 ", slope, "slope in 8" ,2)

l1 = len("Python")
l2 =len("Dragon")
print(l2 > l1)
statement = "I hope this course is not full of jargon"
print("jargon" in statement )
print(not "on" in "dragon" and "python")

print(str(float(len("python"))))

even = int(input("number: "))
print(0 is even%2)

print( 7//3 )
print(int(2.7))

print(type('10') == type(10))
print(type(int(float('9.8'))) == type(10))

hour = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
week =  rate * hour
print("Your weekly earning is" ,  week)

years = int(input("Enter number of years you have lived: "))
seconds = years * 31540000
print("You have lived for ", seconds ,"seconds.")

table = """1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125"""

print(table)