fruits = ['blueberry', 'strawberry', 'cherry', 'orange', 'grape', 'mango']

print("for loop")
for fruit in fruits:
    print(fruit)

print("for loop with range")
#enumerate method will return the index and the value of the list
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("while loop")
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

print("break statement")
for fruit in fruits:
    if fruit == "orange":
        print("orange is found in the list")
        break
    print(fruit)    