import time
import sys
import math
#
from System.Collections.Generic import List
from System import Byte, Int32
#
bagOfHolding = Items.FindBySerial(Misc.ReadSharedValue("BagOfHolding"))
#
def UseKnife():
    knife = Items.FindByID(0x0EC4, -1, Player.Backpack.Serial)
    if knife == None:
        Misc.SendMessage("Need to have knife to cut up fish")
        Stop()
    Items.UseItem(knife)    
#
MotionMap = {
             "North": (0, -1), 
             "Right": (+1, -1),
             "East": (+1, 0),
             "Down": (+1, +1),
             "South": (0, +1),
             "Left": (-1, +1),
             "West": (-1, 0),
             "Up": (-1, -1),
             "North": (0, -1), 
             "Right": (+1, -1),
             "East": (+1, 0),
             "Down": (+1, +1),
             "South": (0, +1),
             "Left": (-1, +1),
             "West": (-1, 0),
             "Up": (-1, -1),
             } 
#
Distance = 3
#
while True:
    Journal.Clear()
    Items.UseItemByID(0x0DC0)
    Target.WaitForTarget(10000)
    x_delta, y_delta = MotionMap[Player.Direction]
    x = Player.Position.X + (x_delta * Distance)
    y = Player.Position.Y + (y_delta * Distance)
    tiles = Statics.GetStaticsTileInfo(x, y, Player.Map)
    #land_id = Statics.GetLandID(x, y, Player.Map)
    if len(tiles) == 0 or tiles[0].StaticID == 0:
        Target.TargetExecuteRelative(Player.Serial, Distance)
    else:    
        Target.TargetExecute(x, y, tiles[0].StaticZ, tiles[0].StaticID)
    #Target.TargetExecuteRelative(Player.Serial, 1)
    Misc.Pause(10000)
    if Journal.Search("seem to be biting here"):
        for i in range(0,8):
            Player.ChatSay(1, "Forward one")
            Misc.Pause(500)
    FishList = [ 0x09CC, 0x09CD, 0x09CE, 0x09CF ]
    for fish in range(0x4300, 0x430f):
        FishList.append(fish)
    for fish in range(0x44c0, 0x44cf):
        FishList.append(fish)    
    #
    for item in Player.Backpack.Contains:
        if item.ItemID in FishList: 
            UseKnife()
            Target.WaitForTarget(2000)
            Target.TargetExecute(item.Serial)
            Misc.Pause(1000)
    #        
    item = Items.FindByID(0x097A, 0, Player.Backpack.Serial)
    if item:
        Items.Move(item, bagOfHolding, -1)
        Misc.Pause(1000)   
    #
    TrashList = [ 0x1711, 0x170B, 0x170C, 0x170D, 0x170E, 0x170F ]
    TrashBag = 0x42292AC5
    #    
    for item in Player.Backpack.Contains:
        if item.ItemID in TrashList: 
            Items.Move(item, TrashBag, -1)
            Misc.Pause(1000)   
    

