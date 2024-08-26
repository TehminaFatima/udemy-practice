fruits = ["apple","banana","orange","grape"]

first_fruit = fruits[0]
second_fruit = fruits[1]

print("first fruit : ", first_fruit)     
print("second fruit : ", second_fruit)

nested_list=  [["apple","banana"],["orange","grape"]]
specific_fruit = nested_list[0][1]

fruits.insert(2,"cherry")
print(fruits)

fruits[1] ="kiwi"
print(fruits)
#:2 it will replace the first two fruits with blueberry and strawberry    
fruits[:2] = ["blueberry","strawberry"]
print(fruits)
#append method will add the mango in fruits
fruits.append("mango")
print(fruits)

#insert method will add the pineapple at index 2
fruits.insert(2,"pineapple")
print(fruits)

#remove method will remove the orange from the list
fruits.remove("orange") 
print(fruits)

#pop method will remove the last element from the list
fruits.pop()
print(fruits)

#extend method will add the orange and peach in the list
fruits.extend(["orange","peach"])
print(fruits)

#del method will remove the element at index 1
del fruits[1]
print(fruits)

#clear method will remove all the elements from the list
fruits.clear()
print(fruits)
