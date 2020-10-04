import math


def degreesFromLine(line):
    try:
        degrees = line.replace('°', '|').replace('\'', "|").replace(',', '|').split('|')
        lat = int(degrees[0]) + int(degrees[1]) * .01
        lon = int(degrees[3]) + int(degrees[4]) * .01
        dir1 = degrees[2]
        dir2 = degrees[5]
        
        return lat, lon, dir1, dir2
    except ValueError:
        Player.HeadMessage(50, str(line))


def MapXY(line):
    lat, lon, dir1, dir2 = degreesFromLine(line)
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


def findSector(x, y):
    if x < 1280 and y < 1024:
        return "01"
    elif 1280 <= x < 2560 and y < 1024:
        return "02"
    elif 2560 <= x < 3840 and y < 1024:
        return "03"
    elif 3840 <= x < 5120 and y < 1024:
        return "04"
    elif x < 1280 and 1024 <= y < 2048:
        return "05"
    elif 1280 <= x < 2560 and 1024 <= y < 2048:
        return "06"
    elif 2560 <= x < 3840 and 1024 <= y < 2048:
        return "07"
    elif 3840 <= x < 5120 and 1024 <= y < 2048:
        return "08"
    elif x < 1280 and 2048 <= y < 3072:
        return "09"
    elif 1280 <= x < 2560 and 2048 <= y < 3072:
        return "10"
    elif 2560 <= x < 3840 and 2048 <= y < 3072:
        return "11"
    elif 3840 <= x < 5120 and 2048 <= y < 3072:
        return "12"
    elif x < 1280 and 3072 <= y < 4096:
        return "13"
    elif 1280 <= x < 2560 and 3072 <= y < 4096:
        return "14"
    elif 2560 <= x < 3840 and 3072 <= y < 4096:
        return "15"
    elif 3840 <= x < 5120 and 3072 <= y < 4096:
        return "16"
    else:
        Player.HeadMessage(60, "Could not find sector, You fucked up somehow")
        return 'Unknown'


def getFilename(sector):
    # now = datetime.datetime.now()
    UOAM_relative_path = '../../../UOAM/'
    # map_filename = 'MIBs_' + now.strftime('%Y%m%d_%H%M%S') + '.Map'
    map_filename = 'Mib_s' + sector + '.Map'
    map_path = '/'.join([UOAM_relative_path, map_filename])

    return map_path


Player.HeadMessage(50, "Select Bag of SoS")
SoSbag = Items.FindBySerial(Target.PromptTarget())
sectors_dict = {}

for s in SoSbag.Contains:
    if Journal.GetLineText("The world will save in 1 minute."):
        Misc.Pause(500)
        Player.HeadMessage(33, "Pausing for upcoming world save")
        Journal.WaitJournal("World save complete.", 120000)
        Journal.Clear()
        Player.HeadMessage(33, "Paused and cleared Journal due to world save. Script will continue now.")
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
    x, y = MapXY(line)
    sector = findSector(x, y)
    # Player.HeadMessage(33, "Coords:"+str(Gumps.LastGumpGetLine(2)))
    # Misc.Pause(400)
    # Player.HeadMessage(33, "x|y:" + str(x) + "|" + str(y))
    # Misc.Pause(400)
    Gumps.CloseGump(1426736667)
    Misc.Pause(1200)

    coords = "+amib: " + str(x) + " " + str(y) + " " + "1" + " " + str(s.Serial)[-4:] + "\n"

    if sectors_dict.get(sector):
        sectors_dict[sector].append(coords)
    else:
        sectors_dict[sector] = ["3 \n", coords]

    ##Begin File Save
    Player.HeadMessage(33, str(coords))


# save the .Mib files, split by sector
for sector in sectors_dict.keys():
    map_path = getFilename(sector)
    txt = "".join(sectors_dict[sector])
    Misc.Pause(800)
    ##create new Mibs.Map text file in UOAM directory 
    with open(map_path, 'w') as txt_file:
        txt_file.write(txt)
    Misc.Pause(400)
    msg = "Sector " + sector + " complete."
    Player.HeadMessage(33, msg)


Player.HeadMessage(33, "Script complete.")