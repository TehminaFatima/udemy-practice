thistuple=("apple","banana","cherry")
print(thistuple)    

#len method will return the length of the tuple
print(len(thistuple))

tuple1  = (1,2,3,'hello')
tuple2 = (4,5,6,'world')
empty_tuple = ()
#concatenation of two tuples
tuple3 = tuple1 + tuple2
print(tuple3)

first_item = tuple1[0]
last_item = tuple1[-1]  

print("first_item:",first_item)
print("last_item:",last_item)   

#slicing of tuple
#1:3 will access the elements from 1 index to 3 index
sliced_tuple = tuple1[1:3]
print("sliced_tuple:",sliced_tuple)

result = 5 in tuple1
print("result:",result)

#count method will return the number of times the element is present in the tuple
count = tuple1.count('hello')
print("count:",count)

#index method will return the index of the element
index = tuple1.index('hello')
print("index:",index)

my_tuple = tuple1 + (1,2,3,4,5)
print(my_tuple)

#repetition of tuple
repeated_tuple = tuple1 * 2
print("repeated tuple",repeated_tuple)

tuple1 += tuple2
print(tuple1)

myList = list(my_tuple)
myList[2] = 10
my_tuple = tuple(myList)
print(my_tuple)