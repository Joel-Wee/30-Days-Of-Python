string = ['Thirty', 'Days', 'Of', 'Python']
final_string = " ".join(string)
print(final_string)

words = 'Coding', 'For' , 'All'
final_words = " ".join(words)
print(final_words)

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.strip("Coding"))
print(company.find("All"))
print(company.replace("Coding For All", "Python"))
new = "Python for Everyone"
print(new.replace("Everyone", "All"))
print(company.split(" "))
new = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(new.split(", "))
print(company[0])
print(len(company) - 1)
print(company[10])
print("PCE")
print("CFA")
print(company.find("C"))
print(company.find("F"))
print(company.rfind("l"))

sen = 'You cannot end a sentence with because because because is a conjunction'
print(sen.find("because"))
print(sen.rfind("because"))
print(sen.replace("because because because", ""))

print(company.startswith("Coding"))
print(company.endswith("coding"))

sen = '   Coding For All      '
print(sen.strip(" "))

library =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
new_lib = "# ".join(library)
print(new_lib)

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity\t\nAsabeneh\t250\tFinland\tHelsinki".expandtabs(11))

radius = 10
print("radius = 10")
print("area = 3.14 * radius ** 2")
print(f"The area of a circule with radius {radius} is {3.14 * radius**2} meters square")

print("8 + 6 = 14")
print("8 - 6 = 2")
print("8 * 6 = 48")
print("8 / 6 = 1.33")
print("8 % 6 = 2")
print("8 // 6 = 1")
print("8 ** 6 = 262144")