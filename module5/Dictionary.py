"""
Dictionary are unordered collection of data
it consist of key and value
value can be duplicates allowed bur in key it does not allow duplicate
in dictionary it separate key and value by colon(:). key can be any datatype.in the below 101 is key and name is value
"""
stdinfo={
    101:"arun",
    102:"arun",
    103:"ajay"
}
dict(stdinfo)
print(stdinfo)
"""
Methods in Dictionaries are keys(),values(),update(),remove(),items()
"""
print(stdinfo.keys())
print(stdinfo.values())
print(stdinfo.items())
stdinfo.update({104:"vijay"})
print(stdinfo)
stdinfo.pop(101)
print(stdinfo)
print(stdinfo[104])
print(stdinfo.get(103))
