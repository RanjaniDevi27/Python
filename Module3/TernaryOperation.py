"""
syntax:
value_if_true if codition else value_if_false
"""
mark=int(input("enter the mark obtain:"))
result= "pass"if(mark>50)else"fail"
print(result)
marks=int(input("Enter the mark obtain:"))
results="fail"if(marks<50)else"Outstanding"if(mark>90)else"Average"
print("Result:"+result)