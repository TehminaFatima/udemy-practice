my_dict = {'name':'John','age':25,',location':'USA'}

name = my_dict['name']
age = my_dict['age']    

print("name:",name) 
print("age:",age)

my_dict['occupation'] = 'developer'
my_dict['age'] = 26

print(my_dict)

#pop method will remove the item from the dictionary
my_dict.pop('age')
print(my_dict)

#del method will delete the dictionary
del my_dict['location']
print(my_dict)

occupation = my_dict.get('occupation','not found')
print(occupation)

keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(keys)
print(values)
print(items)

#update method will add the key value pair to the dictionary
my_dict.update({'name':'John Doe','hobby':'reading'})

#setdefault method will add the key value pair to the dictionary if the key is not present
my_dict.setdefault('hobby','coding')

print(my_dict)