# Imports the CSV library
import csv
import string


def display(list):

    start = 0
    Pokedex = ''

    if len(list) == 0:
        Pokedex = "No Entry Found"
        return Pokedex

    for x in list.keys():
        if start == 0:
            Pokedex = f"{'###':<4} {'Name':<13} {'Region':<8} {'Weight':<11} {'Height':<8} {'Type 1':<10} {'Type 2':<10}"
            Pokedex += "\n"
            Pokedex += ('-' * 70)
            Pokedex += "\n"
            start = 1

        Num = list[x]['number']
        num = str(int(Num)).zfill(3)
        name2 = list[x]['name']
        region = list[x]['region']
        weight = list[x]['weight']
        height = list[x]['height']
        typ1 = list[x]['type1']
        typ2 = list[x]['type2']
        Num = int(Num)
        Num = str(Num)

        Pokedex += f"{num:<4} {name2:<13} {region:<8} {weight:<11} {height:<8} {typ1:<10} {typ2:<10}"
        Pokedex += "\n"

    return Pokedex


def alpha(list4, reverse):
    # creates list to sort names
    nam = []
    # integer to go through the whole pokedex
    y = 0
    # integer to place the new pokedex dictionary in the correct place
    place = 1

    # Creates new list called PokedexA that will be returned containing the list in alphabetical order
    PokedexA = list4.copy()
    # Clears list to start fresh
    PokedexA.clear()

    if len(list4) == 0:
        return PokedexA

    for count in list4.keys():
        # for the length of the pokedex add just the name to the list
        nam.append(list4[count]['name'])

    # If else to determine if the list is sorted A-Z or Z-A
    if reverse == "1":
        # List is sorted A-Z
        nam.sort()
    else:
        # List is sorted Z-A
        nam.sort(reverse=True)

    # While loop to go through the length of the dictionary list2
    while y < len(list4):
        # For loop to compare to each item in the dictionary
        for ne in list4.keys():
            # If else statement to compare list to dictionary for sorting of the dictionary
            if nam[y] == list4[ne]['name']:
                # Some pokemon are listed multiple times in pokedex this ensure correct entry is selected
                if nam[y] == nam[y - 5]:
                    PokedexA[place] = list4[ne + 5]
                    place += 1
                    break
                elif nam[y] == nam[y-4]:
                    PokedexA[place] = list4[ne + 4]
                    place += 1
                    break
                elif nam[y] == nam[y-3]:
                    PokedexA[place] = list4[ne + 3]
                    place += 1
                    break
                elif nam[y] == nam[y-2]:
                    PokedexA[place] = list4[ne + 2]
                    place += 1
                    break
                elif nam[y] == nam[y-1]:
                    PokedexA[place] = list4[ne + 1]
                    place += 1
                    break
                else:
                    PokedexA[place] = list4[ne]
                    place += 1
                    break
            else:
                continue

        y += 1
    return PokedexA


def weight_order(list5, reverse):

    # creates blank list to help with ordering
    whgt = []
    # Integer to ensure the whole pokedex is run through
    y = 0
    # integer to place the entry in a new dictionary
    place = 1
    # Creates and clears ne dictionary that is sent back to main code
    PokedexW = list5.copy()
    PokedexW.clear()

    if len(list5) == 0:
        return PokedexW

    for count in list5.keys():
        # The list is filled with both the name as a string and weight as a double
        whgt.append([list5[count]['name'], list5[count]['weightN']])

    # If else to determine if the list is sorted lightest to heaviest or vice versa
    if reverse == "1":
        # sorted lightest to heaviest
        whgt.sort(key=lambda weight: weight[1])
    else:
        # sorted heaviest to lightest
        whgt.sort(key=lambda weight: weight[1], reverse=True)

    # unknown
    columns = list(zip(*whgt))

    # separates the sorted list into name and weight for ease of looping through
    nameO = columns[0]
    weightO = columns[1]

    # For the length of the list
    while y < len(list5):
        # for the length of the number of keys
        for ne in list5.keys():
            # Compares the name of the sorted list to the dictionary
            if nameO[y] == list5[ne]['name']:
                # Compares the weight of the found name to the weight of the sorted list
                if weightO[y] == list5[ne]['weightN']:
                    #
                    if nameO[y] == nameO[y - 5]:
                        PokedexW[place] = list5[ne + 5]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 4]:
                        PokedexW[place] = list5[ne + 4]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 3]:
                        PokedexW[place] = list5[ne + 3]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 2]:
                        PokedexW[place] = list5[ne + 2]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 1]:
                        PokedexW[place] = list5[ne + 1]
                        place += 1
                        break
                    else:
                        PokedexW[place] = list5[ne]
                        place += 1
                        break
                else:
                    continue
            else:
                continue

        y += 1
    return PokedexW


def height_order(list6, reverse):

    hght = []
    y = 0
    place = 1
    PokedexH = list6.copy()
    PokedexH.clear()

    if len(list6) == 0:
        return PokedexH

    for count in list6.keys():
        hght.append([list6[count]['name'], list6[count]['height'], list6[count]['heightN']])

    if reverse == "1":
        hght.sort(key=lambda height: height[2])
    else:
        hght.sort(key=lambda height: height[2], reverse=True)

    columns = list(zip(*hght))

    nameO = columns[0]
    heightO = columns[1]

    while y < len(list6):
        for ne in list6.keys():
            if nameO[y] == list6[ne]['name']:
                if heightO[y] == list6[ne]['height']:
                    if nameO[y] == nameO[y - 5]:
                        PokedexH[place] = list6[ne + 5]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 4]:
                        PokedexH[place] = list6[ne + 4]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 3]:
                        PokedexH[place] = list6[ne + 3]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 2]:
                        PokedexH[place] = list6[ne + 2]
                        place += 1
                        break
                    elif nameO[y] == nameO[y - 1]:
                        PokedexH[place] = list6[ne + 1]
                        place += 1
                        break
                    else:
                        PokedexH[place] = list6[ne]
                        place += 1
                        break
                else:
                    continue
            else:
                continue

        y += 1
    return PokedexH


def numerical_order(list7, reverse):
    # creates list to sort names
    num = []
    # integer to go through the whole pokedex
    y = 0
    # integer to place the new pokedex dictionary in the correct place
    place = 1

    # Creates new list called PokedexN that will be returned containing the list in alphabetical order
    PokedexN = list7.copy()
    # Clears list to start fresh
    PokedexN.clear()

    if len(list7) == 0:
        return PokedexN

    for count in list7.keys():
        # for the length of the pokedex add just the name to the list
        num.append(list7[count]['number'])

    # If else to determine if the list is sorted A-Z or Z-A
    if reverse == "1":
        # List is sorted 1-898
        num.sort()
    else:
        # List is sorted 898-1
        num.sort(reverse=True)

    # While loop to go through the length of the dictionary list2
    while y < len(list7):
        # For loop to compare to each item in the dictionary
        for ne in list7.keys():
            # If else statement to compare list to dictionary for sorting of the dictionary
            if num[y] == list7[ne]['number']:
                # Some pokemon are listed multiple times in pokedex this ensure correct entry is selected
                if num[y] == num[y - 5]:
                    PokedexN[place] = list7[ne + 5]
                    place += 1
                    break
                elif num[y] == num[y - 4]:
                    PokedexN[place] = list7[ne + 4]
                    place += 1
                    break
                elif num[y] == num[y - 3]:
                    PokedexN[place] = list7[ne + 3]
                    place += 1
                    break
                elif num[y] == num[y - 2]:
                    PokedexN[place] = list7[ne + 2]
                    place += 1
                    break
                elif num[y] == num[y - 1]:
                    PokedexN[place] = list7[ne + 1]
                    place += 1
                    break
                else:
                    PokedexN[place] = list7[ne]
                    place += 1
                    break
            else:
                continue

        y += 1
    return PokedexN


def show_type(list8, typeA, choose):

    PokedexT = list8.copy()
    PokedexT.clear()
    place = 1

    if len(list8) == 0:
        return PokedexT

    if choose == "1":
        for x in list8.keys():
            if list8[x]['type2'] == typeA.capitalize() or list8[x]['type1'] == typeA.capitalize():
                PokedexT[place] = list8[x]
                place += 1
            else:
                continue

    elif choose == "2":
        for x in list8.keys():
            if list8[x]['type1'] == typeA.capitalize():
                PokedexT[place] = list8[x]
                place += 1
            else:
                continue

    elif choose == "3":
        for x in list8.keys():
            if list8[x]['type2'] == typeA.capitalize():
                PokedexT[place] = list8[x]
                place += 1
            else:
                continue

    elif choose == "4":
        for x in list8.keys():
            if list8[x]['type1'] == typeA.capitalize() and list8[x]['type2'] == '':
                PokedexT[place] = list8[x]
                place += 1
            else:
                continue

    else:
        PokedexT.clear()
    return PokedexT


def find(list9, name3):

    PokedexF = list9.copy()
    PokedexF.clear()
    place = 1
    found = 0

    if len(list9) == 0:
        return PokedexF

    for x in list9.keys():
        if name3.capitalize() == list9[x]['name']:
            PokedexF[place] = list9[x]
            place += 1
            found = 1
        else:
            continue
    if found == 0:
        PokedexF.clear()
    return PokedexF


def find_with(list10, name4):

    PokedexFW = list10.copy()
    PokedexFW.clear()
    place = 1
    found = 0

    if len(list10) == 0:
        return PokedexFW

    for x in list10.keys():
        if name4 == '':
            break
        elif name4.lower() in list10[x]['name'] or name4.capitalize() in list10[x]['name']:
            PokedexFW[place] = list10[x]
            place += 1
            found = 1
        else:
            continue
    if found == 0:
        PokedexFW.clear()
    return PokedexFW


def region(list11, reg):

    PokedexR = list11.copy()
    PokedexR.clear()
    place = 1

    if len(list11) == 0:
        return PokedexR

    for x in list11.keys():
        if list11[x]['region'] == reg.capitalize():
            PokedexR[place] = list11[x]
            place += 1
        else:
            continue

    return PokedexR


def define_list():
    # Sets up a blank dictionary
    pokemon = {
        'name': '',             # Name = Pokemon's name
        'number': 0.0,          # Number = Pokemon's National Pokedex Number
        'region': '',           # Region = Pokemon's Original Region
        'weight': '',           # Weight = Pokemon's Weight as a String
        'height': '',           # Height = Pokemon's Height as a String
        'type1': '',            # Type1 = Pokemon's Primary Type
        'type2': '',            # Type2 = Pokemon's Secondary Type
        'heightN': 0.0,         # HeightN = Pokemon's Height as a Floating Number
        'weightN': 0.0,         # WeightN = Pokemon's Weight as a Floating Number
        'EvoM': '',             # EvoM1 = The evolution method to the linked number pokemon above
        'EvStage': '',          # EvStage = which stage evolution the pokemon is
        'Abil1': '',            # Abil1 = one ability of a pokemon
        'Abil2': '',            # Abil2 = the second ability of a pokemon
        'AbilH': '',            # AbilH = the hidden ability of a pokemon
        'RBYDex': '',           # RBYDex = the Pokedex number in the Red, Blue, and Yellow games
        'GSCDex': '',           # GSCDex = the Pokedex number in the Gold, Silver, and Crystal games
        'RSEDex': '',           # RSEDex = the Pokedex number in the Ruby, Sapphire, and Emerald games
        'FRLGDex': '',          # FRLGDex = the Pokedex number in theFire Red and Leaf Green games
        'DPDex': '',            # DPDex = the Pokedex number in the Diamond and Pearl games
        'PDex': '',             # PDex = the Pokedex number in the Platinum game
        'HGSSDex': '',          # HGSSDex = the Pokedex number in the Heart Gold and Soul Silver games
        'BWDex': '',            # BWDex = the Pokedex number in the Black and White games
        'B2W2Dex': '',          # B2W2Dex = the Pokedex number in the Black2 and White2 games
        'XYcentDex': '',        # XYcentDex = the central Pokedex number in the X and Y games
        'XYcoastDex': '',       # XYcoastDex = the coastal Pokedex number in the X and Y games
        'XYmountDex': '',       # XYmountDex = the mountain Pokedex number in the X and Y games
        'ORASDex': '',          # ORASDex = the Pokedex number in the Omega Ruby and Alpha Sapphire games
        'SMDex': '',            # SMDex = the Pokedex number in the Sun and Moon games
        'SMMelDex': '',         # SMDex = the Melemele Pokedex number in the Sun and Moon games
        'SMAkaDex': '',         # SMDex = the Akala Pokedex number in the Sun and Moon games
        'SMUlaDex': '',         # SMDex = the Ula'ula Pokedex number in the Sun and Moon games
        'SMPoniDex': '',        # SMDex = the Poni Pokedex number in the Sun and Moon games
        'USUMDex': '',          # USUMDex = the Pokedex number in the Ultra Sun and Ultra Moon games
        'USUMMelDex': '',       # USUMDex = the Melemele Pokedex number in the Ultra Sun and Ultra Moon games
        'USUMAkaDex': '',       # USUMDex = the Akala Pokedex number in the Ultra Sun and Ultra Moon games
        'USUMUlaDex': '',       # USUMDex = the Ula'ula Pokedex number in the Ultra Sun and Ultra Moon games
        'USUMPoniDex': '',      # USUMDex = the Poni Pokedex number in the Ultra Sun and Ultra Moon games
        'LGPEDex': '',          # LGPEDex = the Pokedex number in the Let's Go Pikachu and Let's Go Eevee games
        'SSDex': '',            # SSDex = the Pokedex number in the Sword and Shield games
        'SSIoADex': '',         # SSIoADex = the Isle of Armor Pokedex number in the Sword and Shield games
        'SSTCTDex': '',         # SSTCTDex = The Crown Tundra Pokedex number in the Sword and Shield games
        'RBEntry': '',           # REntry = Pokedex entry in the Red Pokedex
        'YellowEntry': '',           # YEntry = Pokedex entry in the Yellow Pokedex
        'GEntry': '',           # GEntry = Pokedex entry in the Gold Pokedex
        'SilEntry': '',         # SilEntry = Pokedex entry in the Silver Pokedex
        'CEntry': '',           # CEntry = Pokedex entry in the Crystal Pokedex
        'REntry': '',           # REntry = Pokedex entry in the Ruby Pokedex
        'SapEntry': '',         # SapEntry = Pokedex entry in the Sapphire Pokedex
        'EEntry': '',           # EEntry = Pokedex entry in the Emerald Pokedex
        'FREntry': '',          # FREntry = Pokedex entry in the Fire Red Pokedex
        'LGEntry': '',          # LGEntry = Pokedex entry in the Leaf Green Pokedex
        'DEntry': '',           # DEntry = Pokedex entry in the Diamond Pokedex
        'PearlEntry': '',       # PearlEntry = Pokedex entry in the Pearl Pokedex
        'PlatEntry': '',        # PlatEntry = Pokedex entry in the Platinum Pokedex
        'HGEntry': '',          # HGEntry = Pokedex entry in the Heart Gold Pokedex
        'SSEntry': '',          # SSEntry = Pokedex entry in the Soul Silver Pokedex
        'BEntry': '',           # BEntry = Pokedex entry in the Black Pokedex
        'WEntry': '',           # WEntry = Pokedex entry in the White Pokedex
        'B2Entry': '',          # B2Entry = Pokedex entry in the Black2 Pokedex
        'XEntry': '',           # XEntry = Pokedex entry in the X Pokedex
        'YEntry': '',           # YEntry = Pokedex entry in the Y Pokedex
        'OREntry': '',          # OREntry = Pokedex entry in the Omega Ruby Pokedex
        'ASEntry': '',          # ASEntry = Pokedex entry in the Alpha Sapphire Pokedex
        'SunEntry': '',         # SunEntry = Pokedex entry in the Sun Pokedex
        'MEntry': '',           # MEntry = Pokedex entry in the Moon Pokedex
        'USEntry': '',          # USEntry = Pokedex entry in the Ultra Sun Pokedex
        'UMEntry': '',          # UMEntry = Pokedex entry in the Ultra Moon Pokedex
        'LGPEntry': '',         # LGPEntry = Pokedex entry in the Let's Go Pikachu Pokedex
        'SwordEntry': '',       # SwordEntry = Pokedex entry in the Sword Pokedex
        'ShieldEntry': '',      # ShieldEntry = Pokedex entry in the Shield Pokedex
        'SpriteM': [],         # Sprite = Location of the sprite image
        'ShinySpriteM': [],    # ShinySprite = location of the shiny sprite image
        'SpriteG': '',          # Sprite = Location of the sprite image
        'ShinySpriteG': '',     # ShinySprite = location of the shiny sprite image
        'SpriteForm': [],
        'TreeT': '',            # TreeT = type of evolutionary tree
        'Group': 0,             # Group = Group number for evolutions
        'Placement': '',        # Placement = Placement in the Evolutionary tree
        'MegaAbil': '',
        'MegaType': '',
        'MegaWgt': 0.0,
        'MegaHgt': '',
        'GigantamaxHgt': ''
    }

    # Clears the dictionary to remove the first entry
    pokemon.clear()
    unown = 201
    letters = list(string.ascii_uppercase)
    letters.append('!')
    letters.append('?')
    castform = 351
    castformf = ['Normal', 'Fire', 'Water', 'Flying']
    primal = [382, 383]
    primalf = ['Normal Form', 'Primal Form']
    deoxys = 386
    deoxysf = ['Normal', 'Attack', 'Defence', 'Speed']
    burmy = 412
    burmyf = ['Grass Cloak', 'Sand Cloak', 'Trash Cloak']
    cher = 421
    cherf = ['Overcast', 'Sunshine']
    shedon = [422, 423]
    shedonf = ['West', 'East']
    rotom = 479
    rotomf = ['Electric', 'Heat', 'Wash', 'Frost', 'Fan', 'Mow']
    giratina = 487
    giratinaf = ['Altered Form', 'Origin Form']
    shaymin = 492
    shayminf = ['Land', 'Sky']
    arcsil = [493, 773]
    typing = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water',
              'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy']
    basc = 550
    bascf = ['Red-Striped', 'Blue-Striped']
    deer = [585, 586]
    deerf = ['Spring', 'Summer', 'Fall', 'Winter']
    orus = [641, 642, 645]
    orusf = ['Incarnate Form', 'Therian Form']
    kyurem = 646
    kyuremf = ['Normal', 'Black', 'White']
    keld = 647
    keldf = ['Ordinary', 'Resolute']
    meloetta = 648
    meloettaf = ['Aria', 'Pirouette']
    genesect = 649
    genesectf = ['No Drive', 'Douse Drive', 'Shock Drive', 'Burn Drive', 'Chill Drive']
    viv = 666
    vivf = ['Icy Snow', 'Polar', 'Tundra', 'Continental', 'Garden', 'Elegant', 'Meadow', 'Modern', 'Marine',
            'Archipelago', 'High Plains', 'Sandstorm', 'River', 'Monsoon', 'Savanna', 'Sun', 'Ocean', 'Jungle', 'Fancy',
            'PokeBall']
    flabe = [669, 670, 671]
    flabec = ['Red', 'Yellow', 'Orange', 'Blue', 'White']
    fur = 676
    furf = ['Natural', 'Heart', 'Star', 'Diamond', 'Debutante', 'Matron', 'Dandy', 'La Reine', 'Kabuki', 'Pharaoh']
    aeg = 681
    aegf = ['Shield', 'Blade']
    pumpgeist = [710, 711]
    pumpgeistf = ['Small', 'Average', 'Large', 'Extra Large']
    zygarde = 718
    zygardef = ['10% Form', '50% Form', 'Perfect Form']
    hoopa = 720
    hoopaf = ['Confined', 'Unbound']
    ori = 741
    orif = ['Baile Style', 'Pom-Pom Style', "Pa'u Style", 'Sensu Style']
    lycan = 745
    lycanf = ['Midday', 'Midnight', 'Dusk']
    wishi = 746
    wishif = ['Solo', 'School']
    mini = 774
    minic = ['Shelled', 'Green', 'Orange', 'Yellow', 'Light Blue', 'Blue', 'Pink', 'Purple', 'Black']
    necro = 800
    necrof = ['Normal', 'Dawn Wings', 'Dusk Mane']
    magern = 801
    magernf = ['Normal', 'Original Color']
    cram = 845
    cramf = ['Normal', 'Gulping', 'Gorging']
    alcrem = 869
    alcremfl = ['Vanilla Cream', 'Ruby Cream', 'Matcha Cream', 'Mint Cream', 'Lemon Cream', 'Salted Cream', 'Ruby Swirl',
                'Caramel Swirl', 'Rainbow Swirl']
    alcremsw = ['Strawberry', 'Berry', 'Love', 'Star', 'Clover', 'Flower', 'Bow']
    morp = 877
    morpf = ['Full Belly', 'Hangry']
    eiscue = 875
    eiscuef = ['Ice Face', 'Noice Face']
    caler = 898
    celerf = ['Normal', 'Ice Rider', 'Shadow Rider']




    # Opens the csv file of pokemon entries
    with open('Pokedex_List_3.csv', encoding='utf-8', newline='') as f:
        reader = enumerate(csv.reader(f))

        # Increments through the rows
        for i, row in reader:
            if i > 0:
                # Saves the information of the different rows and columns
                numb = float(row[0])    # Saves the pokemon's number
                name = row[1]           # Saves the pokemon's name
                reg = row[2]            # Saves the pokemon's region
                wgt = str(float(row[3])) + " lbs."   # Saves the pokemon's weight as a string
                wgt2 = float(row[3])    # Saves the pokemon's weight as a floating number
                hgt = row[4]            # Saves the pokemon's height
                tp1 = row[5]            # Saves the pokemon's first type
                tp2 = row[6]            # Saves the pokemon's second type
                hgtN = float(row[7])    # Saves the pokemon's height as a floating number
                evoM = row[8]
                evs = row[9]
                ab1 = row[10]
                ab2 = row[11]
                abH = row[12]
                rby = row[13]
                gsc = row[14]
                rse = row[15]
                frlg = row[16]
                dp = row[17]
                p = row[18]
                hgss = row[19]
                bw = row[20]
                b2w2 = row[21]
                xycent = row[22]
                xycoast = row[23]
                xymount = row[24]
                oras = row[25]
                sm = row[26]
                smm = row[27]
                sma = row[28]
                smu = row[29]
                smp = row[30]
                usum = row[31]
                usumm = row[32]
                usuma = row[33]
                usumu = row[34]
                usump = row[35]
                lgpe = row[36]
                ss = row[37]
                ssa = row[38]
                sst = row[39]
                red = row[40]
                yellow = row[41]
                gold = row[42]
                silver = row[43]
                crystal = row[44]
                ruby = row[45]
                sapphire = row[46]
                emerald = row[47]
                fred = row[48]
                lgreen = row[49]
                diamond = row[50]
                pearl = row[51]
                platinum = row[52]
                hgold = row[53]
                ssilver = row[54]
                black = row[55]
                white = row[56]
                black2 = row[57]
                x = row[58]
                y = row[59]
                oruby = row[60]
                asapphire = row[61]
                sun = row[62]
                moon = row[63]
                usun = row[64]
                umoon = row[65]
                lgp = row[66]
                sword = row[67]
                shield = row[68]
                spritemf = row[69]
                sspritemf = row[70]
                spritema = row[71]
                sspritema = row[72]
                spritef = row[73]
                sspritef = row[74]
                spritem = row[75]
                sspritem = row[76]
                spriteg = row[77]
                sspriteg = row[78]
                treet = row[79]
                treeg = int(row[80])
                treep = row[81]
                mabil = row[84]
                mtype = row[85]
                mwgt = row[86]
                mhgt = row[87]
                ghgt = row[88]
                # Ensures the strings are capitalized
                name = str.title(name)      # Saves the name with each word capitalized
                reg = str.capitalize(reg)   # Saves the region capitalized
                tp1 = str.capitalize(tp1)   # Saves the first type capitalized
                tp2 = str.capitalize(tp2)   # Saves the second type capitalized

                if int(numb) == unown:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, letters[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + letters[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == castform:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, castformf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + castformf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == deoxys:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, deoxysf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + deoxysf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == burmy:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, burmyf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + burmyf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == cher:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, cherf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + cherf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) in shedon:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, shedonf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + shedonf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == rotom:
                    pass
                elif int(numb) == giratina:
                    pass
                elif int(numb) == shaymin:
                    pass
                elif int(numb) in arcsil:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, typing[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + typing[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == basc:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, bascf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + bascf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) in deer:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, deerf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + deerf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) in orus:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, orusf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + orusf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == kyurem:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, kyuremf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + kyuremf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == keld:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, keldf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + keldf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == meloetta:
                    pass
                elif int(numb) == genesect:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, genesectf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + genesectf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == viv:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, vivf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + vivf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) in flabe:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, flabec[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + flabec[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == fur:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, furf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + furf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == aeg:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, aegf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + aegf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) in pumpgeist:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, pumpgeistf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + pumpgeistf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == zygarde:
                    pass
                elif int(numb) == hoopa:
                    pass
                elif int(numb) == ori:
                    pass
                elif int(numb) == wishi:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, wishif[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + wishif[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == mini:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n'))
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, minic[l]]
                        p += 1
                        l += 1
                    sptm.append([ssptm[0], '\u2606 ' + minic[-1] + ' \u2606'])
                    spriteFo = sptm
                elif int(numb) == necro:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, necrof[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + necrof[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == magern:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, magernf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + magernf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == cram:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, cramf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + cramf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == alcrem:
                    p = 0
                    fl = 0
                    sw = 0
                    ssptm = sspritemf.split('\n')
                    sptm = [''] * len(spritemf.split('\n')) + [''] * len(ssptm)
                    for t in spritemf.split('\n'):
                        if sw == len(alcremsw):
                            fl += 1
                            sw = 0
                        sptm[p] = [t, alcremfl[fl] + ' ' + alcremsw[sw]]
                        p += 1
                        sw += 1
                    sw = 0
                    for l in ssptm:
                        sptm[p] = [l, '\u2606 ' + alcremsw[sw] + ' \u2606']
                        p += 1
                        sw += 1
                    spriteFo = sptm
                elif int(numb) == morp:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, morpf[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + morpf[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                elif int(numb) == caler:
                    pass
                elif int(numb) == eiscue:
                    p = 0
                    l = 0
                    sptm = [''] * len(spritemf.split('\n')) * 2
                    ssptm = sspritemf.split('\n')
                    for t in spritemf.split('\n'):
                        sptm[p] = [t, eiscuef[l]]
                        p += 1
                        sptm[p] = [ssptm[l], '\u2606 ' + eiscuef[l] + ' \u2606']
                        p += 1
                        l += 1
                    spriteFo = sptm
                else:
                    if spritemf != '':
                        spriteFo = [[spritemf, 'Male/Female']]
                        spriteFo.append([sspritemf, '\u2606 Male/Female \u2606'])
                    else:
                        spriteFo = [[spritema, 'Male']]
                        spriteFo.append([sspritema, '\u2606 Male \u2606'])
                        spriteFo.append([spritef, 'Female'])
                        spriteFo.append([sspritef, '\u2606 Female \u2606'])

                if spritem != '':
                    if len(spritem.split('\n')) == 2:
                        spritem = spritem.split('\n')
                        sspritem = sspritem.split('\n')
                        spriteFo.append([spritem[0], 'Mega Y'])
                        spriteFo.append([sspritem[0], '\u2606 Mega Y \u2606'])
                        spriteFo.append([spritem[1], 'Mega X'])
                        spriteFo.append([sspritem[1], '\u2606 Mega X \u2606'])
                    elif int(numb) in primal:
                        spritem = [spritem]
                        sspritem = [sspritem]
                        spriteFo.append([spritem[0], primalf[1]])
                        spriteFo.append([sspritem[0], '\u2606 ' + primalf[1] + ' \u2606'])
                    elif int(numb) == necro:
                        spritem = [spritem]
                        sspritem = [sspritem]
                        spriteFo.append([spritem[0], 'Ultra Burst'])
                        spriteFo.append([sspritem[0], '\u2606 Ultra Burst \u2606'])
                    else:
                        spritem = [spritem]
                        sspritem = [sspritem]
                        spriteFo.append([spritem[0], 'Mega'])
                        spriteFo.append([sspritem[0], '\u2606 Mega \u2606'])
                else:
                    pass

                if spriteg != '':
                    spriteFo.append([spriteg, 'Gigantamax'])
                    spriteFo.append([sspriteg, '\u2606 Gigantamax \u2606'])
                else:
                    pass

                # Saves the information to the directory
                pokemon.update({i: {'name': name, 'number': numb, 'region': reg, 'weight': wgt, 'height': hgt,
                                    'type1': tp1, 'type2': tp2, 'heightN': hgtN, 'weightN': wgt2,
                                    'EvoM': evoM, 'EvStage': evs, 'Abil1': ab1, 'Abil2': ab2, 'AbilH': abH,
                                    'RBYDex': rby, 'GSCDex': gsc, 'RSEDex': rse, 'FRLGDex': frlg, 'DPDex': dp,
                                    'PDex': p, 'HGSSDex': hgss, 'BWDex': bw, 'B2W2Dex': b2w2, 'XYcentDex': xycent,
                                    'XYcoastDex': xycoast, 'XYmount': xymount, 'ORASDex': oras, 'SMDex': sm,
                                    'SMMelDex': smm, 'SMAkaDex': sma, 'SMUlaDex': smu, 'SMPoniDex': smp,
                                    'USUMDex': usum, 'USUMMelDex': usumm, 'USUMAkaDex': usuma, 'USUMUlaDex': usumu,
                                    'USUMPoniDex': usump, 'LGPEDex': lgpe, 'SSDex': ss, 'SSIoADex': ssa,
                                    'SSTCTDex': sst, 'RBEntry': red, 'YellowEntry': yellow, 'GEntry': gold,
                                    'SilEntry': silver, 'CEntry': crystal, 'REntry': ruby, 'SapEntry': sapphire,
                                    'EEntry': emerald, 'FREntry': fred, 'LGEntry': lgreen, 'DEntry': diamond,
                                    'PearlEntry': pearl, 'PlatEntry': platinum, 'HGEntry': hgold, 'SSEntry': ssilver,
                                    'BEntry': black, 'WEntry': white, 'B2Entry': black2, 'XEntry': x, 'YEntry': y,
                                    'OREntry': oruby, 'ASEntry': asapphire, 'SunEntry': sun, 'MEntry': moon,
                                    'USEntry': usun, 'UMEntry': umoon, 'LGPEntry': lgp, 'SwordEntry': sword,
                                    'ShieldEntry': shield, 'SpriteM': spritem, 'ShinySpriteM': sspritem,
                                    'SpriteG': spriteg, 'ShinySpriteG': sspriteg, 'TreeT': treet, 'Group': treeg,
                                    'Placement': treep, 'SpriteForm': spriteFo, 'MegaAbil': mabil, 'MegaType': mtype,
                                    'MegaWgt': mwgt, 'MegaHgt': mhgt, 'GigantamaxHgt': ghgt}})

    return pokemon  # Returns the list to the main program
