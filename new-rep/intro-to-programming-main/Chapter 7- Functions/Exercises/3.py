#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it. 
#Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.


def make_shirt(size, message):
    """Pink shirt."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

#Put size and message of the shirt.

make_shirt('large', 'I love Sparkles!')
make_shirt(message="Naps are the best.", size='medium')