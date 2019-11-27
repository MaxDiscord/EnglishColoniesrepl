wood = 0
food = 0
population = 102
water
x = 0
y = -7
maxx = 20
maxy = 20
naturemap = [["Forest" for x in range(maxx)] for y in range(maxy)]
naturemap[0][-7] = "Plains"
colonymap = [["None" for x in range(maxx)] for y in range(maxy)]
colonymap[0][-7] = "Town Hall"
print ("You have landed on a Plains tile. It looks like there is forest all around you")
print ("All 102 people that survived the journey voted and they voted to stay and make the colony here.")
while True:
    mainInput = input ("> ")
    if mainInput = ("w"):
        x = x - 1
    elif mainInput = ("e"):
        x = x + 1
    elif mainInput = ("n"):
        y = y + 1
    elif mainInput = ("s"):
        y = y - 1
