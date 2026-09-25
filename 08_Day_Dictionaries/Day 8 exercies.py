dog = {
    "Name" : "Max",
    "Breed" : "Dog",
    "Legs" : 4,
    "Age" : 6,
}

#first_name, last_name, gender, age, marital status, skills, country, city and address
student = {
    "first_name" : "Joel",
    "last_name" : "Nambiar",
    "gender" : "Male",
    "age" : "19",
    "marital status" : "Single",
    "skills" : ["Javascript", "Python"],
    "country" : "Malaysia",
    "city" : "Shah Alam",
    "address" : {
        "Street code": "40123",
        "House number" : 10
    }
    
}

print(len(student))

print((student["skills"]))
print(type(student["skills"]))

student["skills"].append("HTML")

keys = student.keys()
print(keys)

values = student.values()
print(values)

list = student.items()
print(list)

student.pop("first_name")
print(student)

del dog