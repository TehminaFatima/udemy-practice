fruits = ['apple', 'banana','orange']
for fruit in fruits:
    print(f"i like {fruit}")

    for number in range(10):
        print(f"count :{number}")

        for index,fruit in enumerate(fruits):
            print(f"index:{index} fruit:{fruit}")
           