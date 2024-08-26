my_set = {1,2,3,4,5}
"""
print(my_set)

for item in my_set:
    print(item)

set1 = {1,2,3,4,5}  
set2 = {4,5,6,7,8}

#union of two sets
union_set = set1.union(set2)
print("union_set:",union_set)

#intersection of two sets
intersection_set = set1.intersection(set2)
print("intersection_set:",intersection_set)

#difference of two sets
difference_set = set1.difference(set2)
print("difference_set:",difference_set)


#union of two sets
updated_set = set1|set2
print("updated_set:",updated_set)

#intersection of two sets
updated_set = set1 & set2
print("updated_set:",updated_set)

#difference of two sets
updated_set = set1 - set2
print("updated_set:",updated_set)

result = 5 in set1
print("result:",result) """


#iterating through the set
first_item = next(iter(my_set))
print("first_item:",first_item)

#max method will return the maximum item in the set
max_item = max(my_set)
print("max_item:",max_item)

#min method will return the minimum item in the set
min_item = min(my_set)
print("min_item:",min_item)

#len method will return the length of the set
length = len(my_set)
print("length:",length)

#add method will add the item to the set
my_set.add(6)
print(my_set)

#update method will add multiple items to the set
my_set.update([7,8,9])
print(my_set)

#remove method will remove the item from the set
my_set.remove(9)
print(my_set)

#discard method will remove the item from the set
my_set.discard(8)
print(my_set)

#pop method will remove the last item from the set
my_set.pop()
print(my_set)

#clear method will remove all the items from the set
my_set.clear()
print(my_set)
