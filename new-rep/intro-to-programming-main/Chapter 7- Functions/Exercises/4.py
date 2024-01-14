#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size='large', message='I love Sparkles!'):
    """Pink shirt."""
    print("\nI am going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

#put size and the message of the shirt.
make_shirt()
make_shirt(size='medium')
make_shirt('small', 'The beach sounds nice right now.')