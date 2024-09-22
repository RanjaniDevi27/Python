# Method 1 -Concatenation using +operator
companyName="Ednue Technologies"
suffix ="Pvt Ltd"
print(companyName +" "+suffix)

# Method 2 -% or c-style string formatting
# %s for string
# %d for integer
# %f for float
name="ranjani"
age =25
score=99
#print(name+age)#TypeError: can only concatenate str (not "int") to str
print("%s age is %d.she has scored %.2f in HSC"%(name,age,score))

# Method 3 -.format() method
print("{} age is {}.She has scored {} in HSC.".format(name,age,score))
print("{0} age is {2}.She has scored {1} in HSC.".format(name,age,score))

# Method 4- f'string'
personName="alex"
companyName="google"
print(f"{personName} works in {companyName}")
print("{personName} works in {companyName}")

waterAmount=1.5
noOfTimes=4
totalAmount=waterAmount+noOfTimes
print(f"{personName} works in {companyName}.He Drinks {totalAmount} of a water per day.")
print(f"{personName} works in {companyName}.He Drinks {waterAmount+noOfTimes} of a water per day.")
