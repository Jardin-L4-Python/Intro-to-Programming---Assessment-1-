#Make several dictionaries, where each dictionary represents a different pet. 
#In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
#Next, loop through your list and asyou do, print everything you know about each pet

pets = []

pet = {
    'animal type': 'python',
    'name': 'liz',
    'owner': 'rin',
    'weight': 37,
    'eats': 'worms',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'cassy',
    'owner': 'bea',
    'weight': 3,
    'eats': 'kyla',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'ian',
    'owner': 'carl',
    'weight': 45,
    'eats': 'brush'
}
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ":" + str(value))
