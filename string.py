text1 = "programming is fun for me"
# 0:11 or :11 will access the letters from 0 index to eleven
substring1 = text1[0:11]
substring2 = text1[:11]
#12: will access the letters after 12 index
substring3 = text1[12:]

print("substring1",substring1)
print("substring2",substring2)
print("substring3",substring3)



text = "python is versatile"
#-3: will access the last three letters
"""
modified_text = text[-3:]
print("original text :" , text)
print("modified_text :" , modified_text)

"""

#replace method will replace the word versatile with awesome
modified_text = text.replace("versatile", "awesome")
print("text: ",text)
print("modified_text: ",modified_text)

#lower method will convert the text to lower case
lower_case = text.lower()

#upper method will convert the text to upper case
upper_case = text.upper()

#title method will convert the text to title case
title_case = text.title()

print("lower_case: ",lower_case)
print("upper_case: ",upper_case)
print("title_case: ",title_case)




numbers=[1,2,3,4,5]

result = ""
for num in numbers:
    result += str(num)

    print("numbers:",numbers)
    print("concatenated result:", result)
