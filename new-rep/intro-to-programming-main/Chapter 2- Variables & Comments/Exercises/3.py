#Stripping Names

#The variable is assigned to the string
name= "\tRose Teddy\n"

#Prints the name
print("Unmodified:")
print(name)

#Prints the name and removes the leading whitespace
print("\nUsing 1strip():")
print(name.lstrip())

#Prints the name and removes the trailing whitespace
print("\nUsing rstrip():")
print(name.rstrip())

#Prints the name and removes the leading and trailing whitespace
print("\nUsing strip():")
print(name.strip())

