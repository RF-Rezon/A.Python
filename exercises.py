print('Personal Message')

person_name = "Milton"
print("\tHello " + person_name +", would you like to learn some Python today?")


print('Name Cases')
print("\t",person_name.lower())
print("\t",person_name.upper())
print("\t",person_name.title())


famous_quote='"A person who never made a mistake never tried anything new."'
famous_author="Albert Einstein"


print("\nFamous Quote 1,2")
message_here = famous_author + " once said, " + famous_quote
print(message_here)


print("\nStripping Names")
a_person_name = "  \n\tSalfa     "

print(a_person_name)
print(a_person_name.lstrip())
print(a_person_name.rstrip())
print(a_person_name.strip())



