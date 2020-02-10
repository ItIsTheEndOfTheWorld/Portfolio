from rooms import bandLocker
import random
#bandLocker is the room you start out in.

#b - list of almost all players. They are printed for the player to view. The player can pick one. If they don't, it's randomized.
#the only player not listed is chad, which we used for development and testing purposes. chad is our god.
b = ["Jack", "Brendan", "Sebastian", "Nathan", "Drew", "Caleb", "Megan", "Ryan", "Emily", "Kylee"]
for e in b:
    print(">" + e)
a = raw_input("What character would you like to be?\n").strip()
if a != "":
    a = a[0].upper() + a[1:].lower() #format the string properly so it's checked accurately against the list.
if a not in b and a.lower() != "chad":
    a = random.choice(b)
    print("You did not enter a valid choice. You are going to be " + a + ".")
    
bandLocker(a.lower())
#starts game.
#alternately, you could just go to the file location and run that, but this seemed... easier
