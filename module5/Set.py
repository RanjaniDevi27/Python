"""
set is unordered collection of data. it does not allowed duplicate
it is similar to list
"""
names={'abc','def','abc','efg','xyz'}
klm=set(names)
print(klm)
set1={1,2,3,4,5}
set2={5,3,6,7,8}
set1.add(10)
print(set1)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))