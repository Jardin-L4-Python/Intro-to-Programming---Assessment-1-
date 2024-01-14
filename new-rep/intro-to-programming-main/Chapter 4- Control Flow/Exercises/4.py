#Stages of Life

#The user is asked to input their age
age= int(input("Input your age:"))

#If age is lesser than or equal to 2, it will print 'You are a baby'
if age<=2:
    print("You are a baby")

#If age is lesser than or equal to 4, it will print 'You are a toddler'
elif age<=4:
    print("You are a toddler")

#If age is lesser than or equal to 13, it will print 'You are a kid'
elif age<=13:
    print("You are a kid")

#If age is lesser than or equal to 20, it will print 'You are a teenager'
elif age<=20:
    print("You are a teenager")

#If age is lesser than or equal to 65, it will print 'You are an adult'
elif age<=65:
    print("You are an adult")

#If age is more than or equal to 65, it will print 'You are an elder'
else:
    print("You are an elder")


