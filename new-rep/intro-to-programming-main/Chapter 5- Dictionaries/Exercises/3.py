#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) 
#by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. 
#When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, 
#these new words and meanings should automatically be included in the output.

#Put five more python terms to your glossary.

glossary = {
    'string': 'A sequence of characters.',
    'comment': 'A note or sentence in a program that is not read by the Python interpreter',
    'list': 'A group of items in a certain order.',
    'loop': 'Work through a group of items, gradually',
    'dicitonary': "A group of key-value store.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dicitonary.',
    'condiitonal test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
