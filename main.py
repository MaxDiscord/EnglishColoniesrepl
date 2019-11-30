import sys
import random
import time
wood = 0
clinic = False
food = 0
population = 10
water = 0
locx = 5
locy = 5
maxx = 9
maxy = 9
popmax = 0
turn = 1
birthturn = 1
season = 1
starvingturn = 0
foodperturn = 0

        
save = open ("kaigame.txt","r+")
havesave = input ("Do you have a save")
if havesave == "yes":
    readSave=save.read()
    splitSave =readSave.split("\n")
    population = int(splitSave[0])
    food=int(splitSave[1])
    wood=int(splitSave[2])
    clinic=bool(splitSave[3])
    townhall=bool(splitSave[4])
    foodperturn = int (splitSave[5])
    #naturemap
    naturemap = splitSave[6].split(",")
    naturemapbegin = naturemap[0].split("[")
    naturemap.insert(0,naturemapbegin[1])
    naturemapend = naturemap[81].split("]")
    naturemap.insert(81,naturemapend[0])
    #colonymap
    colonymap = splitSave[7].split(",")
    colonymapbegin = colonymap[0].split("[")
    colonymap.insert(0,colonymapbegin[1])
    colonymapend = colonymap[81].split("]")
    colonymap.insert(81,colonymapend[0])
else:
    pass
    
        
townhall = False
naturemap = [["Forest" for locx in range(maxx)] for y in range(maxy)]
naturemap[locx][locy] = "Plains"
colonymap = [["None" for locx in range(maxx)] for locy in range(maxy)]
berrymap = [["Berries" for locx in range(maxx)]for locy in range(maxy)]
print ("You have landed on a",naturemap[locx][locy],"tile. It looks like there is forest all around you")
print ("All",population," people that survived the journey voted and they voted to stay and make the colony here.")
while True:
    print ("Wood:",wood)
    print ("Food:",food)
    print ("Population:",population)
    print ("Water:",water)
    mainInput = input ("> ")
    if mainInput == "naturemap":
        for y in range(maxx):
            for x in range(maxy):
                if naturemap[x][y] == "Forest":
                    if y==locy and x==locx:
                        print ("X",end=" ")
                    else:
                        print ("x",end=" ")
                elif naturemap[x][y] == "Plains":
                    if y==locy and x==locx:
                        print ("U",end=" ")
                    else:
                        print ("u",end=" ")
            print("")
    elif mainInput == "gather water":
        water = water + 5
    elif mainInput == "colonymap":
        for y in range(maxx):
            for x in range(maxy):
                if colonymap[x][y] == "Town Hall":
                    if y==locy and x==locx:
                        print ("S",end=" ")
                    else:
                        print ("s",end=" ")
                elif colonymap[x][y] == "House":
                    if y==locy and x==locx:
                        print ("L",end=" ")
                    else:
                        print ("l",end=" ")
                elif colonymap[x][y] == "Farm":
                    if y==locy and x==locx:
                        print ("F", end=" ")
                    else:
                        print ("f", end= " ")
                elif colonymap[x][y] == "Clinic":
                    if y ==locy and x ==locx:
                        print ("H", end=" ")
                    else:
                        print ("h", end= " ")
                else:
                    if y==locy and x==locx:
                        print ("O",end= " ")
                    else:
                        print ("o", end = " ")
            print("")
    elif mainInput == ("w"):
        if locx>0:
            locx = locx - 1
        else:
            print("You can't go that way.")
    elif mainInput == ("e"):
        if locx<maxx-1:
            locx = locx + 1
        else:
            print("You can't go that way.")
    elif mainInput == ("n"):
        if locy>0:
            locy = locy - 1
        else:
            print("You can't go that way.")
    elif mainInput == ("s"):
        if locy<maxy-1:
            locy = locy + 1
        else:
            print("You can't go that way.")
    elif mainInput == ("gather wood"):
        if naturemap[locx][locy] == "Plains":
            print ("You cannot cut down wood on a plains tile")
        else:
            naturemap[locx][locy] = "Plains"
            wood = wood + 5
    elif mainInput == ("gather berries"):
        berrymap[locx][locy] = "None"
        food = food + 20
    elif mainInput == ("build"):
        build = input ("What do you want to build? ")
        if build == "town hall":
            wood = wood - 10
            colonymap[locx][locy] = "Town Hall"
        elif build == ("home"):
            wood = wood - 2
            colonymap[locx][locy] = "House"
            popmax = popmax + 10
        elif build == ("farm"):
            if naturemap[locx][locy] == "Forest":
                print ("You cannot build a farm here")
            else:
                colonymap[locx][locy] = "Farm"
                wood = wood - 1
                foodperturn = foodperturn + 10
                if food < population:
                    print ("People are starving")
                    print ("You have 3 turns to fix it")
                    starvingturn = starvingturn + 1
                    if starvingturn == 3:
                            print("You loose")
                            sys.exit()
        elif build == ("clinic"):
            clinic = True
            wood = wood - 10
            food = food / 2
            colonymap[locx][locy] = "Clinic"
    elif mainInput == "quit":
        saveet = input ("Do you want to save your game")
        if saveet == "yes":
            population = str(population)
            food = str(food)
            wood = str(wood)
            clinic = str(clinic)
            townhall = str(townhall)
            naturemap = str(naturemap)
            colonymap=str(colonymap)
            foodperturn=str(foodperturn)
            save.write(population)
            save.write("\n")
            save.write(food)
            save.write("\n")
            save.write(wood)
            save.write("\n")
            save.write(clinic)
            save.write("\n")
            save.write(townhall)
            save.write("\n")
            save.write(foodperturn)
            save.write("\n")
            save.write(naturemap)
            save.write("\n")
            save.write(colonymap)
            save.close()
            sys.exit()



    sick = random.randint(1,27)
    if sick == 21:
        print ("someone is sick")
        if clinic == True:
            print ("You have a clinic.")
            die = random.randint(1,6)
            if die == 3:
                print ("That person died :(")
                population = population - 1
            else:
                print ("He is no longer sick.")
        else:
            death = random.randint(1,2)
            if death == 2:
                print ("That person died")
                population = population - 1
            else:
                print ("He got lucky,he is no longer sick.")
    food = food - population
    food = food + foodperturn
    turn = turn + 1
    birthturn = birthturn + 1
    if birthturn == 10:
        population = population + 1
        birthturn = 1
        season = season + 1
    deadcrop = random.randint(1,30)
    if deadcrop == 5:
        food = food - foodperturn
        print ("Your crops died")
        if food < population:
            print ("People are starving")
            print ("You have 3 turns to fix it")
            starvingturn = starvingturn + 1
            if starvingturn == 3:
                    print("You loose")
                    sys.exit()
