message = print("Hello Python world!")
print(message)
print('---------------------------------------------')


message = "Hello Python Crash Course world!"
print(message)
print('---------------------------------------------')


# message = "Hello Python Crash Course reader!"
# print(mesage)

name = "ada lovelace"
print(name.title())
print('---------------------------------------------')


name = "Ada Lovelace"
print(name.upper())
print(name.lower())
print('---------------------------------------------')

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"  #doing concatenation
print(message)
print('---------------------------------------------')


print('\thello world')   # tab
print('\nhello \nPython \nC')   # new line 
print('---------------------------------------------')

print("Languages:\n\tPython\n\tC\n\tJavaScript.")


favourite_language = 'python'
print(favourite_language)
favourite_language = '     python'    #removed temporarily
print(favourite_language.lstrip())
favourite_language = 'python     5    '
print(favourite_language.rstrip()) #removed temporarily


print('---------------------------------------------')

favourite_language = 'python      '
favourite_language = favourite_language.strip()  #permanently
print(favourite_language)  
