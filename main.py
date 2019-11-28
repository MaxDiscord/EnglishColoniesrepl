import sys
import random
import time
wood = 0
food = 0
population = 10
water = 0
locx = 10
locy = 10
maxx = 20
maxy = 20
popmax = 0
turn = 1
birthturn = 1
starvingturn = 0
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
    if mainInput == ("w"):
        locx = locx - 1
    elif mainInput == ("e"):
        locx = locx + 1
    elif mainInput == ("n"):
        locy = locy - 1
    elif mainInput == ("s"):
        locy = locy + 1
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
                naturemap[locx][locy] == "Farm"
                if food < population:
                    print ("People are starving")
                    print ("You have 3 turns to fix it")
                    starvingturn = starvingturn + 1
                    if starvingturn == 3:
                            print("You loose")
                            sys.exit()
        foodperturn = foodperturn + 10
        food = food - population
        turn = turn + 1
        birthturn = birthturn + 1
        if birthturn == 10:
            population = population + 1
            birthturn = 1
        deadcrop = random.randint(1,30)
        if deadcrop == 5:
            food = food - foodperturn
            print ("Your crops died")
			

				
		
                
                
                
