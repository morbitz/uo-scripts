import math

Player.HeadMessage(50, "Select Bag of SoS")
SoSbag = Items.FindBySerial(Target.PromptTarget())
Sector1 = Items.FindBySerial(0x4221255D)
Sector2 = Items.FindBySerial(0x422124D3)
Sector3 = Items.FindBySerial(0x422125AC)
Sector4 = Items.FindBySerial(0x42212242)
Sector5 = Items.FindBySerial(0x4221239C)
Sector6 = Items.FindBySerial(0x422125F8)
Sector7 = Items.FindBySerial(0x422124AA)
Sector8 = Items.FindBySerial(0x42212501)
Sector9 = Items.FindBySerial(0x41C6F619)
Sector10 = Items.FindBySerial(0x4221242D)
Sector11 = Items.FindBySerial(0x422125DA)
Sector12 = Items.FindBySerial(0x4221247A)
Sector13 = Items.FindBySerial(0x41F189FD)
Sector14 = Items.FindBySerial(0x41F1899F)
Sector15 = Items.FindBySerial(0x41C6F18D)
Sector16 = Items.FindBySerial(0x41C6F05C)


def MapXY(lat, lon, dir1, dir2):
    if dir1 == 'S':
        y = math.floor(lat) * 60. + lat % 1. * 100.
    else:
        y = -1.0 * math.ceil(lat) * 60. + lat % 1. * 100.
    y = int(y / 21600. * 4096.) + 1624
        
    if y < 0:
        y += 4096
    if y >= 4096:
        y -= 4096
            
    if dir2 == 'E':
        x = math.floor(lon) * 60. + lon % 1. * 100.
    else:
        x = -1.0 * math.ceil(lon) * 60. + lon % 1. * 100.
            
    x = int(x / 21600. * 5120.) + 1323
        
    if x < 0:
        x += 5120
    if x >= 5120:
        x -= 5120

    return x, y

Misc.Pause(800)
##create new Mibs.Map text file in UOF directory 
with open('Mibs.Map', 'w') as txt_file:
    txt_file.write("3 \n")
Misc.Pause(400) 
        
for s in SoSbag.Contains:
    if Journal.GetLineText("The world will save in 1 minute."):
        Misc.Pause(500)
        Player.HeadMessage(33, "Pausing for upcoming world save")
        Journal.WaitJournal("World save complete.", 120000)
    Items.Move(s, Player.Backpack, 0)
    Misc.Pause(800)
    if s.ItemID == 0x099F:
        Items.UseItem(s)
        Misc.Pause(800)
        for i in Player.Backpack.Contains:
            if i.ItemID == 0x14EE:
                s = i
                Misc.Pause(100)
    Items.UseItem(s)
    Gumps.WaitForGump(1426736667, 10000)
    Misc.Pause(200)
    line = Gumps.LastGumpGetLine(2)
    degrees = line.replace('°', '|').replace('\'', "|").replace(',', '|').split('|')
    lat = int(degrees[0]) + int(degrees[1]) * .01
    lon = int(degrees[3]) + int(degrees[4]) * .01
    dir1 = degrees[2]
    dir2 = degrees[5]
    x, y = MapXY(lat, lon, dir1, dir2)
    Player.HeadMessage(33, "Coords:"+str(Gumps.LastGumpGetLine(2)))
    Misc.Pause(400)
    Player.HeadMessage(33, "x|y:" + str(x) + "|" + str(y))
    Misc.Pause(400)
    if x < 1280 and y < 1024:
        Items.Move(s, Sector1, 0)
        Player.HeadMessage(33, "Sector 1")
    elif 1280 <= x < 2560 and y < 1024:
        Items.Move(s, Sector2, 0)
        Player.HeadMessage(33, "Sector 2")
    elif 2560 <= x < 3840 and y < 1024:
        Items.Move(s, Sector3, 0)
        Player.HeadMessage(33, "Sector 3")
    elif 3840 <= x < 5120 and y < 1024:
        Items.Move(s, Sector4, 0)
        Player.HeadMessage(33, "Sector 4")
    elif x < 1280 and 1024 <= y < 2048:
        Items.Move(s, Sector5, 0)
        Player.HeadMessage(33, "Sector 5")
    elif 1280 <= x < 2560 and 1024 <= y < 2048:
        Items.Move(s, Sector6, 0)
        Player.HeadMessage(33, "Sector 6")
    elif 2560 <= x < 3840 and 1024 <= y < 2048:
        Items.Move(s, Sector7, 0)
        Player.HeadMessage(33, "Sector 7")
    elif 3840 <= x < 5120 and 1024 <= y < 2048:
        Items.Move(s, Sector8, 0)
        Player.HeadMessage(33, "Sector 8")
    elif x < 1280 and 2048 <= y < 3072:
        Items.Move(s, Sector9, 0)
        Player.HeadMessage(33, "Sector 9")
    elif 1280 <= x < 2560 and 2048 <= y < 3072:
        Items.Move(s, Sector10, 0)
        Player.HeadMessage(33, "Sector 10")
    elif 2560 <= x < 3840 and 2048 <= y < 3072:
        Items.Move(s, Sector11, 0)
        Player.HeadMessage(33, "Sector 11")
    elif 3840 <= x < 5120 and 2048 <= y < 3072:
        Items.Move(s, Sector12, 0)
        Player.HeadMessage(33, "Sector 12")
    elif x < 1280 and 3072 <= y < 4096:
        Items.Move(s, Sector13, 0)
        Player.HeadMessage(33, "Sector 13")
    elif 1280 <= x < 2560 and 3072 <= y < 4096:
        Items.Move(s, Sector14, 0)
        Player.HeadMessage(33, "Sector 14")
    elif 2560 <= x < 3840 and 3072 <= y < 4096:
        Items.Move(s, Sector15, 0)
        Player.HeadMessage(33, "Sector 15")
    elif 3840 <= x < 5120 and 3072 <= y < 4096:
        Items.Move(s, Sector16, 0)
        Player.HeadMessage(33, "Sector 16")
    else:
        Items.Move(s, SortBag, 0)
        Player.HeadMessage(60, "Could not find sector, You fucked up somehow")
    Misc.Pause(1200)
    Gumps.CloseGump(1426736667)
    Misc.Pause(1200)
    
##Begin File Save
    txt = "+amib: " + str(x) + " " + str(y) + " " + "1" + " " + str(s.Serial)[-4:] + "\n"
    Player.HeadMessage(33, str(txt))
    with open('./Mibs.Map', 'a') as txt_file:
        txt_file.write(txt)
        
Player.HeadMessage(33, "Sorting Complete, Mibs.Map in Razor Enhanced Folder")
