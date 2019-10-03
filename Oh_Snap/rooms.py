from functions import *
import time
import random
import subprocess as sp #i'm unsure of why i imported this
'''working title: oh snap
title options: oh snap, infinity school, oh snap i'm late for infinity school, davis no'''

pencils = 0 #for pencils
inventory = [pencils] #your stuff
internalInventory = [] #stuff that the user shouldn't be able to see but which allows for conditions
turns = 0 #won't be implemented for a while but exists
name = "" #character name. this is for turns and character quirks

def hall000():
    global inventory, internalInventory, pencils, turns
    c = "000"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m[1:] == "00":
        if m[0] == "2":
            return hall200()
        elif m[0] == "4":
            return hall400()
        else:
            return hall600()
    elif m == "library":
        return library()
    else:
        if m[1:] == "01":
            return room001()
        elif m[1:] == "02":
            return room002()
        elif m[1:] == "03":
            return room003()
        elif m[1:] == "04":
            return room004()
        elif m[1:] == "05":
            return room005()
        elif m[1:] == "06":
            return room006()
        elif m[1:] == "07":
            return room007()
        elif m[1:] == "08":
            return room008()
        elif m[1:] == "09":
            return room009()
        elif m[1:] == "10":
            return room010()
        else:
            return room011()
def room001():
    #stotts
    global inventory, internalInventory, pencils, turns
    c = "001"
    s = other(c, "Stotts")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory) #these technically don't need to be m, but they are because it was easier to mass find and replace instead of individually doing it
    return hall000()
def room002():
    #poertner and grice
    global inventory, internalInventory, pencils, turns
    c = "002"
    s = other(c,"Poertner and Grice")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall000()
def room003():
    #mooney
    global inventory, internalInventory, pencils, turns
    c = "003"
    s = other(c,"Mooney")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall000()
def room004():
    #heide
    global inventory, internalInventory, pencils, turns
    c = "004"
    s = other(c,"Heide")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall000()
def room005():
    #grigsby and shelby 
    global inventory, internalInventory, pencils, turns
    c = "005"
    s = other(c,"Grigsby and Shelby")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall000()
def room006():
    #sundberg
    global inventory, internalInventory, pencils, turns
    c = "006"
    s = other(c,"Sundberg")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall000()
def room007():
    #marshall
    global inventory, internalInventory, pencils, turns
    c = "007"
    s = other(c,"Marshall")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall000()
def room008():
    #barrett
    global inventory, internalInventory, pencils, turns
    c = "008"
    s = other(c, "Barrett")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall000()
def room009():
    #norman
    global inventory, internalInventory, pencils, turns
    c = "009"
    s = other(c,"Norman")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall000()
def room010():
    #balano
    global inventory, internalInventory, pencils, turns
    c = "010"
    s = other(c,"Balano")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall000()
def room011():
    #fritts
    global inventory, internalInventory, pencils, turns
    c = "011"
    s = other(c, "Fritts")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall000()


def hall100():
    global inventory, internalInventory, pencils, turns
    c = "100"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m[1:] == "00":
        if m[0] == "2":
            return hall200()
        elif m[0] == "4":
            return hall400()
        else:
            return hall600()
    elif "restroom" in m:
        return restroom100()
    else:
        if m[1:] == "01":
            return room101()
        elif m[1:] == "02":
            return room102()
        elif m[1:] == "03":
            return room103()
        elif m[1:] == "04":
            return room104()
        elif m[1:] == "05":
            return room105()
        elif m[1:] == "06":
            return room106()
        elif m[1:] == "07":
            return room107()
        elif m[1:] == "08":
            return room108()
        elif m[1:] == "09":
            return room109()
        elif m[1:] == "10":
            return room110()
        elif m[1:] == "11":
            return room111()
        elif m[1:] == "12":
            return room112()
        elif m[1:] == "13":
            return room113()
        elif m[1:] == "15":
            return room115()
        elif m[1:] == "17":
            return room117()
def room101():
    #oberlander
    global inventory, internalInventory, pencils, turns
    c = "101"
    s = other(c,"Oberlander")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room102():
    #frentrop
    global inventory, internalInventory, pencils, turns
    c = "102"
    s = other(c,"Frentrop")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room103():
    #mumaw
    global inventory, internalInventory, pencils, turns
    c = "103"
    s = other(c,"Mumaw")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room104():
    #polasek
    global inventory, internalInventory, pencils, turns
    c = "104"
    s = other(c,"Polasek")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room105():
    #wilbers
    global inventory, internalInventory, pencils, turns
    c = "105"
    s = other(c,"Wilbers")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room106():
    #christian
    global inventory, internalInventory, pencils, turns
    c = "106"
    s = other(c,"Christian")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room107():
    #dorsch    =D
    global inventory, internalInventory, pencils, turns
    c = "107"
    s = other(c,"Dorsch")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room108():
    #palermo
    global inventory, internalInventory, pencils, turns
    c = "108"
    s = other(c,"Palermo")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room109():
    #barnett
    global inventory, internalInventory, pencils, turns
    c = "109"
    s = other(c,"Barnett")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room110():
    #estep
    global inventory, internalInventory, pencils, turns
    c = "110"
    s = other(c,"Estep")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room111():
    #smith
    global inventory, internalInventory, pencils, turns
    c = "111"
    s = other(c,"Smith")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room112():
    #raouf
    global inventory, internalInventory, pencils, turns
    c = "112"
    s = other(c,"Raouf")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room113():
    #daily
    global inventory, internalInventory, pencils, turns
    c = "113"
    s = other(c,"Daily")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room115():
    #williams
    global inventory, internalInventory, pencils, turns
    c = "115"
    s = other(c,"Williams")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()
def room117():
    #schuberth
    global inventory, internalInventory, pencils, turns
    c = "117"
    s = other(c,"Schuberth")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall100()


def hall200():
    global inventory, internalInventory, pencils, turns
    c = "200"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m[1:] == "00":
        if m[0] == "0":
            return hall000()
        elif m[0] == "1":
            return hall100()
        else:
            return hall300()
    elif m == "main office":
        return mainOffice()
    elif m == "counselling office":
        return counsellingOffice()
    elif m == "lecture hall":
        return lectureHall()
    elif m == "gallery hall":
        return galleryHall()
    elif "lobby" in m:
        return lobbyPAC()
    elif m == "library":
        return library()
    elif m == "clinic":
        return clinic()
    elif "lounge" in m:
        return teacherLounge()
    elif "restroom" in m:
        if "female" in m:
            return restroomF200()
        else:
            return restroomM200()
    elif "gym" in m:
        return smallGym()
    else:
        if m[2] == "1":
            return room201()
        elif m[2] == "2":
            return room202()
        else:
            return room204()
def room201():
    #plato lab
    global inventory, internalInventory, pencils, turns
    c = "201"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall200()
def room202():
    #supportive services - holmes
    global inventory, internalInventory, pencils, turns
    c = "202"
    s = other(c,"Holmes")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall200()
def room204():
    #martin
    global inventory, internalInventory, pencils, turns
    c = "204"
    s = other(c,"Martin")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "200":
        return hall200()
    elif m == "303":
        return room303()
    elif m == "301":
        return room301()
    else:
        return room403()
def lectureHall():
    global inventory, internalInventory, pencils, turns
    c = "lecture hall"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall200()
    


def hall300():
    global inventory, internalInventory, pencils, turns
    c = "300"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m[1:] == "00":
        if m[0] == "2":
            return hall200()
        elif m[0] == "4":
            return hall400()
        else:
            return hall600()
    elif "photography" in m:
        return roomPhotoLab()
    elif "office" in m:
        return mainOffice()
    else:
        if m[1:] == "01":
            return room301()
        elif m[1:] == "02":
            return room302()
        elif m[1:] == "03":
            return room303()
        elif m[1:] == "04":
            return room304()
        elif m[1:] == "06":
            return room306()
        elif m[1:] == "08":
            return room308()
        elif m[1:] == "09":
            return room309()
        elif m[1:] == "10":
            return room310()
        elif m[1:] == "12":
            return room312()
        elif m[1:] == "14":
            return room314()
        elif m[1:] == "16":
            return room316()
        elif m[1:] == "17":
            return room317()
        elif m[1:] == "18":
            return room318()
        elif m[1:] == "19":
            return room319()
        elif m[1:] == "20":
            return room320()
        else:
            return room321()
def room301():
    #martin
    global inventory, internalInventory, pencils, turns
    c = "301"
    s = other(c,"Martin")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "300":
        return hall300()
    elif m == "303":
        return room303()
    elif m == "204":
        return room204()
    else:
        return room403()
def room302():
    #dowler and holmes
    global inventory, internalInventory, pencils, turns
    c = "302"
    s = other(c,"Dowler and Holmes")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room303():
    #baker
    global inventory, internalInventory, pencils, turns
    c = "303"
    s = other(c,"Baker")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "300":
        return hall300()
    elif m == "301":
        return room301()
    elif m == "204":
        return room204()
    else:
        return room403()
def roomPhotoLab():
    #next door to baker
    global inventory, internalInventory, pencils, turns
    c = "photography lab"
    
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room304():
    #black and crabtree
    global inventory, internalInventory, pencils, turns
    c = "304"
    s = other(c,"Black and Crabtree")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room306():
    #schibi and vandevent
    global inventory, internalInventory, pencils, turns
    c = "306"
    s = other(c,"Schibi and Vandevent")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room308():
    #leonard and rehkow
    global inventory, internalInventory, pencils, turns
    c = "308"
    s = other(c,"Leonard and Rehkow")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room309():
    #schmelzle
    global inventory, internalInventory, pencils, turns
    c = "309"
    s = other(c,"Schmelzle")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room310():
    #thaller
    global inventory, internalInventory, pencils, turns
    c = "310"
    s = other(c,"Thaller")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room312():
    #alonzo
    global inventory, internalInventory, pencils, turns
    c = "312"
    s = other(c,"Alonzo")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room314():
    #bertrand
    global inventory, internalInventory, pencils, turns
    c = "314"
    s = other(c,"Bertrand")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room316():
    #morrow
    global inventory, internalInventory, pencils, turns
    c = "316"
    s = other(c,"Morrow")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room317():
    #sheridan
    global inventory, internalInventory, pencils, turns
    c = "317"
    s = other(c,"Sheridan")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room318():
    #esch
    global inventory, internalInventory, pencils, turns
    c = "318"
    s = other(c,"Esch")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room319():
    #goebel
    global inventory, internalInventory, pencils, turns
    c = "319"
    s = other(c,"Goebel")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room320():
    #strait
    global inventory, internalInventory, pencils, turns
    c = "320"
    s = other(c,"Strait")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()
def room321():
    #montgomery
    global inventory, internalInventory, pencils, turns
    c = "321"
    s = other(c,"Montgomery")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall300()


def hall400():
    global inventory, internalInventory, pencils, turns
    c = "400"
    
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m[1:] == "00":
        if m[0] == "0":
            return hall000()
        elif m[0] == "1":
            return hall100()
        elif m[0] == "3":
            return hall300()
        else:
            return hall700()
    elif m == "gallery hall":
        return galleryHall()
    elif "restroom" in m:
        if "female" in m:
            return restroomF400()
        else:
            return restroomM400()
    elif m == "commons":
        return commons()
    elif "gym" in m:
        return smallGym()
    else:
        if m[2] == "3":
            return room403()
        elif m[2] == "4":
            return room404()
        elif m[2] == "6":
            return room406()
        else:
            return room410()
def room403():
    #avery
    global inventory, internalInventory, pencils, turns
    c = "403"
    s = other(c,"Avery")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "400":
        return hall400()
    elif m == "303":
        return room303()
    elif m == "204":
        return room204()
    else:
        return room301()
def room404():
    #wisner
    global inventory, internalInventory, pencils, turns
    c = "404"
    s = other(c,"Wisner")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall400()
def room406():
    #DAVIS
    global inventory, internalInventory, pencils, turns
    c = "406"
    s = other(c,"Davis")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall400()
def room410():
    #messick
    global inventory, internalInventory, pencils, turns
    c = "410"
    s = other(c,"Messick")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall400()


def hall500():
    global inventory, internalInventory, pencils, turns
    c = "500"
    
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m[1:] == "00":
        return hall600()
    else:
        if m == "515":
            return room515()
        elif m == "516":
            return room516()
        elif m == "517":
            return room517()
        elif m == "518":
            return room518()
        elif m == "519":
            return room519()
        elif m == "520":
            return room520()
def room515():
    #zwahlen
    global inventory, internalInventory, pencils, turns
    c = "515"
    s = other(c,"Zwahlen")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall500()
def room516():
    #lucas
    global inventory, internalInventory, pencils, turns
    c = "516"
    s = other(c,"Lucas")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall500()
def room517():
    #cooking; none
    global inventory, internalInventory, pencils, turns
    c = "517"
    
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall500()
def room518():
    #mckiddy
    global inventory, internalInventory, pencils, turns
    c = "518"
    s = other(c,"McKiddy")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall500()
def room519():
    #hall
    global inventory, internalInventory, pencils, turns
    c = "519"
    s = other(c,"Hall")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall500()
def room520():
    #mckiddy
    global inventory, internalInventory, pencils, turns
    c = "520"
    s = other(c,"McKiddy")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall500()


def hall600():
    global inventory, internalInventory, pencils, turns
    c = "600"
    
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m[1:] == "00":
        if m[0] == "0":
            return hall000()
        elif m[0] == "1":
            return hall100()
        elif m[0] == "3":
            return hall300()
        elif m[0] == "5":
            return hall500()
        else:
            return hall700()
    elif "restroom" in m:
        if "female" in m:
            return restroomF600()
        else:
            return restroomM600()
    else:
        if m == "603":
            return room603()
        elif m == "605":
            return room605()
        elif m == "607":
            return room607()
        else:
            return room609()
def room603():
    #renee and marshall
    global inventory, internalInventory, pencils, turns
    c = "603"
    s = other(c,"Renee and Marshall")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall600()
def room605():
    #jag den
    global inventory, internalInventory, pencils, turns
    c = "605"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall600()
def room607():
    #ray
    global inventory, internalInventory, pencils, turns
    c = "607"
    s = other(c, "Ray")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall600()
def room609():
    #gran and zwahlen
    global inventory, internalInventory, pencils, turns
    c = "609"
    s = other(c,"Gran and Zwahlen")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall600()


def hall700():
    global inventory, internalInventory, pencils, turns
    c = "700"
    
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m[1:] == "00":
        if m[0] == "4":
            return hall400()
        else:
            return hall600()
    elif m == "gallery hall":
        return galleryHall()
    elif m == "commons":
        return commons()
    elif m == "kitchen":
        return kitchen()
    else:
        return room716()
def room716():
    #zwahlen
    global inventory, internalInventory, pencils, turns
    c = "716"
    s = other(c,"Zwahlen")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall700()


def library():
    #library
    global inventory, internalInventory, pencils, turns
    c = "library"
    
    inventory += ["Harry Potter and the Half-Blood Prince"]
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "200":
        return hall200()
    elif m == "000":
        return hall000()
    elif "lab" in m:
        return libraryLab()
    elif "office" in m:
        return libraryOffice()
    else:
        return libraryConference()
def libraryLab():
    #library lab 1 & 2
    global inventory, internalInventory, pencils, turns
    c = "library lab"
    
    if "staggeringBeauty" not in internalInventory:
        internalInventory += ["staggeringBeauty"]
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return library()
def libraryOffice():
    #office of mr. smith, as well as that area across from the computers and between the bookcases
    global inventory, internalInventory, pencils, turns
    c = "library office"
    
    if "blueRollPaper" not in internalInventory:
        internalInventory += ["blueRollPaper"]
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return library()
def libraryConference():
    global inventory, internalInventory, pencils, turns
    c = "library conference"
    
    furious = 0
    for each in internalInventory:
        if each == "fury":
            furious += 1
    if furious < 2:
        internalInventory += ["fury"]
    if furious > 2:
        internalInventory += ["furious"]
    return library()


def galleryHall():
    global inventory, internalInventory, pencils, turns
    c = "gallery hall"
    
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "200":
        return hall200()
    elif m == "400":
        return hall400()
    elif m == "700":
        return hall700()
    elif m == "commons":
        return commons()
    else:
        return lobbyPAC()

def lobbyPAC():
    global inventory, internalInventory, pencils, turns
    c = "pac lobby"
    
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "pac":
        return pac()
    elif m == "200":
        return hall200()
    elif m == "900":
        return hall900()
    elif m == "gallery hall":
        return galleryHall()
    elif m == "big gym":
        return bigGym()
    else:
        return smallGym()
def pac():
    global inventory, internalInventory, pencils, turns
    c = "pac"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if "hamlet" not in internalInventory:
        internalInventory += ["hamlet"]
    if "lobby" in m:
        return lobbyPAC()
    elif "backstage" in m:
        return backstage()
    else:
        return belowStage()
def techRoom(): 
    #p sure this is the sound booth but eh
    global inventory, internalInventory, pencils, turns
    c = "tech room"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return lobbyPAC()
def backstage():
    global inventory, internalInventory, pencils, turns
    c = "backstage"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "900":
        return hall900()
    elif m == "catwalk":
        return catwalk()
    else:
        return pac()
def catwalk():
    global inventory, internalInventory, pencils, turns
    c = "catwalk"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return backstage()
def belowStage():
    global inventory, internalInventory, pencils, turns
    c = "below stage"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "1000":
        return hall1000()
    else:
        return pac()


def smallGym():
    global inventory, internalInventory, pencils, turns
    c = "small gym"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "200":
        return hall200()
    elif m == "400":
        return hall400()
    else:
        return lobbyPAC()
def bigGym():
    global inventory, internalInventory, pencils, turns
    c = "big gym"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "1000":
        return hall1000()
    elif m == "pac lobby":
        return lobbyPAC()
    elif m == "commons":
        return commons()
    elif "equipment" in m:
        return equipmentRoom()
    elif "female" in m:
        return upFLocker()
    else:
        return upMLocker()
def equipmentRoom():
    global inventory, internalInventory, pencils, turns
    c = "equipment room"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "commons":
        return commons()
    else:
        return bigGym()


def commons():
    global inventory, internalInventory, pencils, turns
    c = "commons"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if len(m) == 3:
        if m == "400":
            return hall400()
        elif m == "700":
            return hall700()
        else:
            return hall900()
    elif "fame" in m:
        return hallOfFame()
    elif "equipment" in m:
        return equipmentRoom()
    elif "gym" in m:
        return bigGym()
    elif "gallery" in m:
        return galleryHall()
    elif m == "kitchen":
        return kitchen()
    elif m == "concessions":
        return concessions()
    elif "female" in m:
        return restroomFCommon()
    else:
        return restroomMCommon()
def kitchen():
    global inventory, internalInventory, pencils, turns
    c = "kitchen"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "700":
        return hall700()
    else:
        return commons()
    
def concessions():
    global inventory, internalInventory, pencils, turns
    c = "concessions"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return commons()


def hallOfFame():
    global inventory, internalInventory, pencils, turns
    c = "hall of fame"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return commons()



def hall900():
    global inventory, internalInventory, pencils, turns, name
    c = "900"
    if "introB" not in internalInventory:
        raw_input("\n\nThe hallways are quiet this...um...Saturday morning? Your phone died around midnight, and you aren't really that good at remembering, well, anything, without it.\nMaybe that's why you have such bad gra-and would you look at that, you can go multiple ways in this hallway.\nThe world's your oyster as you can choose to go to any of the following:\n")
        print "\n\n[just type the number/name of the room you would like to go to]\n[if you want to view commands you can use, type \"help\"]"
        internalInventory += ["introB"]
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if len(m) == 4:
        return hall1000()
    elif "restroom" in m:
        return restroom900()
    elif "band" in m:
        return bandLocker(name)
    elif "stage" in m:
        return backstage()
    elif m == "commons":
        return commons()
    elif "lobby" in m:
        return lobbyPAC()
    else:
        if m[1:] == "02":
            return room902()
        elif m[1:] == "03":
            return room903()
        elif m[1:] == "04":
            return room904()
        elif m[1:] == "05":
            return room905()
        elif m[1:] == "07":
            return room907()
        elif m[1:] == "08":
            return room908()
        elif m[1:] == "09":
            return room909()
        elif m[1:] == "10":
            return room910()
        elif m[1:] == "13":
            return room913()
        elif m[1:] == "14":
            return room914()
        elif m[1:] == "15":
            return room915()
        elif m[1:] == "16":
            return room916()
        elif m[1:] == "17":
            return room917()
        elif m[1:] == "18":
            return room918()
        else:
            return room919()
def room902():
    #wrestling
    global inventory, internalInventory, pencils, turns
    c = "902"
    s = other(c)
    
    return hall900()
def room903():
    #haynes
    global inventory, internalInventory, pencils, turns
    c = "903"
    s = other(c,"Haynes")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()
def room904():
    #wrestling
    global inventory, internalInventory, pencils, turns
    c = "904"
    s = other(c)
    
    return hall900()
def room905():
    #band/orchestra
    global inventory, internalInventory, pencils, turns
    c = "905"
    s = other(c,"Hansen and Mitchell")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()
def room906():
    #bean special - i think there's a piano in here, but i'm not entirely sure.
    global inventory, internalInventory, pencils, turns
    c = "906"
    s = other(c,"Bean")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return room907() #can't get to 900 hall from here.
def room907():
    #bean
    global inventory, internalInventory, pencils, turns
    c = "907"
    s = other(c,"Bean")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "906":
        return room906()
    else:
        return hall900()
def room908():
    #grigsby and jag tv
    global inventory, internalInventory, pencils, turns
    c = "908"
    s = other(c,"Grigsby")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()
def room909():
    #mathis
    global inventory, internalInventory, pencils, turns
    c = "909"
    s = other(c,"Mathis")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "900":
        return hall900()
    else:
        return roomPhotoLabMathis()
def roomPhotoLabMathis():
    global inventory, internalInventory, pencils, turns
    c = "mathis's photography lab"
    s = other(c)
    
    return room909()
def room910():
    #fansher and isd
    global inventory, internalInventory, pencils, turns
    c = "910"
    s = other(c,"Fansher")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()
def room912():
    #sanchez
    global inventory, internalInventory, pencils, turns
    c = "912"
    s = other(c,"Sanchez")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()
def room913():
    #mccleary
    global inventory, internalInventory, pencils, turns
    c = "913"
    s = other(c,"McCleary")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()
def room914():
    #walton
    global inventory, internalInventory, pencils, turns
    c = "914"
    s = other(c,"Walton")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()
def room915():
    #trowbridge
    global inventory, internalInventory, pencils, turns
    c = "915"
    s = other(c,"Trowbridge")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()
def room916():
    #creek
    global inventory, internalInventory, pencils, turns
    c = "916"
    s = other(c,"Creek")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()
def room917():
    #laws
    global inventory, internalInventory, pencils, turns
    c = "917"
    s = other(c,"Laws")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()
def room918():
    #findley
    global inventory, internalInventory, pencils, turns
    c = "918"
    s = other(c,"Findley")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()
def room919():
    #foreign language lab
    global inventory, internalInventory, pencils, turns
    c = "919"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()
'''def bandParent():
    #i didn't add this to functions. can add once everything else is done. far as im concerned it can just be jam packed with parents and you can't set a foot inside.
    global inventory, internalInventory, pencils, turns
    c = "band parent"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall900()'''
def bandLocker(a): #intro done
    global inventory, internalInventory, pencils, name
    if "beginning" not in internalInventory:
        name = a
        turn(a)
        stones()
        thanosAndCo()
        #\033[38;5;(number) sets the text color
        #\033[48;5;(number) sets the background color
        time.sleep(2)
        tmp = sp.call('clear',shell=True)
        print(" --------------- \n|   " + "\033[38;2;255;230;203m\033[48;5;55mOh, Snap!" + "\033[0m   |\n --------------- ") #consider changing character colors to match stones, individually
        print("a text-based game by\n\033[38;5;48m\033[48;5;232m>Lindsey Clark\n\033[0m\033[48;5;202m>Megan Curry\n\033[0m\033[0;92;40m>Emily Johnson\n\033[0m\033[48;5;92m>Ryan Kramer\n\033[0m\033[48;5;124m\033[38;5;117m>Caleb Ridings\n\033[0m\033[48;5;0m\033[48;2;0;0;0m\033[38;2;0;184;0m>Tyler Unger\n\033[0m\033[48;5;201m>Kylee Willis\n\n\033[0mfeaturing the rampaging Mr. Davis\n\n\n")
        raw_input("Please extend your terminal to its maximum height and width. [press enter]")
        tmp = sp.call('clear',shell=True)
        raw_input("\nIt's a chilly December morning, and you just pulled a not quite legal allnighter in the low-reed locker.\nYou slowly regain consciousness to the sounds of something heavy hitting the floor at roughly 75 beats per minute. \nYou shift uncomfortably amongst what seems to be a bed of textbooks, review papers, and some stolen soda (which explains the taste of\nsundrop in your mouth). As you make a slight peek out of the locker, you catch a glimpse of what appears to be Mr. Davis stomping past you.\n")
        raw_input("\nHe seems angry, but you're not sure why.  It's rather terrifying if you're honest. You scan the physics notes you neglected to study last\nnight in search of answers.  Almost prophetically, you read Dorsch's joke for the assignment:\n\n\"You know what they say,'the only thing to stop a rampaging Davis is Thanos himself.'\"\n")
        raw_input("\nYou remember seeing a Thanos in Davis' room once, though who knows where it may be now (it was a wild night last night, after all).\nOne thing is clear, the low-reed locker is getting uncomfortable, and who knows what Davis will do if he finds you.\nYou'll have to find Thanos, it's surely the ONLY solution to your problem.  Looks like you're searching the school.\n")
        raw_input("\nNow, you've also heard stories that infinity stones have also been scattered across South. It may be a bit riskier, and you think Thanos will probably be\nenough to stop Davis, but you never know. Strange things like hidden endings might arise from collecting infinity stones, but the choice is yours on what to do\nnext.")
        raw_input("\nYou leave, cautiously checking that Davis isn't anywhere close by. You exit the band locker room.\n")
        internalInventory += ["beginning"]
        print("")
        return hall900()
    else:
        c = "band locker room"
        s = other(c)
        m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
        return hall900()



def hall1000():
    global inventory, internalInventory, pencils, turns
    c = "1000"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if len(m) == 3:
        return hall900()
    elif "restroom" in m:
        if "female" in m:
            return restroomF1000()
        else:
            return restroomM1000()
    elif "gym" in m:
        return bigGym()
    elif "locker" in m:
        if "female" in m:
            return downFLocker()
        else:
            return downMLocker()
    elif m == "weight room":
        return roomWeight()
    else:
        if m[2:] == "01":
            return room1001()
        elif m[2:] == "03":
            return room1003()
        elif m[2:] == "05":
            return room1005()
        elif m[2:] == "06":
            return room1006()
        elif m[2:] == "07":
            return room1007()
        elif m[2:] == "08":
            return room1008()
        elif m[2:] == "09":
            return room1009()
        elif m[2:] == "10":
            return room1010()
        elif m[2:] == "11":
            return room1011()
        elif m[2:] == "12":
            return room1012()
        elif m[2:] == "13":
            return room1013()
        elif m[2:] == "14":
            return room1014()
        elif m[2:] == "15":
            return room1015()
        elif m[2:] == "16":
            return room1016()
        elif m[2:] == "17":
            return room1017()
        elif m[2:] == "18":
            return room1018()
        elif m[2:] == "19":
            return room1019()
        elif m[2:] == "20":
            return room1020()
        else:
            return room1022()
def room1001():
    #cole
    global inventory, internalInventory, pencils, turns
    c = "1001"
    s = other(c,"Cole")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1003():
    #gonzales
    global inventory, internalInventory, pencils, turns
    c = "1003"
    s = other(c,"Gonzales")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1005():
    #oyler
    global inventory, internalInventory, pencils, turns
    c = "1005"
    s = other(c,"Oyler")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1006():
    #meeting room
    global inventory, internalInventory, pencils, turns
    c = "1006"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "1000":
        return hall1000()
    else:
        return room1007()
def room1007():
    #meeting room
    global inventory, internalInventory, pencils, turns
    c = "1007"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "1000":
        return hall1000()
    else:
        return room1006()
def roomWeight():
    #weights. oyler, cain, courter, terry
    global inventory, internalInventory, pencils, turns
    c = "weight room"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1008():
    #coaches' office
    global inventory, internalInventory, pencils, turns
    c = "1008"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1009():
    #fournier
    global inventory, internalInventory, pencils, turns
    c = "1009"
    s = other(c,"Fournier")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1010():
    #roberts
    global inventory, internalInventory, pencils, turns
    c = "1010"
    s = other(c,"Roberts")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1011():
    #plummer
    global inventory, internalInventory, pencils, turns
    c = "1011"
    s = other(c,"Plummer")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1012():
    #buffington
    global inventory, internalInventory, pencils, turns
    c = "1012"
    s = other(c,"Buffington")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1013():
    #ladd
    global inventory, internalInventory, pencils, turns
    c = "1013"
    s = other(c,"Ladd")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1014():
    #work room
    global inventory, internalInventory, pencils, turns
    c = "1014"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1015():
    #bubalo
    global inventory, internalInventory, pencils, turns
    c = "1015"
    s = other(c,"Bubalo")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1016():
    #unruh
    global inventory, internalInventory, pencils, turns
    c = "1016"
    s = other(c,"Unruh")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1017():
    #brush
    global inventory, internalInventory, pencils, turns
    c = "1017"
    s = other(c,"Brush")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1018():
    #sapp
    global inventory, internalInventory, pencils, turns
    c = "1018"
    s = other(c,"Sapp")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1019():
    #rucinski
    global inventory, internalInventory, pencils, turns
    c = "1019"
    s = other(c,"Rucinski")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1020():
    #oyler
    global inventory, internalInventory, pencils, turns
    c = "1020"
    s = other(c,"Oyler")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def room1022():
    #morrill
    global inventory, internalInventory, pencils, turns
    c = "1022"
    s = other(c,"Morrill")
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()


def upMLocker():
    global inventory, internalInventory, pencils, turns
    c = "up m locker"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return bigGym()
def downMLocker():
    global inventory, internalInventory, pencils, turns
    c = "down m locker"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def upFLocker():
    global inventory, internalInventory, pencils, turns
    c = "up female locker"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return bigGym()
def downFLocker():
    global inventory, internalInventory, pencils, turns
    c = "down female locker"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()



def mainOffice():
    global inventory, internalInventory, pencils, turns
    c = "main office"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "200":
        return hall200()
    elif m == "300":
        return hall300()
    elif "counsel" in m:
        return counsellingOffice()
    elif m == "clinic":
        return clinic()
    elif "lounge" in m:
        return teacherLounge()
    else: #ajsrtlgparti you people didnt finish your offices
    #fine.
    #ill finish them for you.
    #kudos to ryan and tyler (and myself)... and megan? i can't tell if megan's is done or not
    #it's not done, probably
        if "cb" in m:
            return offCB()
        elif "am" in m:
            return offAM()
        elif "bb" in m:
            return offBB()
        elif "sb" in m:
            return offSB()
        elif "do" in m:
            return offDO()
        elif "bl" in m:
            return offBL()
        elif "lp" in m:
            return offLP()
        elif "tk" in m:
            return offTK()
        elif "km" in m:
            return offKM()
        else:
            return offPB()
def offCB():
    #megan    thx dr.belt
    global inventory, internalInventory, pencils, turns
    if "his majesty dr belt" not in internalInventory:
        raw_input('You knock two times on the door to Dr. Belt\'s office and the door swings ajar slowly. It\'s heavier than you thought it would be, but the hinges are smooth and\nsilent.')
        raw_input('\nYour eyes are averted toward the floor in a sign of primal respect to your great principal Dr. Belt. You hear a deep, booming voice speak to you.')
        raw_input('\n"This is Dr. Belt your principal speaking. Enter."')
        raw_input('\nYou shuffle inside and shut the door behind you. Slowly, you raise your eyes to view Dr. Belt. He\'s sitting behind his office desk on a grand, gilded throne.\nIn the gleam of the LED lights in the drop ceiling above, you can see the shape of a cake engraved in the gold in a tessalating pattern.\nDr. Belt sits there on a purple goosefeather cushion, his pointy elbows resting on the soft arms of the throne, with his hands positioned in a power pose.')
        raw_input('\nHe\'s trying to assert his dominance over you.')
        raw_input('')
        raw_input('\nIt\'s working.')
        raw_input('')
        raw_input('\nSuddenly, a door you didn\'t even realize existed slams open to your left. You whirl around and see a black void beyond the dark mahogany. Out climbs a tall man,\nstooping down in order to fit through the door. He\'s wearing a green overcoat, yellow tights, and a pointy hat and shoes. He locks eyes with his majesty Dr. Belt in\na sign of equal footing, much to your own chagrin.')
        raw_input('\n"SANTA!" he cries in delight. He rushes up next to his majesty, dwarfing him in height. He seems oblivious to your presence in the room. That is fine.')
        raw_input("\nWhile his imperial majesty is distracted with the odd man, you leave the room, unnoticed by everyone.")
        internalInventory += ["his majesty dr belt"]
    else:
        raw_input("\nYou would prefer not to bother his illustriousness with your petty concerns.")
        file = open("achievements.txt", "w+")
        file.write("Annoying Peasant - attempted to bother his imperial and royal majesty with your concerns")
        file.close()
    return mainOffice()
def offAM():
    #emily yeeeeee
    global inventory, internalInventory, pencils, turns
    if 'Meirwynne' not in internalInventory:
        raw_input('The door creaks open as you step into the room. It is musty and dark.')
        raw_input("\nA small window in the right corner lets in a small trickle of light which appears to be leading you to a strange object in the opposite corner.")
        raw_input("\nYou're going to look at it aren't you? Curiosity killed the cat didn't it.") #satisfaction brought it back
        raw_input("\nAs you walk over, it appears to be a very large something draped in a sheet. (Don't ask me why it's there, I don't know) *sigh*")
        raw_input("\nYou want to take the sheet off? Of course you do.")
        raw_input("\nToo bad. You leave the sheet on, and you back out of the room. Whatever side quest you were about to go on is just not for you, not today.")
        internalInventory += ["Meirwynne"]
    else:
        raw_input("\nLook, I didn't sign up for making an entire quest, and I don't really have time for it right now. I'm not sure what Emily was going to write, but suffice to say\nit would have involved a world she wrote and a quest to obtain /something/. Davis wouldn't have been able to get you there. Unfortunately, I let this languish too\nlong and am unsure of how to get someone to write an entire quest in the wee hours of the morning so I have time to give this to Davis before I leave. You'll\njust have to live without knowing, I guess.\n\nCheers, Class of 2019.")
    return mainOffice()
def offCL():
    #caleb
    global inventory, internalInventory, pencils, turns
    raw_input("\nYou open the door cautiously, peering in with great anxiety (you've heard some of these offices are extremely elaborate and make you go on some quest or\nsomething).")
    raw_input("\n\nA hazy light creates a calming ambience as you step inside.  A great bookself full of all kinds of old literature and books on history and philosophy covers\nthe wall to your left. The name plate on the desk reads 'Danish Lenin' (what a stupid name, who cares about Denmark anyway). It looks like there's a hotel closet\nfull of...flannels? to your right.") #what... what were you going to do with this???
    return mainOffice()
def offBB():
    global inventory, internalInventory, pencils, turns
    raw_input("\nThe swings on its hinges, light as a feather, and without noise. On second thought, maybe there\'s not actually a door. Maybe you're just really tired...")
    raw_input("\nzzzzzzzzzzzz........")
    time.sleep(60)
    raw_input("\nzzzzzzzzzzzZZZZZZZZZZZZZZZZZzzzzzzzzzz......")
    time.sleep(15)
    raw_input("\n\'Wh-what? Oh, sorry. Anyway, badabing, badaboom, here ya go.\' Davis walks in.")
    busted()
    return hall900()
def offSB():
    global inventory, internalInventory, pencils, turns
    if "spiders" not in internalInventory:
        raw_input("\nThe smell of mildew hits you as soon as you open the door. This place has seen better days, like maybe during the 1940's. The furniture is barely holding\ntogether, with fabric missing from each of the three chairs. The paint is peeling off the walls, and there is an ungodly amount of spiderwebs hanging from\nthe ceiling in the corner. In your periphery, you see a giant shadow move, followed by the sound of multiple legs skittering around.")
        raw_input("\nFear sets in as you imagine Aragog and all his children waiting for their next meal. You \"Nope\" it out of there real quick.")
    else:
        raw_input("\nThat room is not a room you want to be in. You staunchly refuse to go back in there.")
    return mainOffice()
def offDO():
    #davis
    global inventory, internalInventory, pencils, turns
    if "mini laser sword keychain" not in inventory:
        raw_input("\nAs you open the door, a soft red glow from an unknown light source illuminates the office.  You notice a series of 8 widescreen computer monitors in a two row\nconfiguration on a nearly immaculate desk. There is a motivational poster hanging behind the desk. You can barely make out the text in the dim light, but you\ncould swear it says something like, \"Bald is beautiful.\" There is a modern high-backed office chair that would feel right at home in the office of a super villain.")
        raw_input("\nYou flip on the lights but nothing happens. You decide to investigate what is apparently the only souce of light. Behind a filing cabinet, you find the source: a\nreplica laser sword from some movie about ancient knights that took place long ago and far away.")
        raw_input("\nYou investigate the replica laser sword and notice a hidden compartment in the hilt. Within the hidden compartment, you discover after prying it open with a\npopsicle stick you found on the desk, is another mini laser sword, this one on a keychain. You decide to keep it as a memento.")
        inventory += ["mini laser sword keychain"]
        raw_input("\nThis room, while as \"cool\" as it is, weirds you out, so you decide to leave.")
    else:
        raw_input("\nAs you open the door, a soft red glow from a mini laser sword illuminates the office.  You notice a series of 8 widescreen computer monitors in a two row\nconfiguration on a nearly immaculate desk. There is a motivational poster hanging behind the desk. You can barely make out the text in the dim light, but you\ncould swear it says something like, \"Bald is beautiful.\" There is a modern high-backed office chair that would feel right at home in the office of a super villain.")
        raw_input("\nYou try to flip on the lights again but, again, nothing happens. Nothing has changed since the last time you were here. You want to leave, so you do.")
    return mainOffice()
def offBL():
    global inventory, internalInventory, pencils, turns
    if "The Swag." not in inventory:
        raw_input("\nThere appears to be an old-fashioned printing press here. A long roll of paper is being turned over a wheel, and it's being sliced and printed on as it goes.\nSurprisingly, none of the pages you can see are askew or otherwise messed up. You pick one of the finished copies up. It's of something called The Swag. You\nthought the school magazine was called The Jag, but perhaps you were wrong...")
        raw_input("\nNope, not wrong. This is somebody's spoof of the school's magazine, and it's quite funny. You decide to keep a copy.")
        inventory += ["The Swag."]
    else:
        raw_input("\nThere appears to be an old-fashioned printing press here. A long roll of paper is being turned over a wheel, and it's being sliced and printed on as it goes.\nSurprisingly, none of the pages you can see are askew or otherwise messed up. You pick one of the finished copies up. It's a black-and-white copy of the only\nedition of The Swag.")
    return counsellingOffice()
def offLP():#lindsey OR NOT YOU COULD ALSO JUST WRITE LITERALLY NOTHING AUDOGATHPA YOU PEOPLE
    global inventory, internalInventory, pencils, turns
    if "paper stream" not in internalInventory:
        raw_input("\nA paper slides out from underneath the door. It has a half typed sentence on it. You look back up at the door and shrug. Weird, but nothing dangerous. You open\nthe door. It's a good thing they open outward, as you never would have been able to open it inward.")
        raw_input("\nA veritable flood of papers comes out of the room. You're covered by them and flail about, attempting to surface. Eventually, the stream dies down a bit, and\nyou are able to poke your head above the topmost layer. You swim your way inside the room, swearing as you do that you'll never come to school again if your\nentire body is covered in paper cuts. You can't see anything in here. There's just paper after paper after paper, all of them on printer paper and all of them\nincomplete. Some of them have very, very few words on them, while others are mostly filled or half filled. These must be, you decide, unfinished essays. You\nweren't aware the school kept them; there's probably a few in here from you.")
        internalInventory += ["paper stream"]
    else:
        raw_input("\nYou swim your way inside the room, swearing as you do that you'll never come to school again if your entire body is covered in paper cuts. You can't see anything\nin here. There's just paper after paper after paper, all of them on printer paper and all of them incomplete. Some of them have very, very few words on them,\nwhile others are mostly filled or half filled. These must be, you decide, unfinished essays. You weren't aware the school kept them; there's probably a few in\nhere from you.")
    return counsellingOffice()
def offTK():
    #Ryan To code. Im literally TK. 
    global inventory, internalInventory, pencils, turns
    if "cubeEscape" not in internalInventory:
        raw_input("\nStepping into the office you just see a book case with scratch marks on the floor, which looks like that the book case has been moved multiple times.")
        raw_input("\nYou move the book case, and see a very deep stone stairwell heading down...")
        raw_input("\nGoing down the stairwell, you see 2 bookshelves and a very large cabinet at the bottom of the steps. In between the bookshelves is a small table, was a large class container on top.")
        raw_input("\nOne of the bookshelves is completely empty, each shelf divided into squares. The other bookshelf has a candle, a glass water jug, a bowl of dirt, and an air pump.")
        raw_input("\nYou walk over to the cabinet as you open it you see glass beakers with human body parts, all on different pedestals, you remove the beaker that has an eye in it, and the pedestal moves, like you are supposed to balance the beakers...")
        raw_input("\nSpending the next few minutes you balance the scales...  Suddenly on the middle pedestal, a black cube appears before you...")
        raw_input("\nAs you grab the Black Cube, you hear a deep voice say 'Welcome, To Rusty Lakes...")
        interalInventory += ['cubeEscape']
    else:
        print("This is not the place that it once was... All you see now is a normal office, only odd thing is a picture with a man that had an owl head.")
    return counsellingOffice()
def offKM():
    #dibs
    global inventory, internalInventory, pencils, turns
    global internalInventory
    
    if "twilightZone" not in internalInventory:
        raw_input("\n\"There is a fifth dimension beyond that which is known to man.\"")
        raw_input("\nYou step into the room, looking around. To your left, there's whiteboard wall with a desk pushed up against it.\nTo your right, there's a replication of the vast, unflinching infinity of space. Ahead of you, there's a window with a stunning view of a brick wall.")
        raw_input("\n\"It is a dimension as vast as space and as timeless as infinity.\"")
        raw_input("\nWhere is that voice coming from? You look around, but there's no obvious source. Slowly, you glance up.")
        raw_input("\n\"It is the middle ground between light and shadow, between science and superstition, and it lies between the pit of man's fears and the summit of his knowledge.\"")
        raw_input("\nThere's a speaker on the ceiling, but, standing underneath it, all you can hear is crackling static. You walk to the right, towards the star-filled void.")
        raw_input("\n\"This is the dimension of imagination. It is an area which we call...\"\nAn ominous thunderclap sounds overhead.")
        raw_input("\n\"the Twilight Zone.\"")
        raw_input("\nThe floor drops out from underneath you.")
        raw_input("\nRather than fall, you begin to float. You make swimming motions in the air frantically, trying to get back to the door, but nothing seems to be happening.")
        raw_input("\nYou try running instead of swimming. The door seems to get further and further away.")
        raw_input("\nYou shut your eyes for a few seconds in a long blink. When you open them, you appear to be in a different room.")
        internalInventory += ["twilightZone"]
    else:
        print("You don't want to go back in there; you don't know how you got out the first time, and you don't want to try getting out again.")
    return counsellingOffice()
def offPB():
    #i dunno who this is or if it's an office, but it's in the counselling office area.
    global inventory, internalInventory, pencils, turns
    raw_input("The FitnessGram PACER Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20-meter pacer test will begin in\n30 seconds. Line up at the start. The running speed starts slowly but gets faster each minute after you hear this signal: [beep]. A single lap should be completed\neach time you hear this sound: [ding]. Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the\nsound, your test is over. The test will begin on the word start. On your mark, get ready, start.")
    raw_input("You begin walking out of some previously unknown PTSD.")
    time.sleep(8.47)
    print("[ding]")
    time.sleep(8.47)
    print("[ding]")
    time.sleep(8.47)
    print("[ding]")
    time.sleep(8.47)
    print("[ding]")
    time.sleep(8.47)
    print("[ding]")
    time.sleep(8.47)
    print("[ding]")
    time.sleep(8.47)
    print("[beep]")
    #^7
    time.sleep(8)
    print("[ding]")
    time.sleep(8)
    print("[ding]")
    time.sleep(8)
    print("[ding]")
    time.sleep(8)
    print("[ding]")
    time.sleep(8)
    print("[ding]")
    time.sleep(8)
    print("[ding]")
    time.sleep(8)
    print("[ding]")
    time.sleep(8)
    print("[beep]")
    #^8
    time.sleep(7.58)
    print("[ding]")
    time.sleep(7.58)
    print("[ding]")
    time.sleep(7.58)
    print("[ding]")
    time.sleep(7.58)
    print("[ding]")
    time.sleep(7.58)
    print("[ding]")
    time.sleep(7.58)
    print("[ding]")
    time.sleep(7.58)
    print("[ding]")
    time.sleep(7.58)
    print("[beep]")
    #^8
    time.sleep(7.2)
    print("[ding]")
    time.sleep(7.2)
    print("[ding]")
    time.sleep(7.2)
    print("[ding]")
    time.sleep(7.2)
    print("[ding]")
    time.sleep(7.2)
    print("[ding]")
    time.sleep(7.2)
    print("[ding]")
    time.sleep(7.2)
    print("[ding]")
    time.sleep(7.2)
    print("[ding]")
    time.sleep(7.2)
    print("[beep]")
    #^9
    raw_input("\"Wait, why am I doing this?\" you wonder. \"I should stop.\"")
    return counsellingOffice()
def counsellingOffice():
    global inventory, internalInventory, pencils, turns
    c = "counselling office"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "heist" and "heist" not in internalInventory:
        raw_input("\nYou cautiously step forward. Below your foot, a tile lights up. It has the letter D on it. Frowning, you look at the tiles ahead of you. There are 8 rows, each\nwith different letters. You think you can spell out Davis with them, so you precariously reach with your other foot towards the nearest A, arms windmilling\nas you attempt to keep your balance. Your foot lands on the A, and the tile lights up. You push your weight onto that foot, lifting the other one, and reach\ntowards the V. It lights up, and you repeat the process with the I and the S. As nothing negative has happened, you decide you're probably right in that that\nwas what you needed to do. You quickly move off the tiles, relieved that you're done with that.")
        raw_input("\nYou look towards the next step in your attempted heist: criss-crossing laser beams. Honestly, you thought stuff like this only existed in movies. Fortunately for\nyou, it looks like there's enough of a gap at the bottom of the lasers that you can just roll through to the next area.")
        if random.randint(1,50) != 20:
            raw_input("\nYou made it through! Now you just have to get to the... book? It appears to be a boot, albeit a very old and worn one. It sits in a glass case, and you think\nyou can probably shatter the casing if you try hard enough.")
            x = "yes"
            while x == "yes" or x == "y":
                if random.randint(1, 20) != 3:
                    raw_input("\nYou shatter the glass. Avoiding the shards, you reach in and grab the book. It crumbles a bit in your hand, and you attempt to read the front of it. Unfortunately,\nit's not written in a language that you can understand, though you think it looks like it could be hieroglyphics. You decide it's the Book of the Dead,\nbecause that's fun.")
                    inventory += ["Book of the Dead"]
                    file = open("achievements.txt", "w+")
                    file.write("Director of the CIA")
                    file.close()
                    internalInventory += ["heist"]
                    break
                else:
                    x = raw_input("\nUnfortunately, you can't break through the glass. You can try again, but you're afraid that taking too long would allow Davis to catch up to you.\nWould you like to try again?\n").lower().strip()
            return counsel()
        else:
            raw_input("\nUnfortunately, you must have hit one of the beams, as there's now an alarm going off. You're preparing to try again when you realize Davis is standing off to\nthe side, tapping his foot.")
            busted()
    elif m == "200":
        return hall200()
    elif "main" in m:
        return mainOffice()
    elif "lounge" in m:
        return teacherLounge()
    else:
        if "cb" in m:
            return offCB()
        elif "am" in m:
            return offAM()
        elif "bb" in m:
            return offBB()
        elif "sb" in m:
            return offSB()
        elif "do" in m:
            return offDO()
        elif "bl" in m:
            return offBL()
        elif "lp" in m:
            return offLP()
        elif "tk" in m:
            return offTK()
        elif "km" in m:
            return offKM()
        else:
            return offPB()
def counsel(): #this was for the counselling office, as i had no idea how to restart it without... messing anything up.
    return counsellingOffice()
def clinic():
    global inventory, internalInventory, pencils, turns
    c = "clinic"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "200":
        return hall200()
    else:
        return mainOffice()
def teacherLounge():
    global inventory, internalInventory, pencils, turns
    c = "teacher lounge"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    if m == "200":
        return hall200()
    elif "main" in m:
        return mainOffice()
    else:
        return counsellingOffice()


def restroomM200():
    global inventory, internalInventory, pencils, turns
    c = "200 male restroom"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall200()
def restroomF200():
    global inventory, internalInventory, pencils, turns
    c = "200 female restroom"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall200()
def restroomM400():
    global inventory, internalInventory, pencils, turns
    c = "400 male restroom"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall400()
def restroomF400():
    global inventory, internalInventory, pencils, turns
    c = "400 male restroom"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall400()
def restroomM600():
    global inventory, internalInventory, pencils, turns
    c = "600 male restroom"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall600()
def restroomF600():
    global inventory, internalInventory, pencils, turns
    c = "600 female restroom"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall600()
def restroomFCommon():
    global inventory, internalInventory, pencils, turns
    c = "commons female restroom"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return commons()
def restroomMCommon():
    global inventory, internalInventory, pencils, turns
    c = "commons male restroom"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return commons()
def restroomF1000():
    global inventory, internalInventory, pencils, turns
    c = "1000 female restroom"
    s = other(c)
    m, inventory, internalInventory = tiny(c, s, inventory, internalInventory)
    return hall1000()
def restroomM1000():
    global inventory, internalInventory, pencils, turns
    c = "1000 male restroom"
    s = other(c)
    
    return hall1000()
def restroom900():
    global inventory, internalInventory, pencils, turns
    c = "900 restroom"
    s = other(c)
    
    return hall900()
def restroom100():
    global inventory, internalInventory, pencils, turns
    c = "100 restroom"
    s = other(c)
    
    return hall100()