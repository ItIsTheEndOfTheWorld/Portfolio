import sys
import random
import time
import subprocess as sp
from datetime import datetime as dt
from datetime import timedelta as td
from tictactoe import main

#i'm leaving in all of our development comments. cheer.

# QUESTION: ARE WE GOING TO HAVE DOORS BETWEEN ROOMS BE UNLOCKED? (like davis and jag den or dorsch and barnett)
#no. just the ones that connect to the hallway
#thank the gods this is gonna be long enough already

if True: #hold initializations. inside True because the platform I was working on allowed me to collapse it - i didn't have to see any of this code
    name = ""
    countHoF, countPlant = 0, 0 #number of times you've been in the hall of fame and have seen the plant respectively
    numLib = random.randint(0,3) #generates a number for the weather outside the library
    gym, lockers = False, False #scoreboards in the gym on and whether lockers have been opened
    thanos = "" #thanos location; generated thanosAndCo
    inv = [] #inventory
    iInv = [] #internalInventory
    pencils = [] #list of places where you've picked up a pencil; for dev use, not the user
    #powerups = [] #powerup locations, but i took them out because i didn't want to code them. left in for future recoding
    stone = [] #stone locations
    gotStones = [] #stone locations where the user has gotten stones
    beginningTime = dt.now()
    file = open("log.txt", "w+") #create the log file
    file.close()
    teacher = "none" #dear gods i just dont wanna edit all the rooms again. setting this as default makes my life easier
if True:
    allrooms = ['weight room', '010', '011', 'clinic', '406', '404', '403', '1018', '716', 'library office', '1015', '1000 female restroom', 'commons', '410', 'counselling office', '319', '318', 'library lab', '309', '400 female restroom', '312', '310', '316', 'library', '314', '115', '117', '111', '110', '113', '112', 'big gym', 'photography lab', 'concessions', '200 female restroom', '520', '1019', '1014', 'small gym', '1016', '1017', '1010', '1011', '1012', '1013', '308', 'pac lobby', 'gallery hall', 'commons female restroom', '300', '301', '302', '303', '304', 'below stage', '306', '100 restroom', '108', '109', "mathis's photography lab", '102', '103', '101', '106', '107', '104', '105', '519', '518', '1009', '1008', '1007', '1006', '1005', '515', '517', '516', '1000 male restroom', 'hall of fame', 'lecture hall', 'main office', '600 male restroom', '200 male restroom', 'kitchen', '400 male restroom', '317', 'teacher lounge', 'backstage', 'down male locker', '1020', '1022', 'pac', '605', '607', '603', '609', 'tech room', '320', '321', 'down female locker', '201', '200', '202', '204', 'commons male restroom', '003', '002', '001', '007', '006', '005', '004', '009', '008', 'up male locker', '1003', 'up female locker', '1001', 'equipment room', '600 female restroom', 'catwalk']

    
#FUNCTION LIST:
#   aide - help function. lists most available commands (if not all - there are probably some hidden in specific rooms, hence the 
#       "most", but i'm not sure)
#   moveThereMoveWhere - determines all possible places the user can move
#   move - determine where the user can move where they're trying to move
#   other - determines if win conditions have been met, else prints all possible places user can move
#   tiny - function that holds other functions and determines what needs to be used. also has fun commands!
#   pencilDesk - for picking up pencils. also has the senate closet and power stone, as those are on a desk.
#   turn - not yet implemented
#   whoami - prints name
#   inventory - prints user's inventory
#   roomSpecificCommands - exactly what it says. don't bother reading this; just play the game.
#   look - allows user to get a description of the current room. if thanos is in the room, you get thanos.
#       again, don't... don't bother reading the code. it's a Whole Lot of description
#   busted - deals with what happens when davis catches up to user. may not... actually be used, as i think
#       it relies on turns, but i also used time somewhere, so maybe it relies on that.
#   thanosAndCo - generates where thanos and powerups are. (powerups not yet implemented)
#   stones - generates where all the stones that aren't power are.
#   beginTime - registers time user began
#   elapsed - determines elapsed time
#   writeLog - writes to a file all the valid moves the user makes. was created because i cleared the screen
#       and couldn't remember my previous moves
#   removeLine - removes a line from the file



def aide(c):   #general command set
    #aide as in aider for mes amis francais
    s = "\nmove               > type the number/name of the room you want to move to\nview inventory     > type \"inventory\"\nlook around        > type \"look\"\nsearch desk        > type \"search\" or \"search desk\"\nview used commands > go to \"log.txt\". most recent will be at the top"
    room = c #fool
    if c == "counselling office":
        s += "\nconduct heist      > type \"steal\" or \"heist\""
    elif c == "library office":
        s += "\npick lock          > type \"pick\""
    elif c == "tech room":
        s += "\nopen chest         > type \"open\""
    elif room == "equipment room":
        s += "\nchange display     > type \"technology\""
    elif room == "band locker":
        s += "\nopen locker        > type \"open\""
    elif room == "weight room":
        s += "\nlook at rug        > type \"investigate\""
    elif room == "006":
        s += "\nsomething cool     > type \"Easter egg\""
    elif room == "103":
        s += "\nplay tape          > type \"play\" (make sure you have the VHS tape first)"
    elif room == "106":
        s += "\nplay a game        > type \"tic-tac-toe\""
    elif room == "107":
        s += "\nopen cabinets      > type \"open\""
    elif room == "310":
        s += "\nbreak field        > type \"voodoo\""
    elif room == "404":
        s += "\nphotoshop          > type \"photoshop\""
    elif room == "406":
        s += "\nmove covering      > type \"covering\""
    elif room == "410":
        s += "\nsteal money        > type \"steal\""
        s += "\ngo to Narnia       > type \"closet\""
    elif room == "515":
        s += "\ntake rabbit        > type \"rabbit\""
    elif room == "609":
        s += "\nmake gauntlet      > type \"make\""
    elif room == "906":
        s += "\nplay piano         > type \"play\""
    elif room == "914":
        s += "\ntourner le roue    > tape \"tournes\""
    elif room == "teacher lounge":
        s += "\nget a coke         > type \"coke\" (make sure you have money first)"
    elif room == "kitchen":
        s += "\nget the corn       > type \"corn\""
    elif room == "below stage":
        s += "\nget an item        > type \"take\""
    elif room == "commons":
        s += "\nget mayo packet    > type \"take\""
    elif room == "backstage":
        s += "\nget the skull      > type \"take\""
    elif room == "107":
        s += "\ntake an eraser     > type \"take\""
    elif room == "108":
        s += "\nget rubber band    > type \"take\""
    return s

#i think this is everything
def moveThereMoveWhere(currPlace): #can you move to the current place? this should be used in tandem with move. currPlace is the current room number/name
    possPlaces = []#places where you can move
    currPlace = str(currPlace).lower().strip()
    if currPlace[len(currPlace)-2:] == "00": #if it's a hall, in other words
        if currPlace == "000":
               possPlaces = ["200", "400", "600", "001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "library"]
        elif currPlace == "100":
            possPlaces = ["200", "400", "600", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "115", "117", "100 restroom"]
        elif currPlace == "200":
            possPlaces = ["000", "100", "300", "201", "202", "204", "library", "main office", "counselling office", "lecture hall", "gallery hall", "pac lobby", "200 male restroom", "200 female restroom", "small gym", "clinic", "teacher lounge"]
        elif currPlace == "300":
            possPlaces = ["200", "400", "600", "301", "302", "303", "304", "306", "308", "309", "310", "312", "314", "316", "317", "318", "319", "320", "321", "main office", "photography lab"]
        elif currPlace == "400":
            possPlaces = ["000", "100", "300", "700", "403", "404", "406", "410", "gallery hall", "commons", "400 male restroom", "400 female restroom", "small gym"]
        elif currPlace == "500":
            possPlaces = ["600", "515", "516", "517", "518", "519", "520"]
        elif currPlace == "600":
            possPlaces = ["000", "100", "300", "500", "700", "603", "605", "607", "609", "600 male restroom", "600 female restroom"]
        elif currPlace == "700":
            possPlaces = ["400", "600", "716", "gallery hall", "commons", "kitchen"]
        #800 doesn't exist
        elif currPlace == "900":
            possPlaces = ["1000", "902", "903", "904", "905", "907", "908", "909", "910", "913", "914", "915", "916", "917", "918", "919", "pac lobby", "backstage", "band locker room", "900 restroom", "commons"]
        elif currPlace == "1000":
            possPlaces = ["900", "1001", "1003", "1005", "1006", "1007", "1008", "1009", "1010", "1011", "1012", "1013", "1014", "1015", "1016", "1017", "1018", "1019", "1020", "1022", "1000 male restroom", "1000 female restroom", "big gym", "down male locker", "down female locker", "weight room"]
    else:
        if currPlace == "library": #done
            possPlaces = ["library lab", "library office", "library conference", "200", "000"]
        elif currPlace == "library lab" or currPlace == "library office" or currPlace == "library conference":
            possPlaces = ["library"]
        elif currPlace == "gallery hall": #done
            possPlaces = ["200", "400", "700", "commons", "pac lobby"]
        elif currPlace == "small gym": #done
            possPlaces = ["200", "400", "pac lobby"]
        elif currPlace == "big gym": #done
            possPlaces = ["1000", "pac lobby", "commons", "equipment room", "up male locker", "up female locker"]
        elif currPlace == "pac": #done
            possPlaces = ["pac lobby", "backstage", "below stage"]
        elif currPlace == "pac lobby":
            possPlaces = ["pac", "200", "tech room", "gallery hall", "900", "big gym", "small gym"]
        elif currPlace == "tech room":
            possPlaces = ["pac lobby"]
        elif currPlace == "below stage": #done
            possPlaces = ["1000", "pac"]
        elif currPlace == "backstage": #done
            possPlaces = ["900", "pac", "catwalk"]
        elif currPlace == "catwalk":
            possPlaces = ["backstage"]
        elif currPlace == "lecture hall": #done
            possPlaces = ["200"]
        elif currPlace == "kitchen": #done
            possPlaces = ["700", "commons"]
        elif currPlace == "commons": #think it's done
            possPlaces = ["400", "700", "900", "hall of fame", "equipment room", "big gym", "gallery hall", "kitchen", "concessions", "commons male restroom", "commons female restroom"]
        elif currPlace == "hall of fame" or currPlace == "concessions": #done
            possPlaces = ["commons"]
        elif currPlace == "equipment room": #done
            possPlaces = ["big gym", "commons"]
        elif "photography lab" in currPlace: #done
            if "mathis" in currPlace:
                possPlaces = ["909"]
            else:
                possPlaces = ["300"]
        elif "restroom" in currPlace: #done
            if "1" in currPlace:
                if len(currPlace[:4].strip()) == 3:
                    possPlaces = ["100"]
                else:
                    possPlaces = ["1000"]
            elif "2" in currPlace:
                possPlaces = ["200"]
            elif "4" in currPlace:
                possPlaces = ["400"]
            elif "6" in currPlace:
                possPlaces = ["600"]
            elif "9" in currPlace:
                possPlaces = ["900"]
            else:
                possPlaces = ["commons"]
        elif "locker" in currPlace: #done
            if "up" in currPlace:
                possPlaces = ["big gym"]
            elif "band" in currPlace:
                possPlaces = ["900"]
            else:
                possPlaces = ["1000"]
        elif currPlace == "clinic":
            possPlaces = ["200", "main office"]
        elif currPlace == "teacher lounge":
            possPlaces = ["200", "main office", "counselling office"]
        elif "office" in currPlace:
            if currPlace == "main office": #done, though check what pb is
                possPlaces = ["200", "300", "office cb", "office am", "office bb", "office sb", "office do", "office bl", "office lp", "office tk", "office km", "office pb", "counselling office", "teacher lounge", "clinic"]
            elif currPlace == "counselling office":
                possPlaces = ["200", "office cb", "office am", "office bb", "office sb", "office do", "office bl", "office lp", "office tk", "office km", "office pb", "main office", "teacher lounge"]
            else:
                possPlaces = ["main office", "counselling office"] #may not use this
        elif currPlace == "301": #art rooms are connected #all of these are done
            possPlaces = ["300", "204", "303", "403"]
        elif currPlace == "303":
            possPlaces = ["300", "204", "301", "403"]
        elif currPlace == "204":
            possPlaces = ["200", "301", "303", "403"]
        elif currPlace == "403":
            possPlaces = ["400", "204", "301", "303"]
        elif currPlace == "906": #done
            possPlaces = ["907"]
        elif currPlace == "907":
            possPlaces = ["906", "900"]
        elif currPlace == "909": #done
            possPlaces = ["mathis's photography lab", "900"]
        elif len(currPlace) == 4 or currPlace == "weight room": #done?
            possPlaces = ["1000"]
            if currPlace == "1006":
                possPlaces += ["1007"]
            elif currPlace == "1007":
                possPlaces += ["1006"]
        else:
            possPlaces = [currPlace[0] + "00"]
    return sorted(possPlaces, key=len)

def move(currPlace, tryPlace): 
    #currPlace is current place, tryPlace is the place the user's trying to move to
    if "move to" in tryPlace:
        tryPlace = tryPlace[7:]
    elif "move" in tryPlace:
        tryPlace = tryPlace[4:]
    elif "go to" in tryPlace:
        tryPlace = tryPlace[5:]
    elif "go" in tryPlace:
        tryPlace = tryPlace[2:]
    tryPlace = tryPlace.strip().lower()
    possPlaces = moveThereMoveWhere(currPlace)
    if tryPlace in possPlaces:
        return True
    return False

def other(c, teach='none'):
    global teacher, inv, stone, gotStones
    x = moveThereMoveWhere(c)
    tmp = sp.call('clear',shell=True)
    elapsed()
    y = look(c, teach)
    if c in stone and c not in gotStones:
        b = y
        if "MIND" in b:
            raw_input("You grab the Mind Stone - not your best decision - and gasp as a new sense makes its place in your mind. You can now feel the minds of everything around you,\nwhich isn't a lot, surprisingly.")
            inv += ["Mind Stone"]
        elif "REALITY" in b:
            raw_input("You scramble to pick up the Reality Stone. Suddenly, you're outside the school building. You drop the Stone in shock, and the illusion vanishes. You pick it\nup again, this time keeping a firmer grasp on your reality.")
            inv += ["Reality Stone"]
        elif "SOUL" in b:
            if "rabbit" in inv:
                raw_input("You can feel that the Soul Stone is near. You, being as heartless as you are, push the rabbit over the convenient edge of the cliff that has appeared in front\nof you. The Stone appears in response to your sacrifice.")
                inv.remove("rabbit")
                raw_input("You don't directly touch the Soul Stone, though it might be the most harmless of all the Infinity Stones now. Instead, you grab it with the your shirt and\nreverently place it in your pocket.")
                inv += ["Soul Stone"]
        elif "SPACE" in b:
            raw_input("You grab the Space Stone. Nothing particularly happens with it, but you think you've gained an extra shadow.")
            inv += ["Space Stone"]
        else:
            raw_input("You pick up the Time Stone. Suddenly, there's wisdom in your head from those who have had it before you; it instructs you on how\nto use its power and what not to do. You think you know what you can do with this...")
            inv += ["Time Stone"]
        gotStones += [c]
    else:
        y = y.split("rawinput")
        for each in range(0,len(y)):
            raw_input("\n" + y[each])
    teacher = teach
    s = "\n\n\tRooms\n\n"
    q = 0
    for a in x:
        if q%2 == 0:
            s += "\n>" + a
        else:
            s += "\t\t>" + a
        q+=1
    tmp = sp.call('clear',shell=True)
    print("\nWhat would you like to do?\n")
    print s
    return s

def tiny(c, s, i, iI): #c is the current room, s is the string of rooms that you can move to - see other - i is inventory, iI is internalInventory, and teach is teacher
    #this is what holds the functions that need to be used
    global name, iInv, inv, teacher
    iInv = iI
    inv = i
    while True:
        elapsed()
        m = raw_input("\n").lower().strip()
        writeLog(m)
        if m == "help" or m == "h" or "commands" in m:
            raw_input(aide(c))
        elif m == "quit" or m == "exit":
            x = []
            for each in inv:
                each = str(each)
                if "Space" in each:
                    x += ["You use the Space Stone. Davis and Dorsch switch places. Davis is very confused, probably; you're not sure. You can't see him. Dorsch just cheerily\nwaves hello at you."]
                elif "Reality" in each:
                    x += ["You use the Reality Stone. Thanos turns into a giant duck. Davis freaks out and runs away."]
                elif "Mind" in each:
                    x += ["You use the Mind Stone. Davis becomes your puppet. Now you have to teach computer science. Seems like a lose situation to me, but eh."]
                elif "Time" in each:
                    x += ["You use the Time Stone. Davis goes so far back in time that his hair grows back into a hideous mullet. Davis is horrified and goes to get a haircut,\nleaving you alone."]
                elif "Power" in each:
                    x += ["You use the Power Stone. The entire math department materializes above Davis and lands on top of him in a dog pile."]
                elif "Soul" in each:
                    x += ["You use the Soul Stone. Davis gets his soul back, no longer feeling like he needs to display his depression by chasing students."]
            if len(x) == 6:
                raw_input("Well, don't act like you didn't see this coming. Half the universe just evaporates along with the Mighty American Buffalo.\nMegan and Caleb should never have given Davis that Thanos...")
            elif len(x) == 0:
                if "Thanos" in inv:
                    raw_input("Davis stares into Thanos' cold grey eyes. His legs begin to tremble and his shiny bald scalp begins dripping with sweat. He gives you one last glare before turning around and stomping back to his room.")
                else:
                    busted("near")
            else:
                raw_input(random.choice(x))
            sys.exit("\033[3;31;40m\n\nGOODBYE.\n\n\033[0m")
        elif m == "cry":
            raw_input("\nYou curl up into a little ball on the floor and begin to cry.")
            raw_input("Time passes.\n")
            raw_input("You stand up, aching - turns out laying on the floor for an indeterminate amount of time isn't good for your back - but feeling much better.\n")
        elif m == "inventory" or m == "i" or m == "inv":
            inventory()
        elif m in ["heist", "steal"] and c == "counselling office":
            return "heist"
        elif m == "look" or m == "l":
            y = look(c, teacher)
            y = y.split("rawinput")
            for each in range(0,len(y)):
                raw_input("\n" + y[each])
        elif "break dance" in m:
            raw_input("\nYou begin to break dance. Davis catches up to you and joins you.")
            raw_input("You're still break dancing. It's Monday morning, and neither you nor Davis has stopped, making this a weird contest of who-can-break-dance-longer.\nOther students join you.")
            raw_input("School is about to start, but the other students aren't in class. They've crowded around you and Davis and are break dancing.\n")
            raw_input("You open your eyes and blink a few times. What a weird dream. You stand up and move on your way.\n")
        elif m in ["search desk", "search teacher desk", "search", "desk", "teacher desk"] and c[len(c)-2:] != "00":
            pencilDesk(c, teacher)
        elif "who" in m:
            whoami()
        else:
            if (name,m) == ("ryan","burn"):
                print("\nYou pick up a piece of paper from the floor and set it ablaze. Smoke wafts up from the paper towards the sprinkler system.\nThe sprinklers refuse to turn on, however, so you'll have to find some other way to escape Davis.")
            elif name == "megan" and m in ["music", "compose", "play"]:
                print("\nYou whip out a tablet and begin composing a piece on an online editor you found years ago.")
                time.sleep(2)
                print("\nYou finish your piece. About two hours have passed. You decide to play it.\nYou head back to the band locker room and grab your trumpet and a music stand that conveniently was lying around, then exit so you're standing in the 900s hall. Davis appears off in the distance.\nYou begin playing your composition. Davis pauses his stomping to listen.")
                raw_input("")
                time.sleep(.5)
                print("\nYou finish playing your song. Davis claps. You go back into the band locker room to put your stuff back. You then exit and return to where you were,\nas does Davis (out of respect for the song you composed).")
                raw_input("")
            elif name == "caleb" and m in ["history", "philosophy", "rant", "denmark"]:
                #wait is there a point to this i was planning on having calebs end immediately because i thought itd be funny
                print("\nYou begin discussing (with absolutely nobody) how Denmark actually caused 9/11. It's not a conspiracy theory, and it's rather long, but you've got time.")
                time.sleep(2)
                raw_input("\nDavis shows up and begins listening. \"I swear I've heard this before,\" he remarks. You ignore him, as you should, and continue explaining.")
                time.sleep(1)
                raw_input("\nWhen you're finally done, Davis shakes his head and walks away, apparently unwilling to get into another discussion. Shame. You were winding up to talk\nabout literally any historical event he was willing to listen to.")
            elif name == "jack" and m in ["play", "game", "ds"]:
                print("\nYou whip your DS out of your pocket and begin playing Pokemon.")
                time.sleep(2)
                w = random.choice([" Bulbasaur!", " Charmander!", " Squirtle!", " Caterpie!", " Weedle!", " Pidgey!", " Rattata!", " Spearow!", " Ekans!", " Pikachu!", " Sandshrew!", " Nidoran (male)!", " Nidoran (female)!", " Clefairy!", " Vulpix!", " Jigglypuff!", " Zubat!", "n Oddish!", " Paras!", " Venonat!", " Diglett!", " Meowth!", " Psyduck!", " Mankey!", " Growlithe!", " Poliwag!", " Abra! That's hard to do!", " Machop!", " Bellsprout!", " Tentacool!", " Geodude!", " Ponyta!", " Slowpoke!", " Magnemite!", " Farfetch'd!", " Doduo!", " Seel!", " Grimer!", " Shellder!"," Gastly!"," Onix!"," Drowzee!"," Krabby!"," Voltorb!"," Exeggcute!"," Cubone!"," Hitmonlee!"," Lickitung!"," Koffing!"," Rhyhorn!"," Chansey!"," Tangela!"," Kangaskhan!"," Horsea!"," Goldeen!"," Staryu!"," Mr. Mime!"," Scyther!"," Jynx!"," Electabuzz!"," Magmar!"," Pinsir!"," Tauros!"," Magikarp!"," Lapras!"," Ditto!"," Eevee!"," Porygon!"," Omanyte!"," Kabuto!"," Aerodactyl!"," Snorlax!"," Dratini!"," Mew! Wow!"])
                print("\nYou caught a" + w)
                if w == " Mew! Wow!":
                    file = open("achievements.txt", "a+")
                    file.write("MEW")
                    file.close()
                time.sleep(2)
                print("\nYou put your DS away.")
            elif name == "brendan" and m in ["play", "game", "phone"]:
                raw_input("\nYou bring your phone out, ignoring that it's dead. You hold the power button for a few seconds and hold your breath.")
                raw_input("\nIt powers on! You cheer. The lockscreen comes up. You have 3% of your battery left. Good. That's just enough to play a round of Monster Super League.")
                raw_input("\nYou could also make a phone call, but who cares about that. The important thing is that you won't miss a day's worth of events because your phone was dead.")
                raw_input("\nYou get in a round before your phone dies.")
            elif name == "sebastian" and "run" in m:
                raw_input("\nYou decide to do a couple laps through the halls. As you pass Davis, you wave.")
                raw_input("\nYou arrive back where you were after your third lap and decide that's enough.")
            elif name == "nathan" and m in ["wow", "math", "wow!", "i hate math", "time", "how long do i have", "how much time do i have", "davis"]:
                raw_input("\nYou decide to do some math. Maybe you can figure out how long you have before Davis catches you.")
                raw_input("\nYou think you have... " + elapsed() + " seconds left.")
            elif name == "drew" and "build" in m:
                raw_input("\nYou begin to build a robot. You don't have any supplies for it, you quickly realize, but that's never stopped you before.")
                if c != "410":
                    raw_input("\nYou jog to Messick's room, where you hastily build your robot. When Davis appears, you launch it at him. It misses.")
                else:
                    raw_input("\nYou search for supplies and hastily build your robot with the spare parts lying around. When Davis appears, you launch it at him. It misses.")
                raw_input("\nDavis is, however, chased off by the robot, so you've still got time to search with.")
            elif name == "emily" and m in ["play", "instrument", "music", "sing"]:
                raw_input("\nYou pull your kazoo out of your pocket and begin to play the Avengers Theme.")
                time.sleep(2)
                raw_input("\nYou finish and pocket your kazoo.")
            elif name == "kylee" and m in ["code", "program", "davis"]:
                if "timerGlitch" not in iInv:
                    if c != "library":
                        print("\nYou run to the library and quickly log into a computer.")
                    else:
                        print("\nYou run over to one of the computers, quickly powering it on and logging in.")
                    time.sleep(.5)
                    print("\nIt's loading.")
                    time.sleep(1)
                    print("\nIt's still loading. You must not have been on this device before.")
                    time.sleep(.5)
                    raw_input("\nIt loads, and you hurriedly sign on to Cloud9 so you can program. You open oh_snap's code and scroll down, looking for one specific thing.")
                    raw_input("\nThere! You find the timer on the page and alter it; unfortunately, you can't get rid of it. Haha! Davis will now take longer to find you!")
                    iInv += ["timerGlitch"]
                else:
                    if c != "library":
                        print("\nYou run to the library and quickly log into a computer.")
                    else:
                        print("\nYou run over to one of the computers, quickly powering it on and logging in.")
                    time.sleep(.5)
                    print("\nIt's loading.")
                    time.sleep(1)
                    print("\nIt's still loading. You must not have been on this device before.")
                    time.sleep(.5)
                    raw_input("\nIt loads, and you hurriedly sign on to Cloud9 so you can program. You open oh_snap's code and scroll down, looking for one specific thing.")
                    raw_input("\nThere! You find the timer on the page and try to alter it, only to find that you've been restricted to read-only permissions. Rip. There goes that idea.")
            else:
                z = roomSpecificCommands(c, m)
                if not z:
                    y = move(c, m)
                    if y:
                        break
                    raw_input("That's not a valid move, sorry. [press enter]")
                    removeLine()
        print("\nWhat would you like to do?\n")
        print s
    return [m, inv, iInv]

def pencilDesk(c, teach):
    global pencils, inv, teacher, name
    l = False
    if c == "1015" and c not in pencils:
        print("\nWhile rummaging through her desk, you notice a strange button underneath her desk, black and without a label. You've also found the key to the Senate Closet\nand stolen Mrs. Bubalo's pencil, but this button takes the cake. It seems so out of place and almost ominous amongst the rest of the otherwise totally normal\npapers and textbooks.")
        p = inv[0] + 1
        inv[0] = p
        pencils += [c]
        x = raw_input("\nDo you push the button?\n").lower().strip()
        if x == "yes" or x == "y":
            tmp = sp.call('clear',shell=True)
            print("\nThe button isn't nearly as stiff as it appears, and is pressed easily. Suddenly, you are startled by the closet against the wall sliding across the\nfloor. A passage way opens up, but there doesn't seem to be power down it. You peer down the newly revealed steps into the pitch black darkness. That's it, Senate\nis SO CORRUPT!!! You totally need to investigate this, although you still have Davis to worry about. The choice is yours...")
            x = raw_input("\nDo you enter the passage?\n").lower().strip()
            if x == "yes" or x == "y":
                tmp = sp.call('clear',shell=True)
                raw_input("\nYou stumble down the stairs, bumping against the wall to try and steady yourself. The wall feels different, not as smooth as normal. [press enter]")
                raw_input("\nThe stairs keep going down and down, deeper and deeper into the darkness. You can't see your hands in front of you, all you know is you are far below South by\nnow. \"What is Senate doing down here?\" you wonder out loud. Suddenly you here the sound of the entrance sealing itself back up. Ok, time to start freaking out.")
                raw_input("\nYour nervousness causes you to trip and start tumbling down the stairs. You hit a flat bottom quite bruised and in a lot of pain. You feel around until you find\na wall and use it to slowly lift yourself back up to your feet. As your hand slowly crawls up the wall, you feel the outline of a wall switch and you flick it.")
                raw_input("\nSuddenly, hidden bulbs light up in a hazy glow. You're standing at the bottom of stone stairs, the walls made of smooth stones as well. A set of golden doors\nfaces you, taunting your poor broken soul. With nowhere else to go, you open it.")
                raw_input("\nOh my god, Senate is corrupt! You push open the door only to be blinded by bright light reflecting off of mounds and mounds of gold marble. Great pillars hold up\nwhat must be a vault, and great jewels and piles of coins lay in huge piles across the floor. Large couches adorn the center of the chamber, plush and violet,\nand a grand marble table stretches to connect them. A life-sized statue of an jaguar made totally of gold gazes at you from your left, sitting on, you guessed\nit, a marble podium. Strange trinkets like you've never seen before adorn the table, relics of lost civilizations, forgotten art from ages past.... and a top.\nYou spin it, because why not?")
                raw_input("\nSuddenly, your gaze shifts right, and there it is, the fabled Power Stone sitting atop a marble podium! It's all worth it now, the bruises and terror. You've\nfound the Power Stone! Who knows what this will do to Davis. You snatch it before thinking about what to do next.")
                inv += ["Power Stone"]
                raw_input("\nWell, that was a mistake. The moment the power stone is lifted off of its pedistal the roof begins cracking. The room shakes and you are tossed about while\nthe magnificent pillars tumble to the floor.")
                raw_input("\nSuddenly a boulder rolls into view, headed straight for you! (It seems familiar, but you're not sure from where.) You see an... elevator? Ok, you might be able\nto make it, but you're gonna need to roll a saving dex throw.")
                if random.randint(1,20) < 5 and name != "chad":
                    raw_input("\nYou're crushed beneath the boulder. Who knew Senate would kill to keep its corruption hidden? Oh well, it looks like the secret will die with you. As the life\nis squeezed out of your poor body, the last thing you see is that still spinning top. Wait, has it wobbled at all since it started spinning?")
                    file = open("achievements.txt", "a+")
                    file.write("Death - managed to die")
                    file.close()
                    sys.exit("\033[3;31;40m\n\nGAME OVER\n\n\033[0m")
                tmp = sp.call('clear',shell=True)
                raw_input("\nYou slide into the elevator just in time, and the doors shut just before the boulder slams against them. Youch, that would have hurt. The elevator is quite clean\nand well lit, still white in its paint and design.")
                raw_input("\nAs the door clicks open, you are surpised by both the size and clutter of this tiny space. It seems every senate member paints their name onto this wall at some\npoint. It's kinda weird, but whatever, am I right? There's nothing in here that leads you to consider investigating, and you feel your time would be better\nspent elsewhere.")
                nihlExist = "a"
                while nihlExist not in ["yes", "no", "y", "n"]:
                    nihlExist = raw_input("\n\nPause for a moment, dear reader, and answer a question for me: are you a nihlist? A simple yes or no will do.\n").lower().strip()
                raw_input("\nYou ponder what the meaning of all of this is. Of Davis, of yourself, of Thanos... Is there really a meaning behind it all? Why are you running? Why is he chasing\nyou? Why does anyone do anything at all?")
                if nihlExist == "yes":
                    raw_input("\nThere is no meaning to it... TO ANYTHING! Stunned and shocked by this revalation, you curl up into a ball on the floor and wait for Davis (or death, whichever\ncomes first).")
                    file = open("achievements.txt", "a+")
                    file.write("Nihlism at its Finest")
                    file.close()
                    sys.exit("\033[3;31;40m\n\nGAME OVER\n\n\033[0m")
                else:
                    raw_input("\nThere must be a meaning, there must. Maybe finding Thanos will answer this... maybe.")
            else:
                raw_input("\nOh well, probably for the best you leave it be. You already have Davis to worry about, no need to add to your list of worries.")
        else:
            raw_input("Oh well, probably for the best you leave it be. You already have Davis to worry about, no need to add to your list of worries.")
    elif c == "1015":
        raw_input("\nYou already had your mental breakdown for the day; you don't particularly want to have a second one.")
    else:
        for x in pencils:
            if x == c:
                raw_input("\nYou already picked up a pencil from this room.")
                l = True
        if not l:
            try:
                int(c)
                if teach != "none":
                    raw_input("\nYou pick up a pencil from " + teach + "'s desk.")
                    p = inv[0] + 1
                    inv[0] = p
                    pencils += [c]
                else:
                    raw_input("\nYou try in vain to find a desk from which you can steal a pencil. There are none, so you're sad now.")
            except:
                if c in ["library", "counselling office", "main office", "clinic"]:
                    raw_input("You pick up a pencil.")
                    p = inv[0] + 1
                    inv[0] = p
                    pencils += [c]
                pass
    pass

def turn(a=name):
    global name
    if a != name:
        name = a.lower()
    pass

def whoami():
    raw_input("\n" + name[0].upper() + name[1:])

def inventory():
    s = ""
    q = 0
    for e in inv:
        if e == inv[0]:
            s += "\n>" + str(e) + " pencils"
        else:
            if q%2 == 1:
                s += "\t\t>" + str(e)
            else:
                s += "\n>" + str(e)
        q += 1
    print s
    pass

def roomSpecificCommands(room, m): #room is room, m is attempted command
    global inv, iInv
    if room == "library" and "lockpick" in inv:
        if "open" in m or "pick" in m:
            raw_input("\nYou pick the lock on the locked door to Mr. Smith's office. That key you saw on his desk? You take it, claiming it as yours. Unfortunately, as you're not a good\nlockpicker, you've now busted the pick beyond all hope of repair or usage. You throw it away.")
            inv.remove("lockpick")
            inv += ["key"]
            return True
    elif room == "commons" and "take" in m and "mayo" not in inv:
        raw_input("\nYou pick up a packet of mayo. Maybe it'll come in handy later.")
        inv += ["mayo"]
        return True
    elif room == "below stage" and "take" in m and "belowstage" not in iInv:
        r = random.choice(["monarch outfit", "sparkly mirror", "basket of fake flowers"])
        raw_input("\nYou decide to take an item with you: the " + r + ".")
        iInv += ["belowstage"]
        inv += [r]
        return True
    elif room == "backstage" and "skull" not in inv and "take" in m:
        raw_input("\nYou grab the skull. \"Poor Yorick,\" you mutter. \"Poor Yorick.\"")
        inv += ["skull"]
        return True
    elif room == "tech room" and "open" in m and "lockpick" not in inv:
        raw_input("\nYou open the chest. There's only one item in it, a lockpick, and you grab it. Could come in handy.")
        inv += ["lockpick"]
        return True
    elif room == "equipment room" and "technology" in m and not gym:
        raw_input("\nYou mess with the technology in this room - and don't you just hate that general term, technology, but you have no idea what it is that you're messing with -\nand manage to turn the scoreboards in the gym on.")
        gym = True
        return True
    elif room == "band locker" and "open" in m and not lockers:
        raw_input("\nDo you just do the opposite of everything I want you to do? Fine. Have it your way. You begin opening each and every locker in the band locker room.")
        time.sleep(10)
        raw_input("\nYou're still opening lockers but at a slower rate.")
        time.sleep(10)
        raw_input("\nHave you realized how dumb this is yet?")
        time.sleep(10)
        for q in range(0,10):
            raw_input("\nYou're still opening lockers.")
            time.sleep(10)
        raw_input("\nYou finish opening lockers.")
        file = open("achievements.txt", "a+")
        file.write("Dummy of the Year")
        file.close()
        raw_input("\nWhat did you get out of that? Pretty much nothing. Bravo. *coughs* I told you so!")
        lockers = True
        return True
    elif room == "weight room" and "investigate" in m and "rug" not in iInv:
        raw_input("\nYou decide to investigate the rug underneath some of the devices. There's a stain peaking out from underneath it, and beyond that, you think you can make out\nsome kind of trapdoor, but when you go to move the rug, you realize you can't, as you're Weak and incapable of moving the heavy equipment stopping the rug from\nbeing moved.")
        iInv += ["rug"]
        return True
    elif room == "teacher lounge" and "coke" in m and "$5" in inv:
        raw_input("\nYou buy a Coke for $5 dollars. Overpriced, yes, but worth it; the Coke machine doesn't give change, and all you have is a $5.")
        inv += ["Coke"]
        return True
    elif room == "concessions" and "starburst" in m and "5 yellow Starbursts" not in inv:
        raw_input("\nYou pick up five yellow Starbursts from the ground where they lay.")
        inv += ["5 yellow Starbursts"]
        return True
    elif room == "kitchen" and "corn" not in inv and "corn" in m:
        raw_input("\nYou pick up the singluar piece of corn. It's yours now.")
        inv += ["corn"]
        return True
    elif room == "001" and "plant" in m:
        if "water" in m and "water bottle with water" in inv:
            raw_input("\nYou water the plant. It seems happier now, somehow.")
        else:
            raw_input("\nIt's a normal plant.")
        return True
    elif room == "006" and "easter egg" in m and "Easter egg" not in inv:
        raw_input("\nYou pick up an Easter egg off the floor. It's not even close to Easter, so why that was there is beyond your powers of comprehension, but you accept that.")
        inv += ["Easter egg"]
        return True
    elif room == "103" and "VHS" in inv and "play" in m:
        raw_input("\nYou pop the VHS tape into the TV. Then turn the TV on. It shows nothing but static. You don't see a remote anywhere, so you turn to leave when audio starts\nplaying from behind you. It's not in English, so you're not sure what this is, but when you turn back around, you see the communist symbol on the TV. Weird.")
        inv.remove("VHS")
        return True
    elif room == "106" and "tic-tac-toe" in m:
        main()
        return True
    elif room == "107" and "open" in m:
        raw_input("\nYou open one of the many cabinets. There's a small ball bearing, a block of wood, and some string in there. You take out all three, placing the block of wood at\na relatively unsteep angle by leaning it against one of the other cabinets. You put the string back in the cabinet, having forgot why you had it. You travel to\nthe corner of the room and grab a meter stick, measuring the height from the top of the block to the ground. It's .6 m. You grab the timer from the closet and\nreset it. Then you place the ball on top of the block and roll it, beginning the timer when you let it go and stopping it when it hits the floor. You repeat\nthis. You're not sure why you're doing this, but you're doing it. The measurements you're getting are in no way accurate, and they won't help you determine\nwhatever you're trying to determine because they won't, but you're... trying anyway.")
        return True
    elif room == "107" and "take" in m and "Minion Harry Potter eraser" not in inv:
        raw_input("\nYou take the Harry Potter Minion eraser of the side of the desk. You really like it.")
        inv += ["Minion Harry Potter eraser"]
        return True
    elif room == "108" and "take" in m and "rubber band ball" not in inv:
        raw_input("\nYou grab one of the several rubber band balls hanging on the board. It's yours now. You can now shoot rubber bands.")
        inv += ["rubber band ball"]
        return True
    elif room == "310" and "voodoo" in m and "voodoo doll" not in inv:
        raw_input("\nYou begin chanting under your breath. The words just come to you. You aren't sure what you're saying. In time, the force holding you back seems to dissapate.")
        raw_input("\nYou can now walk forward, so you do. You reach the board, and you take one of the voodoo-looking items, a doll. You manage this just in time, as the moment you\nstep away, the force comes back, repelling you stronger than ever.")
        raw_input("\nYou don't think you'll be able to get through it again.")
        inv += ["voodoo doll"]
    elif room == "404" and "photoshop" in m:
        raw_input("\nYou want to mess around with images of Davis and Photoshop on the computers, but you quickly realize that you don't have any photos of Davis to edit. Shame.")
        return True
    elif room == "406" and "covering" in m:
        raw_input("\nYou move the covering to the side. You find a board version of \033[38;2;255;230;203m\033[48;5;55mOh, Snap!\033[0m and pull it out. It's updated in realtime, apparently, as you can see a figure\nrepresenting Davis moving ever so slowly closer to you as the seconds tick away. It creeps you out, quite frankly, so you put it back.")
        return True
    elif room == "410" and "steal" in m and "Magic Messick" not in inv:
        raw_input("\nYou rob the TSA store - honestly, that's ridiculous - and get $5 and a Magic Messick trophy.")
        inv += ["Magic Messick"]
        inv += ["$5"]
        return True
    elif room == "410" and "closet" in m:
        raw_input("\nLight floods the closet as you step into Narnia. You're in the middle of the woods and wind lightly ripples across the grass and trees. You feel safe all of a\nsudden, like Davis can't get you here, as if you're in a whole new world, safe from the whims of Thanos or Davis.")
        file = open("achievements.txt", "a+")
        file.write("Narnia - achieved the Narnia ending")
        file.close()
        sys.exit("\033[3;31;40m\n\nYOU WON\n\n\033[0m")
    elif room == "515" and "rabbit" in m and "rabbit" not in inv:
        raw_input("\nYou pick up a live rabbit. Why not?")
        inv += ["rabbit"]
        return True
    elif room == "609" and "make" in m:
        if "Failed Gauntlet" not in inv:
            raw_input("\nYou try to make an Infinity Gauntlet, but all you can really manage is the middle finger. You decide to keep it anyway, as a memento.")
            inv += ["Failed Gauntlet"]
        else:
            raw_input("\nYou don't really want to try again; you'd be pushing your luck if you did anything extra; you were probably lucky to escape with all your fingers last time.")
        return True 
    elif room == "716" and "storage" in m:
        if "key" in inv:
            raw_input("\nYou unlock the door and enter slowly. It's a storage room; there are boxes everywhere. Curiously, they're all sitting on the floor, none of them on shelving.\nYou relock the door behind you on your way out.")
            file = open("achievements.txt", "a+")
            file.write("Storage Master")
        else:
            raw_input("\nYou can't go in there without a key.")
        return True
    elif room == "906" and "play" in m:
        raw_input("\nYou sit down at the keys and begin to play.")
        time.sleep(1)
        raw_input("\nYou're playing from memory, so this is a little difficult for you, but you don't think you're missing too many notes.")
        time.sleep(3)
        raw_input("\nYou don't remember what comes next, so you stand.")
        return True
    elif room == "914" and "tournes" in m:
        raw_input("\nTu tournes la roue! Elle s'arrete sur... " + random.choice(["MIND", "POWER", "REALITY", "SOUL", "SPACE", "TIME"]))
        raw_input("\nA booming laugh comes from above. \"You didn't think it was that easy, did you? Ha!\"\nYou get nothing from the wheel.")
        return True
    elif "rubber band ball" in inv and "shoot" in m:
        raw_input("\nYou shoot a rubber band.")
        return True
    
    return False
    
def look(room, teach="none"): #room room name/number, teach teacher
    global countHoF, numLib, thanos, powerups, stone, countPlant, gym, beginningTime, gotStones, inv, iInv
    s = ""
    a = ""
    b = ""
    file = open("achievements.txt", "a+")
    room = room.lower()
    if thanos == room and "Thanos" not in inv: 
        b += "The heavens open and glorious trumpets sound inside your head. Thanos, your ticket out of here!! He's still got his hat on, and his glare makes you\nuncomfortable, but you've done it! Your quest has finished and your days of fearing Davis have come to an end."
        inv += ["Thanos"]
        return b
    '''elif room in powerups:
        b += "POWERUP HERE"'''
    if room in stone and room not in gotStones:
        if stone[0] == room:
            b += "MIND STONE HERE"
        elif stone[1] == room:
            b += "POWER STONE HERE"
        elif stone[2] == room:
            b += "REALITY STONE HERE"
        elif stone[3] == room:
            b += "SOUL STONE HERE"
        elif stone[4] == room:
            b += "SPACE STONE HERE"
        else:
            b += "TIME STONE HERE"
        return b
    if room[len(room)-2:] == "00": #halls
        s = "There are doors on either side of the " + room + "s hall.\nYou want to search them all, but you aren't sure if you'll be able to - Davis is chasing you, after all."
        poster = random.choice(["none", "On the left, there's a poster of a film club. It appears to be in German.", "There's a poster advertising the perils of sleep deprivation to your right.", "You turn towards the closest wall and stare at it. It appears to be a normal wall.", "There's a small metal door in front of you. Etched into it is a triangle. It has no significance, but you like it."])
        if poster != "none":
            s += "\n" + poster
    elif "hall" in room:
        if room == "lecture hall":
            s += "On either side, there's a whiteboard with doodles on it. There are rolling tables and chairs here as well. On one of the tables, someone has left a water bottle. You take the bottle because you can."
            inv += ["empty water bottle"]
        elif room == "gallery hall":
            s += "There are flags of Denmark, Japan, Jordan, Norway, Philippines, and Switzerland hanging from the ceiling. Opposite the flags is a row of glass cases.\nThey contain art. You pause to examine some pieces.\n"
            s += random.choice(["This piece appears to be a person with a TV for a head. There's a small plant growing onscreen.", "This photograph, of a highway or some similar dark but lit scene, has hit other pieces and nearly knocked them down. Strange that nobody has fixed it yet.", "There are several sculptures in this case. One of them is of a bulbasaur. There are plants growing out of all of them."])
        elif room == "hall of fame":
            countHoF += 1
            if countHoF < 4:
                s += "There are glass walls on two sides of you; this is a bad place to hide in, if that's what you were trying to do. You can see a series of awards encased in one of\nthe glass walls. Through the other, you can see the commons in its full glory. There's a slideshow being projected directly ahead. It appears to be a\nmontage of Davis.\nThe slideshow speeds up."
            else:
                s += "There are glass walls on two sides of you; this is a bad place to hide in, if that's what you were trying to do. You can see a series of awards encased in one of\nthe glass walls. Through the other, you can see the commons in its full glory. There's a slideshow being projected directly ahead. It appears to be a\nmontage of Davis, but the slideshow is going so fast that you can't be sure of that any more."
            if countHoF == 3:
                s += " The slides are now flicking by so fast that all you can see is a blur.\nA small red balloon appears next to you before vanishing. You turn around in an attempt to ascertain where it has gone, but you see no trace of it.\nThe blur, when you turn back to it, has obtained an edge of color."
                file.write("IT - survived the balloon encounter")
    elif "library" in room:
        if room == "library":
            s += "You are immediately assaulted by the "
            if numLib == 0:
                s += "natural light outside. It burns your eyes to look "
            elif numLib == 1:
                s += "downpour, which, oddly enough, is inside the library. It appears to be contained, however, within the circulation desk.\nYou decide not to go near there and set about exploring. There's some dim natural light that pours "
            else:
                s += "inky black outside. It hurts your eyes to look at this unnatural lack of light " 
            if numLib == 0 or 2:
                s += "through the massive windows on the wall\nahead of you and the wall to your left, so you decide to avoid them.\nYou walk forward with your eyes shut. You think you're in the middle of the library, so you turn 90 degrees clockwise and open your eyes.\nNow all you can see is books. You walk forward slowly, trailing your hand along the rows of books. You stoop down to pull one off the shelf."
            else:
                s += "through the massive windows on the wall ahead of you and the wall\nto your left, so you decide to avoid them.\nYou walk forward with your eyes shut. You think you're in the middle of the library, so you turn 90 degrees clockwise and open your eyes.\nNow all you can see is books. You walk forward slowly, trailing your hand along the rows of books. You stoop down to pull one off the shelf."
                inv += ["Harry Potter and the Philosopher's Stone"]
        elif "lab" in room:
            if "staggeringBeauty" not in iInv:
                s += "You pull the divider between the two labs so the lab is now a full room. Satisfied, you can now move on with your day: time to explore the lab.\nThere are rows upon rows of computers, but you can't see any that are on. You move to the other side of the lab, where you find a single monitor showing an\nodd-looking worm on a white-green gradient background with the words \"Shake vigorously\" on top.\nCurious, you wiggle the mouse, causing the worm onscreen to wiggle and the background to begin a flashing gif sequence. Stunned, you stagger backwards,\nblindly reaching out a hand in the hopes of not falling.\nYour hand hits something - the back of a chair, it feels like, and you put your weight on it. Blinking, you open your eyes. The worm has stopped moving, and\nthe background has stopped flashing.\nYou warily move away."
            else:
                s += " There are rows upon rows of computers. The only one that's turned on is the one with that horrible worm."
        elif "office" in room:
            s += "There's one part of the office that you can't step into - that of the new tech dude, Mr. Smith, so you peer in through the window.\nIt's dark inside, so all you can really see is your reflection, but you pretend that there's something interesting in there - maybe a key - before moving on.\nThere's another part of the office that you can enter, encased between two bookcases. Within this new space is a laminator, a poster maker, several stencils\nfor paper, huge rolls of paper, and a guillotine for papers."
            if "blueRollPaper" not in iInv:
                s += " You tear off a relatively large piece from the blue roll of paper to keep with you."
        else: #library conference
            furious = 0
            for x in iInv:
                if x == "fury":
                    furious += 1
            if "fury" not in iInv:
                s += "You've never been inside these rooms before. Actually, you've never even really noticed that these rooms exist before. There appears to be a meeting going on\ninside. You attempt to tug the door open, but it won't budge. Nick Fury's face appears on the window. He shakes his head. Slowly, you turn and walk away."
            elif furious == 1:
                t = random.choice([["Iron Man", "him"], ["Captain America", "him"], ["Hulk", "him"], ["Hawkeye", "him"], ["Thor", "him"], ["Black Widow", "her"], ["Vision", "him"], ["Rocket Raccoon","him"], ["Groot","him"], ["Star-Lord", "him"], ["Drax", "him"], ["Thanos (the real one)", "him"], ["Gamora", "her"], ["Nebula", "her"], ["Pepper Potts","her"], ["Wasp", "her"], ["Ant-Man", "him"]])
                s += "You turn back. Maybe you can go in after all; you thought you saw " + t[0] + " through the window, and, as " + t[0] + " is your favorite,\nyou would really like to meet " + t[1] + ". You approach the door again. A loud rattling sound comes from inside, followed by a few shouts.\nSounds important. You walk away again."
            elif furious == 2:
                s += "You walk towards the conference room, taking a second to consider whether or not this is a wise decision; do you really want to interrupt Nick Fury again?\nYou got off lightly last time, but you'll probably get killed this time.\nAs you have no sense of self-preservation, you continue to walk towards the conference room. A loud crash comes from behind you, and a large object hurls\npassed your face. It crashes into the wall ahead of you, leaving a hole in its wake. A man - Thor, perhaps, but you can't really see him - grabs it, stopping\nit from moving any further.\nYou cautiously walk up to the hole and peer through it. You catch a glimpse of the man, who is Thor, Captain America, and Maria Hill before another face blocks\nyour view. Nick Fury stares at you. You stare back. He frowns at you, and you back away. His face is replaced with what appears to be his coat.\nThere goes your window."
            elif "furious" not in iInv:
                s += "You go back toward the conference room again, as you are a person who doesn't learn from their previous mistakes.\nYou can hear someone yelling inside. You think it's Fury, but you aren't entirely sure.\nFury carries on for a bit - sounds like these heroes are getting chewed out - before a crash interrupts him.\nUtter silence follows. You quite clearly hear Fury swear. Curious, you peer into the hole in the wall. There's a large hole where the\nceiling used to be, and all of the heroes appear to have left. Fury is the only one in the room.\nYou really, really don't want to confront an angry Nick Fury, so you leave him to rant in peace."
                file.write("Furious - scared off by Fury")
            else:
                s += "You aren't going back to that room, or what's left of it, anyway. If Fury being furious is enough to chase off a team of superheroes,\nthat probably means it should chase you off too."
    elif "restroom" in room: #this isn't all of them, and this isn't right
        if "200" in room:
            s += "A regular restroom. There's a full length mirror on the opposite side of the wall you see when you first enter, several smaller mirrors above the sinks, and toilets. It's a restroom." #pretty sure the sides are basically the same
        elif "400" in room:
            if "female" in room:
                s += "A quote painted onto the wall when you first walk in tells everyone to be their own kind of beautiful. The left half of a jaguar's face stares at you from the far wall. When you spin around, there's a lady jag mural of a woman wearing a jean jacket. She has a crown floating above her head that quietly says, \"Queen.\""
            else: #male
                s += "On the right wall, there is a painting of a jaguar head. The remainder of the wall is black, blue, and green. By the exit is the word \"Jaguar\"."
        elif "600" in room:
            if "female" in room:
                s += "The wall is covered with black flower outlines. There's space in the middle of them. It looks like it's big enough for a mirror, and the word \"bloom\" is above that. A book is painted on the far wall with the words \"Don't be ashamed of your story. It will inspire others.\" painted on its pages. There's also the everylasting \"Be curious, not judgemental\" painted upon the wall. When you look down, you notice that the floors are really stained, for some reason. Ew."
            else: #male
                s += "The bricks say \"Humble Hustle Hard\", for some reason. A quote from Babe Ruth is also prominently displayed - \"It's hard to beat a person who never gives up.\""
        elif "1000" in room:
            if "female" in room:
                s += "This restroom is painted like the sky. There's a large mural of the sun and moon across from the sinks, and the words \"May the sun bring you happiness... May the moon help you dream.\" are painted around them. The area above the sinks is painted with the night sky, and it's kinda pretty, you suppose."
            else: #male
                s += "You step into the bathroom, but it's pitch black inside; you can't see anything. There's no source of light near the door, either, so you're out of luck. You leave, as spending time here is a waste of time." #this is what happens when my recon man won't do recon. inconvenient. there will be no flashlights in this game specifically so i don't have to write this room.
        elif "commons" in room:
            if "female" in room:
                s += "There's a mural of a cactus next to the trashcan. It tells you that you can do hard things. Above the mirrors are the words \"You are capable, loved, always enough.\" On the far wall is \"Be you tiful\" surrounded by what you think are chrysanthmums and roses."
            else: 
                s += "\"Why not go out on a limb?\" is the first thing you see. It's attached to an apple tree painted on the wall. By the trash can, there are mountains\nthat tell you that nothing worth doing is easy. The far wall has a world, and on top of it, there's some advice you take to heart: \"Be the change you want\nto see in the world.\"\n\"It's good advice,\" you think. The last wall is a light blue and says that it's never too late to be what you might have been. All in all, it's the most\npositive restroom you've ever been in."
        else: #100s and 900s
            s += "You push open the door of one of the single restrooms, then the other. There's nothing of interest inside. They're restrooms."
    elif "office" in room:
        if "main" in room:
            s += "The wall on the side door you entered from is about 27.5 hands away from the largest desk in the room. There are several other desks here, but that's unimportant;\nthe only desk that matters is the largest desk."
        elif "counselling" in room:
            s += "The first thing you see is an open door. It appears to lead into a filing room. You dart by some chairs and a large desk to peek into the room when you\nare tripped by a small wire. After falling flat on your face, you stop to look around. The whole area appears to be set up like something out of a heist film.\nThere are several open offices nearby. The only clear path appears to be the path to the main office, but you could probably scoot around the perimeter to the offices if you wanted to."
    elif "pac" in room:
        if "lobby" in room:
            s += "There are windows all along the west side of the area. To the northwest are two sets of doors leading to the PAC. There are two tall trashcans on either side\nof the windows."
        else:
            if 'hamlet' not in iInv:
                s += "There are rows upon rows of seats. They look new and comfortable, so you sit down in one.\nThey aren't as comfy as those new movie theater seats that all the nearby places seem to be getting, but they aren't awful either. You stand back up.\nA spotlight shines down on the stage, and the house curtain sways, creating a small gap in the middle.\nA man steps through and begins speaking. You creep closer to the stage before sitting down.\n\n\"Tis now the very witching time of night,\nWhen churchyards yawn and hell itself breathes out\nContagion to this world: now could I drink hot blood,\nAnd do such bitter business as the day\nWould quake to look on. Soft! now to my mother.\nO heart, lose not thy nature; let not ever\nThe soul of Nero enter this firm bosom:\nLet me be cruel, not unnatural:\nI will speak daggers to her, but use none;\nMy tongue and soul in this be hypocrites;\nHow in my words soever she be shent,\nTo give them seals never, my soul, consent!\"\n\nThe man huffs, slightly out of breath, before sharply turning and vanishing back behind the curtains. You stand and begin clapping."
            else:
                s += "There are rows upon rows of seats. They are new and somewhat comfortable, not as much as new movie theater seats.\nA spotlight shines down on the stage, and the house curtain sways as though someone is moving behind it."
    elif room == "tech room":
        s += "You step up the stairs just inside the door. At the top, there are a few spinny chairs. You sit down in one and begin to spin.\nWhile you're spinning, you see something of interest: a chest.\nThere's also something that looks like a soundboard, but out of a fear of breaking it, you don't want to touch it."
        if "spinny chair" not in inv:
            s += "\nYou decide to take a spinny chair. Why not?"
            inv += ["spinny chair"]
            beginningTime = dt.now()
    elif room == "backstage":
        s += "The man-who-performed-Hamlet should be back here, but he's not. There is, however, a skull sitting in what you think is center-stage. You pick it up. Poor\nYorick. You suddenly feel the urge to do a soliloquy, but you frown and push the desire aside. You put the skull back down. There's an exit in the left wing,\nbut when you go to open it, you discover that you can't push it open more than a crack. Weird; you know the theatre people use this during practices to keep\ncool, as all the lights shining down on the stage make it very hot. It should open. There's not much else of interest here, as you don't want to die by sandbag."
    elif room == "below stage":
        s += "All you can see, everywhere you look, is props. Props here, props there, props everywhere! With these (and the ability to make more, because what theatre\nwould be complete without its own... unique props that its participants made), you can be anything. Anything? you wonder. Anything, you assure yourself.rawinputAfter wandering around for about half an hour, you have found three different sets of items you like: a monarch's outfit, a sparkly mirror and some wicked\ngloves, and about seven baskets full of fake flowers."
    elif room == "catwalk":
        s += "On the floor is a mess of cables; it's like someone who had no idea what they were doing put all of this together. You're really high up. You through the only\ndoor you can see into the area where the spotlights are kept. You turn off the spotlight that was shining onto the stage. You look at the stage; it looks so\nempty now. You turn the spotlight back on, unable to stand the hollowness of the stage without anything on it."
    elif "gym" in room:
        if "small" in room:
            s += "There is a volleyball net set up in the middle of the room, and a volleyball is rolling toward you. You pick it up and serve it. You hit the net; you're no\nathlete. Angry, you kick the volleyball, and it shoots up and hits the ceiling, where it pops. When it touches down again, it's a flat blob."
        else: #big gym
            s += "Hula hoops are covering the floor, lined up one after the other. They touch, but they don't overlap. "
            if gym:
                s += "There's now a timer ticking down on the scoreboards.\nThere's over an hour left, but there's only an hour left, and while you're not sure what will happen when that hour runs out, you don't really want to find out either."
            else:
                s += "The scoreboards appear to be off when you glance up, but,\nwhen you take a closer look, you realize they're just not displaying anything."
    elif "equipment" in room: #equipment room
        s += "The very pillars of sports are stored here; everywhere around you is equipment that can be used in sports. In one corner of the room is an odd, blue-blinking\nmachine. It is hooked up to the scoreboards in the gym, and it causes good ol' Mr. Michael a lot of trouble."
    elif room == "clinic":
        s += "There are two beds in here, curtains drawn back so you can see them. In the corner is an entrance to a bathroom, but you pop your head in and don't see anything special, so it'd be a waste of time to go in there."
    elif "lounge" in room: #teacher lounge
        s += "There are full-size, non-diet, non-zero Coke machines in here! You walk up to one and punch it, and out falls a Coke. Must be your lucky break; you only wish\nit hadn't been wasted on a Coke."
    elif "photography" in room:
        if "mathis" in room:
            s += "You're not quite sure what you expected, but it definitely wasn't a jammed door. It seems inconvenient to have a room that you can't get into, but that's just\nthe way it is, you suppose."
        else: #baker's photo lab
            s += "There are 18 Apple MACs in here. Next to them rests a set of cabinets that take up half the wall. Two windows look into Baker's room."
    elif room == "commons":
        s += "You feel strange walking into a commons that is so empty. Your steps echo as you look across the space, doing nothing to ease your anxieties about Davis.\"You\nshouldn't spend much time here,\" you think to yourself in second person for some odd reason. You're right, for once. There is no place to hide here, and there\nare lots of rooms to check, so best be on your way and out of this desolate space."
    elif room == "kitchen":
        if "corn" not in inv:
            s += "There are a bunch of stations in the middle of the scramble. The only one that has any food is the french fry one, and underneath the warming light is a\nsingular piece of corn."
        else:
            s += "There are a bunch of stations in the middle of the scramble. They're all empty, completely spotless."
    elif room == "concessions":
        if "starburst" not in iInv:
            s += "The gate of the concessions stand is open, and your eyes immediately lock onto one of the products: Starbursts. There are four packages of them left, and you vault over the counter and grab them, hurriedly unwrapping them. All of the Starbursts are yellow. You make a sound of disgust before grabbing the next packet. Same deal. The next two also contain all yellows. You scoot back over the counter, irritated beyond measure."
            iInv += ["starburst"]
        else:
            s += "The gate of the concessions stand is open. Scattered across the floor and counter are yellow Starbursts."
    elif "band" in room: #band locker room
        s += "The walls are made of lockers. None of them are locked, for some reason, so you can investigate all 100 something of them if you'd like. Why you'd waste that\nmuch time, I, the omnipresent yet not omnipotent narrator, will never know, but that's not my problem either."
    elif "locker" in room:
        if "down" in room:
            if "female" in room:
                s += "Ah, the fancy big locker room. There are lockers here, lockers there, lockers everywhere. Cool."
            else: #male
                s += "Ah, the fancy big locker room. There are lockers here, lockers there, lockers everywhere. Cool."
        else: #upstairs
            if "female" in room:
                s += "This locker room is used for both tornado shelters and regular class. As such, there's a smell in the air, and while it could be sweat, you think it's the suffering of those who didn't want to take gym."
            else: #male
                s += "This locker room is used for both tornado shelters and regular class. As such, there's a smell in the air, and while it could be sweat, you think it's the suffering of those who didn't want to take gym."
    elif room == "weight room":
        s += "There's equipment everywhere. The smell of sweat has seeped into the walls, and you know instinctively that this room can never be used for anything else ever\nagain.\n\nA suspicious stain peeks out from under the rug. \"So the rumours are true,\" you think. \"Someone really did die here.\""
    else:
        if teach != "none":
            a = teach + " (" + room + "): "
        else:
            a = "(" + room + "):"
        if room[0] == "0":
            if room[2] == "1":
                if room == "001":
                    s = "As science classroom, there are lab stations around the room, equipped with sinks and drawers galore. "
                    if countPlant % 4 == 0:
                        s += "There is a large, leafy plant atop the teacher's desk\n."
                    elif countPlant % 4 == 1:
                        s += "There is a large, leafy plant above a set of cabinets.\n"
                    elif countPlant % 4 == 2:
                        s += "There is a large, leafy plant on the floor in the dead center\nof the room. "
                    else:
                        s += "There is a large, leafy plant in one of the sinks.\n"
                    s += "An empty bulletin board proudly displays nothing in the back of the classroom."
                    countPlant += 1
                else: #011
                    s = "This science classroom is atypical; there are counters along the outside edge, but there aren't stations for labs. Along the right wall, there are constructions\nof marshmellows held together with toothpicks; it looks like someone's teambuilding activities went well. There's a glass parrot hanging from the ceiling\nopposite the marshmellowscrapers, and below that are some shelves."
            elif room[2] == "2":
                s = "There appears to be a painting of a monkey in the back of the classroom, leaning up against the wall. Atop the cabinets rests a collection of rubber ducks of\nvarious outfits. A large flag proclaiming \"Chiefs\" hangs on a wall."
            elif room[2] == "3":
                s = "Behind the teacher's desk is a water dispenser. It appears to be on, so you grab a glass and get some. Refreshing. There is a fish tank next to it, but you\nknow instinctively that no fish has seen the inside of it for over a year. Atop the teacher's desk is a football lamp."
                if "empty water bottle" in inv:
                    s += "rawinputWait, you have a water bottle! You hurriedly fill it with the water dispenser."
                    inv.remove("empty water bottle")
                    inv += ["water bottle with water"]
            elif room[2] == "4":
                s = "This room is very brightly lit. It hurts your eyes a bit. Along the left wall, there's a bookcase without any shelving or items in it. Odd. There is also a\nbunch of animals. You suppose someone comes by to feed them on the weekends, as they all have fresh food and water. There's a snake named Horus closest to\nthe door, and a bearded dragon named Smaug, who really seems to love his food, and two corn snakes inhabit the far corner from the entrance."
            elif room[2] == "5":
                s = "On the right wall, there's a very large... you think it's a poster, so poster of our solar system. Next to that are pictures of students. Behind the desk\nare several weather posters. There are lab stations around the room, but they don't look recently used."
            elif room[2] == "6":
                s = "There is absolutely nothing distinctive about this room. There are four walls, sets of tables and lab stations, a periodic table of elements poster, cabinets,\nand a teacher's desk, but outside of that, it appears to be devoid of any life."
            elif room[2] == "7":
                s = "There's a giant container of tennis balls in the back of the classroom; maybe this teacher coaches tennis. There are several large plastic tubs as well,\nfilled with various items. They're covering two lab stations."
            elif room[2] == "8": #008
                s = "On the cabinets, there is a lot of art that has been drawn by kids. There are a lot of plants in the room. Not much else of note draws your eye."
            elif room[2] == "9":
                s = "This room smells really bad. It probably makes the rest of the room smell as well. This is the room in which organisms get dissected, and the scent appears\nto have permanently seeped into the walls, as you don't see anything that could have caused the stench. Upon the desk, there is a green plant. You're unsure\nif it's real or not, as it feels and looks like it could be both. You name it Schrodinger's plant."
            else: #010
                s = "There are wreaths all over the back counter. They take up a lot of space. Next to them are some skeleton models (like those half anatomy, half skin models),\nand they have something - you're not sure what, not being in an anatomy class yourself - that looks like bow ties at the throat level."
        elif room[0] == "1":
            if len(room) == 3:
                if room[2] == "1":
                    if room == "101":
                        s = "There's swimming decor around the room, so you suppose that this teacher must coach the swim team. Close to the door, there's a whiteboard with writing all\nover it. Your favorite is \"If ghosts haven't gone on because of unfinished business, what's Casper's unfinished business?\""
                    else: #111
                        s = "\"FUTURE BUSINESS LEADERS OF AMERICA\", a sign proclaims. There's a little Harry Potter doll on a silhouette of a house just across from the door. It's cute.\nThere is also a computer cart specifically for this classroom."
                elif room[2] == "2":
                    if room == "102":
                        s = "While the windows on the outside of the door are decorated with fabric of vaious fandoms, there's not much within the room itself; a poster of Einstein is\nessentially the only decoration."
                    else: #112
                        s = "Upon the wall is a poster with the names and faces of famous inventors and scientists. There is a very organized bookshelf, and above the flag near the door\nrests a block that says \"Please snow. I'm a teacher.\""
                elif room[2] == "3":
                    if room == "103":
                        s = "There are lights taped to the window next to the door. They're on, and you can't help but like them; they add a nice ambience. There's also an old TV in the\ncorner, one that has a built-in VHS player."
                    else: #113
                        s = "The posters within this room seem more apt for a history teacher than an English teacher, but to each their own, you suppose. There are noisemakers taped to\nthe bottom of the board opposite the door. Maybe you're imagining it, but you think you can feel the misery of students in the air."
                elif room[2] == "4":
                    s = "This room's decorated with streamers and balloons, for some reason - maybe they were celebrating a birthday? You're not sure, but that sounds reasonable.\nQuotes seem to be everywhere, now that you've gotten the party items out of the way; there's a map with a quote on it, a wall full of motivational quotes,\nsome small paintings resting on a bookshelf - lots of quotes. There's also a sign that proudly displays \"Polasek rhymes with classic.\""
                elif room[2] == "5":
                    if room == "105":
                        s = "Everywhere you look, there's either inspirational posters or there's Jag spirit stuff. Mixed between are some flowers."
                    else: #115
                        s = "The rooms display college decor. There's not much else here of interest."
                elif room[2] == "6":
                    s = "Right outside the room, there are several things stuck in the ceiling. It looks almost like someone failed to properly take something down, but you have no\nidea what - paper streamers, maybe? Anyway, you head inside. On the board, there's a tic-tac-toe board. Maybe you have time to play a game..."
                elif room[2] == "7":
                    if room == "107":
                        s = "The first thing you notice is that this teacher has a whiteboard wall. There are drawings all over it, but it's a whiteboard wall - that's cool. There are\nsmall Despicable Me minion erasers in a line on the side of the teacher's desk. Some of them have been drawn on. The area behind the teacher's desk is filled\nwith art from students. The left wall is composed of cabinets."
                    else: #117
                        s = "There is a veritable tonne of pictures of students on the cabinet next to the door. On the back whiteboard, there is a smiley face made of magnets. There is\na small, bright blue blue globe sitting on one of the desks."
                elif room[2] == "8":
                    s = "Fake plants reside in the corners of the room. Paper balls hang from the ceiling; you suppose they're... artistic. At the front of the classroom, there are\nrubber band balls hanging on the top of the whiteboard."
                elif room[2] == "9": 
                    s = "Neat art and self-esteem posters adorn the walls alongside each other. Next to the teacher's desk, there is a small plushie of Toothless from How to Train\nYour Dragon. There are two sizeable whiteboards here, and the scent of math oozes from them."
                else: #110
                    s = "The first thing you see is the Iron Man cutout on the wall. He has a speech bubble above his head, though there's nothing written in it currently. The only\nother things you really care about are the trophies at the back of the room and the Chiefs memorabilia."
            else:
                if room == "1001":
                    s = "On the wall across from the door, there are several flags mounted on tall poles. Upon the windowsill are trophies."
                elif room == "1003":
                    s = "Trophies are lined up on the windowsill. Along the right wall, there are lockers. They're small, but they could hold a purse or other small items. They're\nlocked with external combination locks."
                elif room == "1005":
                    s = "You thought you stepped into room 1005, but as all you can see around you is the night sky, regardless of where you look, you think you're probably wrong.\nYou blink harshly a couple of times, and the stars fade away to show an almost completely empty room. There is a teacher's desk in the center, but that's it."
                elif room == "1006" or room == "1007":
                    s = "The divider between 1006 and 1007 is open, so you guess that you're currently existing in both right now. There are several long, fancy wood-n-plastic tables,\nand there are rolling chairs right there to go along with them. You resist the temptation to roll around in one. There's a podium up at the front of the room"
                    if "speech1000" not in iInv:
                        s += ",\nand you stand behind it and survey your crowd. Small turn out today. You'll get them tomorrow. You clear your throat, preparing to give an impromptu speech, but\nyou choke before you can and start coughing. By the time you're finished, you've lost all desire to give a speech."
                        iInv += ["speech1000"]
                    else:
                        s += "."
                elif room == "1008":
                    s = "You're not sure what you were expecting, but it's just... an office. There's some padding from some sport lying around, but other than that, it's just an ordinary office. Nothing special."
                elif room == "1009": #fournier
                    s = "Fake plants reside in the corners of the room. Paper balls hang from the ceiling; you suppose they're... artistic. At the front of the classroom, there are\nrubber band balls hanging on the top of the whiteboard.\n\nWait, that's Palermo's room. Well, they look practically the same anyway. The only difference is the HISTORY POSTERS ALL OVER THE WALLS. Not much."
                elif room == "1010":
                    s = "You see a bunch of student art over the walls. You see textbooks lying around all opened to the same chapter... It looks like people are doing a bit of last\nminute book studying because, like everyone else, they never actually read the section they're about to be quizzed over."
                elif room == "1011":
                    s = "There's a Persian-style South rug hanging in the corner. There's a globe - imagine that, a history teacher who actually has their globe out. Despite being\nclean, the room seems messy back by the teacher's desk because papers are pinned by a single corner to the back wall."
                elif room == "1012":
                    s = "On the wall opposite the door, memorabilia for the University of Arkansas hangs. This classroom feels stagnant, for some reason, and you want to leave it as\nsoon as possible."
                elif room == "1013":
                    s = "By the door is a \"We can do it!\" poster, the wartime one with the lady on it. Around the room are various self-esteem and motivational posters. On the board\nis art from the teacher's World Religions class."
                elif room == "1014":
                    a = "Teacher Workroom"
                    s = "There's a mini fridge on the left side, alongside two microwaves and a toaster. Hurdles are stored here, for some reason, opposite the door. A stationary bike\nand a treadmill also happen to have found their homes here."
                elif room == "1015":
                    s = "Woah, so this is Senate Headquarters. You've never had a class in here, though; you never much liked psychology, did you? It's warm and inviting,\nand yet you feel there is a sense of efficiency to the room as well. You notice the posters on the wall, looking at big world problems like the Darfur genocide;\nsuddenly you aren't so sure about the whole \"senate corruption\" scandal. Someone kind works here, and you aren't sure they would allow that kind of behavior."
                    if "1015" in pencils:
                        s += "\nThe Senate Closet awaits you, if you so choose."
                    s += "\n\nOK, enough introspection, go do something already!"
                elif room == "1016":
                    s = "The back wall is COVERED in the numbers athletes get when they compete. Actually, all the walls are covered in them. In an effort to distract yourself from\nthe sheer inadequacy of yourself in the light of all of the numbers, your eyes fall upon an excerise ball under the front table. You happily bounce on it for\na few minutes before putting the ball back."
                elif room == "1017":
                    s = "There are two maps of Europe on the wall opposite the door. Hanging around the classroom are various flag - those of Japan, France, the Holy Roman Empire, the\nGerman Empire, and what you think is the British ensign, a flag used by the navy."
                elif room == "1018": #sapp
                    s = "The walls have \"lots of flags and other historical stuff,\" in the words of your... friend. Cool. Unexpected. Fresh. Lovin' it, badabababah."
                elif room == "1019":
                    s = "\"Traditional desks? Never heard of her,\" this room seems to say. The floor is wide open, marked in some places with tape. The left side of the classroom has a\nclass's worth of seats, the plastic kind that have metal rivets towards the top of the back. You can almost see the forensics kids here, performing in their\ndramatic duo or their reader's theatre."
                elif room == "1020":
                    s = "Across from the door are historical posters detailing major events in U.S. history. Next to the door stands a poster with the similarities between Abe Lincoln\nand JFK. On the cabinet resides art from students over the years."
                elif room == "1022":
                    s = "Sign up sheets are everywhere. They're on the tables, on the floors, on the teacher's desk, on the walls, on the ceiling, and, now that you've entered, on you.\nYou pick one up and another immedately replaces it. No open space can be left. You get a papercut from the sign up sheet you grabbed."
        elif room[0] == "2":
            if room[2] == "1":
                s = "This is the only classroom in the school that you've seen with dry wall, so it's weird. Computers line the walls. In the middle of the room, there's a cluster\nof 5 desks."
            elif room[2] == "2":
                s = "A few long tables are pushed together. They have chairs that appear to be comfier than normal chairs but not as comfy as they could be. They wouldn't be out\nof place in a library. The room itself is tiny. It's sort of homey, but only sort of; there are family pictures on the wall next to a list of jobs."
            elif room[2] == "4":
                s = "There are wheels in here, wheels for making ceramics. There are 16 tables and 3 doors, which is a lot of exits. The ceiling is fairly high, giving the room\na very open feeling."
        elif room[0] == "3":
            if room[2] == "1":
                if room == "301":
                    s = "There are windows in this room (!!!) that look out into the hallway. This is the only place that you know of where that happens, so it's definitely weird. It\nlooks really nice though. There are inspirational quotes on the right wall. Art projects hang from the ceiling."
                else: #321
                    s = "This room has windows on its right side, letting in some nice natural light. The room itself is decorated with typical English teacher stuff - grammar topics,\nmainly. The desks are arranged in groups of 4."
            elif room[2] == "2":
                if room == "302":
                    s = "The first thing you notice is a lava lamp-like object. It's a glowy water tube with bubbles in it, not exactly a lava lamp, but not super far off either. On\nthe floor nearby is a chalk board detailing the day's activities. It sits atop a rainbow rug."
                else: #312
                    s = "This room is tiny! A moon chair sits in the corner closest to the door, and you can almost see the ASL club members sitting there on Fridays, practicing\ntheir signs. A coffee pot is the centerpiece of this room."
            elif room[2] == "3":
                s = "The concrete floor here has shattered many a phone. There is a sink on the right side with places to wash hands. Shelves glore are on the left side of the\nroom. There is cardboard all along the front of the room."
            elif room[2] == "4": #recon
                if room == "304":
                    s = "Along the back wall are various paintings of landscapes. They're colorful, but you inherently distrust them because they're too ideal and in a school building."
                else: #314
                    s = "There are a TONNE of flowers on the back board. It's basically covered in small pink ones. The table on the right side has a small podium standing on it,\nand there's a curtain of sorts falling down around it. In the far corner of the classroom, there's a booknook."
            elif room[2] == "6":
                if room == "306":
                    s = "The desks in this room are in a U shape. The sides are very long. You notice that the room has a LOT of sports memorabilia. It'd be hard not to notice,\nactually."
                else: #316
                    s = "On the wall opposite the door, there is a string with a doll and some papers clothespinned to it. Upon the right wall, a colorful painting rests."
            elif room[2] == "7": #317 - no 307
                s = "Around the room are Christmas lights. Looks like this teacher keeps them up year round. They're off right now, but you could easily fix that. There's a\nfull-length poster of Napolean Dynamite on the wall next to the teacher's desk, and across the room is a poster of Hamlet. Several Shakespearean posters adorn the walls."
            elif room[2] == "8":
                if room == "308":
                    s = "The room looks, overall, rather clean. There's a collage board on the wall behind the teacher's desk. On the left wall, there are three different doors.\nBetween the first two doors is a shelving unit with plants and a globe on top."
                else: #318
                    s = "On the whiteboard is an advocating memo for Ecosia, a search engine that plants trees with the ad revenue. On the wall are quotes from King Arthur. They're\non cloths, which is strangely fitting. There are so. many. trophies in the far corner of the room that you wonder how long this guy has been teaching. The small\nones are on the small bookshelf, and the big ones are on the big bookshelf."
            elif room[2] == "9":
                if room == "309":
                    s = "You aren't sure this room has ever been used. It must have once been a computer room, judging by the tables. Yet, for some reason, you hear the quiet\nmelodies of Spotify's focus track.\nTo be honest, you've never even seen this teacher before, you just hear the friends you have in this class never have to do anything. Sounds like a class you\ncould excel at (finally)."
                else: #319
                    s = "There's not a lot of distinct things in here. A bulletin board rests across from the door. You get the impression that there used to be posters on the wall, but\nwhen you look, you don't see any."
            elif room[2] == "0":
                if room == "310": #thaller
                    s = "Pinned on the board in the back of room are several voodoo-looking creations; you're really not sure what they are. When you step forward to examine them,\na force repels you. Confused, you try again, only to get the same result."
                else: #320
                    s = "At the front of the classroom is a rolling cart. There's a stool next to it. Above the teacher's desk is a poster of Hemingway. There are two windows on the\nfar side of the classroom, and they're fairly sizeable, all things considered. Between them is a whiteboard. There's a small library on the wall opposite you."
        elif room[0] == "4":
            if room[2] == "3":
                s = "It's an open, airy art room. There are tables scattered throughout the room. A side table has colored pencils and markers. At the front of the room, there\nare drawers for art assignments."
            elif room[2] == "4":
                s = "There are computers along the wall; they have Photoshop on them. There are legitimate desks as well, but those are unimportant, as is the rest of the room."
            elif room[2] == "6":
                s = "Home base! The far corner of the room contains the Cartoon of the Day, drawn semi-daily by one John Layland! Across from it is where Thanos should be; it is\nnot, however, where he is. There are rubber ducks scattered around the classroom. Next to the teacher's desk - which contains some really odd things, like\na decapitated duck, a small handbook, a red 'n' plastic boogie board, the focus stick, and 'Nightmare Duck', a rubber duck with plastic babies glued to it -\nis an army of yellow rubber ducks. They're led by the purple Fairy Princess Duck. You turn to examine the Power Rangers DVD on the bulletin board, and when you\nturn back, Nightmare Duck is gone. The whiteboard has a 'debate' about Ecosia written on it, and various students have doodled on it. The left side of the\nboard has a giant covering with squares on it.\"DAVIS IS MISSING\" is written on the board, and you can't help but wish that was true; you could probably go home\nif it were."
            elif room[2] == "0": #410
                s = "Upon entering the room, you immediatley feel a combination of magic and suffering. Computers line the walls of this square room while shelves full of broken\nvex pieces. Doors to the wood shop and a mysterious closet catch your eye as you gaze around the sorry wasteland that is the nightmarish room. You've heard\nhorror stories about this place from your friends. Ok, not horror, just a lot of complaints and something about a bathroom.  Still, you're horrified to be\nin this place and shouldn't spend long here."
        elif room[0] == "5":
            if room[2] == "5": #515
                s = "You're surprised not only by the tile floor at your feet, but the absolute clutter of this room. You knew Ag people were weird but good lord, there's a lot\nof crap. Grow lamps, cabinets, animal diagrams, and a frikin back side of a heifer adorn the walls! Yeah, these guys are really weird. The twinkle lights give it\na nice, comfortable vibe at least. You've heard there is a secret passage somewhere in the room, but that might not end up being worth it."
            elif room[2] == "6": #516
                s = "There's a graph made with different colored rectangles on the back wall. You aren't sure what it's for. Along the back board is also a bunch of numbers, the\nkind athletes get when they compete."
            elif room[2] == "7": #517
                s = "Something smells good in this room. On one of the several counters is a fresh, steaming plate of... some type of food; you're unsure of exactly what it is. There are sinks, ovens, and stovetops around the room, and a basket of laundry sits in the corner."
            elif room[2] == "8": #518
                s = "So this is where the sewing room is. You must admit, you've never been in here before. There's fabric all over the tables, and small cubbies are used for storage under the cabinets. The room is cluttered, but it feels somewhat homey."
            elif room[2] == "9": #519
                s = "This is the room where the small children stay. It looks like a preschool inside. There's a drying rack for art and three sinks in the back of the classroom.\nAgainst the left wall is a tiny blue wooden chair. A nearby rug has an image on it of a highway surrounded by green grass."
            else: #520
                s = "Against the far wall is a crib. This must be the classroom that has the take-home babies, then. On the far left wall is a shelf with miscellaneous binders on it. It's very messy."
                if random.randint(1,100) == 42:
                    s += "rawinputThe take-home baby starts crying. You wince and decide to ignore it the best you can; this is absolutely not your class, so it is, therefore, not your problem either."
        elif room[0] == "6":
            if room[2] == "3": #recon all of these. they were closed.
                s = "This room is spacious and tidy; a bookshelf in the far corner is extremely neat and without a paper out of place, the rug before the tables matches the\nposters smartly, and the drapes above the whiteboard help seal the deal."
            elif room[2] == "5":
                s = "There are glass containers for merchandise along the floor. Actually, the entire room is filled with South merchandise. There are shirts hanging on the walls,\nblue and green decor, various snacks - well, that's not merch. Next to the cash-only register are two coolers."
            elif room[2] == "7":
                s = "A lava lamp rests on one of the many shelves in this room. You stare at it, fascinated, as the bubble slowly moves up before appearing to bounce off the top,\ndrifting downward."
            else: #609
                s = "So this is what a shop class looks like. Lots of tables and machines all over the place. Is that a plasma cutter? Ah, so cool. Why don't you just use one of\nthose on Davis? Right, federal court. Let's not do that again.....Right, the smell is weird here. Probably molten metal or something.  And it's all dirty\nand there's sheet metal all over the place. Deal with it."
        elif room[0] == "7": #716
            s = "Hanging above every station are outlets. The stations themselves are wooden tables. There's a similar design in the metal shop room. A chain-link fence\nseparates the room from the storage room. To get into the storage room would require a key."
        elif room[0] == "9":
            if room[2] == "2":
                if room == "902":
                    s = "The floor is a wrestling mat, essentially. You've only been inside this room once before, and it smells like sweat, so you'd rather not go in there again."
                else: #912 
                    s = "Las paredes de este extrano lugar estan cubiertas de carteles de Looney Tunes, mientras que las Pinatas cuelgan del techo. Una catapulta adorna el rincon de la\nsala y sientes que las paredes casi te gritan el lenguaje de la clase."
            elif room[2] == "3":
                if room == "903":
                    s = "You step into the room and are immediately overcome with a sense of drama. Shaking your head to snap yourself out of it, you travel up to the raised side\nof the room. A couch sits on the left side, but it's torn up in some parts. You plop down on it and pretend to be reading a book. You then stand up and, taking\nyour time, make your way across the stage, bumping into every piece of furntiure you can along the way and hopping comically in pain. Finished with your skit,\nyou sketch a bow and sit back down on the couch."
                else: #913
                    s = "This room is connected to a computer room, which, in turn, is connected to another teacher's classroom. It's used for journalism, you think, so that's not\nunexpected. There's a stack of the school's magazine, The Jag, on the front table. The classroom itself is very tidy."
            elif room[2] == "4":
                if room == "904":
                    s = "The floor is a wrestling mat, essentially. You've only been inside this room once before, and it smells like sweat, so you'd rather not go in there again."
                else: #914
                    s = "Il y a une kitchenette dans le coin qu'en face de toi, mais tu a un mauvais pressentiment. Il y a une roue coloree en le le tableau blanc, et tu veux le\ntourner. Autour de la piece, il y a les affiches lumineuses, mais tu ne les comprends pas. La piece est tres lumineuses, trop lumineuses. Tes yeux commencent\na faire mal, mais tu dois probablement enqueter en primer." #don't @ me for my mistakes
            elif room[2] == "5":
                if room == "905":
                    s = "This room is huge, one of the biggest in the school. There are instruments - stringed ones - lined up at the front of the classroom; this is clearly the\nmusic room. Along the back are a bunch of speakers and instruments. At the front stands a podium, slightly raised, where the conductor can conduct. Off to\nthe side are all of the chairs and stands the students use."
                else: #915
                    s = "Der Geruch von brutzelnde Bratwurste verschlingt die Sinne wie Sie seltsame Klassenzimmer betreten. Brezeln baumeln von der Decke und einen... Igel? Adler?\nsteht die Uhr auf einem Bucherregal quer durch den Raum. Das Klassenzimmer fuhlt sich warm und gemutlich, trotz des massiven Fensters deutlich drauBen im Schnee."
            elif room[2] == "6":
                if room == "906":
                    s = "A tiny room, within here stands a piano."
                else: #916
                    s = "Las paredes de este extrano lugar estan cubiertas de carteles de Looney Tunes, mientras que las Pinatas cuelgan del techo. Una catapulta adorna el rincon de la\nsala y sientes que las paredes casi te gritan el lenguaje de la clase."
            elif room[2] == "7":
                if room == "907":
                    s = "The choir room has a set of risers. Across from the risers are several posters detailing the scale the singers should sing. A piano sits in the middle of the room."
                else: #917
                    s = "Las paredes de este extrano lugar estan cubiertas de carteles de Looney Tunes, mientras que las Pinatas cuelgan del techo. Una catapulta adorna el rincon de la\nsala y sientes que las paredes casi te gritan el lenguaje de la clase."
            elif room[2] == "8":
                if room == "908":
                    s = "This is the room where Jag TV is shot. Along the left side are a bunch of computers where editing can be done. There's the desk where the anchors sit across\nfrom the door, not that you can see it from the door - there's a curtain blocking the way."
                else: #918
                    s = "Las paredes de este extrano lugar estan cubiertas de carteles de Looney Tunes, mientras que las Pinatas cuelgan del techo. Una catapulta adorna el rincon de la\nsala y sientes que las paredes casi te gritan el lenguaje de la clase."
            elif room[2] == "9":
                if room == "909":
                    s = "There are cabinets along the wall, capped off by the teacher's desk. A shelf is in the corner opposite the desk. Windows are on the back wall. The weather in\nthe computer lab seems to be nice."
                else: #919
                    s = "There are posters on the walls in various languages, and the bulletin board is boardered by flags on a cardboard border. Each computer - and the entire room\nis full of them - has a headphone and microphone set. There's a printer on one side as well. A set of four computers sit isolated in the center. For what\npurpose, you haven't the slightest, but they are there."
            elif room[2] == "0": #910
                s = "Ooh, the ISD room. There's nothing at all special or interesting about it, but you can smell both satisfaction and suffering of students here."
    file.close()
    return(a + "\n" + s)

def busted(end="none"):
    global inv, beginningTime
    if "Book of the Dead" in inv and end != "near":
        print("Just as Davis catches up to you - you're far enough away to see the light reflected off his head, but you're close enough that he could easily catch you\nbefore you could disappear - the Book of the Dead jumps out of your bag. It approaches Davis, who pauses, staring at it. You blink, and when you open your\neyes, you are in a different room, sans the Book of the Dead.")
        inv.remove("Book of the Dead")
        beginningTime = dt.now()
        pass
    else:
        b = random.choice(["He shakes his head, then says, \"I'm not mad. I'm just disappointed.\" He then turns around and walks away, fading from sight.", "\"CUT!\" The loud cry comes from somewhere over to your left. \"All right people, that's a wrap. Get some rest tonight!\"\nThere's a shuffling sound, then all the stage lights shut off. The only light around you is the dim light of the exit sign over an emergency door.\nYou shake your head. \"Okay,\" you say as you walk towards the door. \"Okay.\"", "The rest of the devs pop up behind you one by one. You look to your right and nod, then your left. Together, you and the other devs turn tail and run.\nYou see a light and point it out to the others, collectively running towards it.\nJust as you think you're home free, you hit a window, as does everyone else. What are you, a bird? Loser."])
        sys.exit("\nDavis has caught up with you!\n" + b + "\033[3;31;40m\n\nGAME OVER\n\n\033[0m")
    
def thanosAndCo(): #co would be powerups
    global allrooms, thanos#, powerups
    rooms = allrooms
    thanos = rooms.pop(random.randint(0, len(rooms)-1))
    '''for x in range(1, 3): #decide powerups and their indexes
        powerups += [rooms.pop(random.randint(0, len(rooms)-1))]'''
    #print powerups
    #print thanos
    #return [thanos, powerups]
    return thanos

def stones():
    global stone
    mind = random.choice(['204', '301', '302', '303', '304', '306', '404', '410', '403'])
    soul = random.choice(['902', '903', '907', '904', '905', '908', '909', '919', '918', '915', '914', '917', '916', '910', '913'])
    time = random.choice(['1019', '1020', '1016', '1022', '1010', '1014', '1018', '1012', '1009', '1008', '1007', '1006', '1005', '1017', '1003', '1011', '1001', '1013'])
    reality = random.choice(['308', '309', '319', '318', '603', '312', '609', '310', '317', '316', '519', '518', '320', '321', '520', '517', '716', '515', '607', '516'])
    space = random.choice(['010', '011', '117', '111', '110', '113', '112', '008', '003', '002', '108', '109', '007', '006', '005', '004', '102', '103', '009', '101', '106', '107', '104', '105', '115', '001'])
    stone = [mind, reality, soul, space, time]
    #print stone
    return stone
    
def beginTime():
    global beginningTime
    beginningTime = dt.now()

def elapsed():
    global beginningTime, iInv
    currTime = dt.now()
    second = beginningTime.hour*60*60 + beginningTime.minute*60 + beginningTime.second
    bT = td(days=beginningTime.day, seconds=second)
    second = currTime.hour*60*60 + currTime.minute*60 + currTime.second
    cT = td(days=currTime.day, seconds=second)
    elapse = cT-bT
    elapse = str(elapse).split(":")
    seconds = int(elapse[0])*60*60 + int(elapse[1])*60 + int(elapse[2])*60
    if name == "chad":
        o = 99999 #chad is our god
    elif name == "ryan":
        o = 1800 #30 minutes
    elif name == "nathan":
        o = 2100 #35 minutes
    elif name == "drew":
        o = 1980 #33 minutes
    elif name == "lindsey":
        o = 2280 #38 minutes
    elif name == "brendan":
        o = 2400 #40 minutes
    elif name == "caleb":
        o = 2580 #43 minutes
    else: #kylee and fight me i'm the main dev who knows where not to go
        if "timerGlitch" in iInv:
            o = 1500 #25 minutes
        else:
            o = 960 #16 minutes
    if seconds > o:
        busted()
    else:
        return str(o - seconds)

def writeLog(command): #log file keeps track of each VALID move you make; i cleared the screen in a way that cleared it permanently, so this is necessary for the user's sanity
    '''file = open("log.txt", "a")
    file.write(command+"\n")
    file.close()'''
    with open("log.txt", 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(command.rstrip('\r\n') + '\n' + content)

def removeLine():
    infile = open('log.txt','r').readlines()
    with open('log.txt','w') as outfile:
        for index,line in enumerate(infile):
            if index != 0:
                outfile.write(line)
