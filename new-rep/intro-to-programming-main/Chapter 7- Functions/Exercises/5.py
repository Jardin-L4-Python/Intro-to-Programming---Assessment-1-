#Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the default country.

#Put a country.

def describe_city(city, country='Korea'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

#Put cities.
    
describe_city('Seoul')
describe_city('Tokyo', 'Japan')
describe_city('Busan')