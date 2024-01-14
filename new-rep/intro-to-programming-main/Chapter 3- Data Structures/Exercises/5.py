#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
#You’ll have to think of someone else to invite.
#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.

guests = ["Annie", "Miel", "Rin"]

name = guests[0].title()
print(name + ", I would like to invite you for dinner.")

name = guests[1].title()
print(name + ", I would like to invite you for dinner.")

name = guests[2].title()
print(name + ", I would like to invite you for dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

#Miel can't make it to the dinner, so let's invite Lyn instead.

del(guests[1])
guests.insert(1, 'Lyn')

#Print the invitations again.
#Annie, Lyn, and Rin are invited.

name = guests[0].title()
print("\n" + name + ", I would like to invite you for dinner.")

name = guests[1].title()
print("\n" + name + ", I would like to invite you for dinner.")

name = guests[2].title()
print("\n" + name + ", I would like to invite you for dinner.")
