"""
Syntax:
for item_var in range/ iteratable:
Statement
"""

names=[
    "alex",
    "arun",
    "ajay"
]

for name in names:
   # print(name)
    print(name, end="----")
company="ednue"
for letter in company:
    print(letter)
    #print(company)
fruits={
    "apple":10,
    "grapes":20,
    "orange":30
}
for fruit in fruits:
    print(fruit)
for fruit in fruits.items():
    print(fruit)
for fruit in fruits.items():
    print(fruit[0])
for fruit in fruits.items():
    print(fruit[1])
for key,value in fruits.items():
    print(f"Count of {key} is {value}")
for num in range(7):
    print(num)
print("----------------------")
for num in range(2,7):
    print(num)
print("----------------------")
for num in range(2,10,2):
    print(num)