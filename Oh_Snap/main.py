from rooms import bandLocker
import random

b = ["Jack", "Brendan", "Sebastian", "Nathan", "Drew", "Caleb", "Megan", "Ryan", "Emily", "Kylee"]
for e in b:
    print(">" + e)
a = raw_input("What character would you like to be?\n").strip()
if a != "":
    a = a[0].upper() + a[1:].lower()
if a not in b and a.lower() != "chad":
    a = random.choice(b)
    print("You did not enter a valid choice. You are going to be " + a + ".")
bandLocker(a.lower())
#starts game.
#alternately, you could just go to the file location and run that, then use this method, but i'm lazy.