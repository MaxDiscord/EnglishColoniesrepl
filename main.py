wood = 0
food = 0
population = 102
water = 0
x = 0
y = 0
locx = 10
locy = 10
maxx = 20
maxy = 20
naturemap = [["Forest" for x in range(maxx)] for y in range(maxy)]
naturemap[locx][locy] = "Plains"
colonymap = [["None" for x in range(maxx)] for y in range(maxy)]
colonymap[locx][locy] = "Town Hall"
print ("You have landed on a",naturemap[locx][locy],"tile. It looks like there is forest all around you")
print ("All",population," people that survived the journey voted and they voted to stay and make the colony here.")
while True:
    mainInput = input ("> ")
    if mainInput == ("w"):
        x = x - 1
    elif mainInput == ("e"):
        x = x + 1
    elif mainInput == ("n"):
        y = y - 1
    elif mainInput == ("s"):
        y = y + 1
    elif mainInput == ("gather wood"):
        naturemap[x][y] = "Plains"
        wood = wood + 5
