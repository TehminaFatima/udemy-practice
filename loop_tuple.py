my_tuple = (1,2,3,4,5)

for item in my_tuple:
    print(item)

for num in my_tuple:
    if num > 30:
        print(num)

nested_tuple = ((1,2,3),(4,5,6),(7,8,9))    
for tuple in nested_tuple:
    for num in tuple:
        print(num)