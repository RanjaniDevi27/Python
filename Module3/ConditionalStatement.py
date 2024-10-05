"""
Syntax for if statement and else statement
if condition:
    code line
else:
    code line

"""
name=input("Enter your name:")
if (len(name)==5):
    print("The given name is "+name)
#not
if not len(name)==5:
    print("length of the given name is not 5")
score=input("Enter your score:")
if (int(score)>=50):
    print("pass")
else:
    print("fail")
"""
elif statement is used in multiple condition .we can use multiple elif condition
"""
mark=int(input("Enter your mark:"))
if mark>90:
    print("Outstanding")
elif mark>65:
    print("Average")
elif mark>50:
    print("Good")
else:
    print("fail")
"""
Logical operation => not,or,and
"""
value=int(input("enter your number:")
if (value >=40) and (value<=60):
    print("Enter number is in range")
if (value==1) or(value==0):
    print("entered number is binary")
if not(value==1):
    print("entered number is not 1")