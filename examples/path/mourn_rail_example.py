from System.Collections.Generic import List


def gotoLocation(x1, y1):
    Coords = PathFinding.Route() 
    Coords.X = x1
    Coords.Y = y1
    Coords.MaxRetry = -1
    PathFinding.Go(Coords)
    Misc.Pause(200)


railCoords1 = [[3676, 2271],[3676, 2290],[3675, 2296],[3649, 2296]]
railCoords2 = [[3631, 2376],[3631, 2402],[3631, 2448],[3631, 2488]]


def gosomewhere():              
    for coords in railCoords1:
        gotoLocation(coords[0],coords[1])


def gosomewhereelse():
    for coords in railCoords2:
        gotoLocation(coords[0],coords[1])


def dosomething():
    pass # filler till you code something
    #what to do

gosomewhere()
dosomething()
gosomewhereelse()
dosomething()
