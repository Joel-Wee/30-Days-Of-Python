# Introduction
# Day 1 - 30DaysOfPython Challenge

print("Hello World!")   # print hello world

print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name': 'Asabeneh'}))  # Dictionary
print(type({9.8, 3.14, 2.7}))    # Tuple

#Exercise Level 1

print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

#3
print("Joel")
print("Nambiar")
print("Malaysia")
print("I am enjoying 30 days of python")

#4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Joel"))
print(type("Nambiar"))
print(type("Malaysia"))

#Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary
print(type(1))
print(type(3.14))
print(type(4j))
print(type("joel"))
print(type(True))
print(type([1,2,3,4,5]))
print(type(("joel", "one", "two")))
print(type({1,2,3,4}))
print(type({
    "year": "2016",
    "month": "Jan",
}))

#Find an Euclidean distance between (2, 3) and (10, 8)
import math

distance = math.sqrt((10-2)**2 + (8-3)**2)
print(distance)