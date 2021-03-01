import tkinter
from PIL import ImageTk, Image
import Pokedex_4_0 as Dex


def entrywindow():
    global press, namvar, numvar, entryvar, entryregvar, entryregvar
    global wghtvar, hgtvar, formvar, place
    global img, img2, image, canvas, entrynum
    global list2, framebottom, framebottommenu, type1var, type1label, frametype1, type2var, type2label
    global frametype2, evolframe, listbtn
    global entrychangebutton1, entrychangebutton2, entrychangebutton3, entrychangebutton4
    global entrychangebutton5, entrychangebutton6, entrychangebutton7, entrychangebutton8

    press = 1
    place = 0
    frametop = tkinter.Frame(root, bg='#A9A9A9')
    # Picture number and form buttons
    frametopleft = tkinter.Frame(frametop, bg='#A9A9A9')
    # Grid for the form buttons
    frametopleftgrid = tkinter.Frame(frametopleft, bg='#A9A9A9')
    frametopleftgrid.rowconfigure([0], minsize=10, weight=1)
    frametopleftgrid.columnconfigure([0, 1, 2], minsize=10, weight=1)
    # Holds the form name and numbers
    frametopleft2 = tkinter.Frame(frametopleft, bg='#A9A9A9')
    frametopleft2.config(highlightbackground='#A9A9A9', highlightthickness=3)
    # Name, Type, Ability, Height, and Weight
    frametopright = tkinter.Frame(frametop, bg='blue')

    frametopright2 = tkinter.Frame(frametopright, bg='blue')

    framename = tkinter.Frame(frametopright2)
    framenamel = tkinter.Frame(framename, bg='blue')
    framenamer = tkinter.Frame(framename, bg='blue')

    frameentryhw = tkinter.Frame(frametopright, bg='black')
    framehw = tkinter.Frame(frameentryhw)
    framehw.rowconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)
    framehw.columnconfigure([0], minsize=10, weight=0)
    framehw.config(height=120, width=120, highlightbackground='black', highlightthickness=2)
    framehw.grid_propagate(False)
    frameline = tkinter.Frame(framehw, bg='black')

    frameentry = tkinter.Frame(frameentryhw)
    frameentry2 = tkinter.Frame(frameentry)
    frameentryreg = tkinter.Frame(frameentry)

    frametype = tkinter.Frame(frametopright2, bg='blue')
    frametype1 = tkinter.Frame(frametype, height=38, width=110)
    frametype1.config(highlightbackground='black', highlightthickness=2)
    frametype1.pack_propagate(False)
    frametype2 = tkinter.Frame(frametype, height=37, width=110)
    frametype2.config(highlightbackground='black', highlightthickness=2)
    frametype2.pack_propagate(False)

    framebottom = tkinter.Frame(root, width=680, height=300, bg='#333333')
    framebottom.pack_propagate(False)

    framebottommenu = tkinter.Frame(framebottom, bg='#333333')
    framebottommenu.rowconfigure([0], minsize=10, weight=1)
    framebottommenu.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], minsize=10, weight=1)

    # Evolution frame that is edited in the evolution function
    evolframe = tkinter.Frame(framebottom)

    framecontrols = tkinter.Frame(root)
    framecontrols.rowconfigure([0, 1], minsize=10, weight=1)
    framecontrols.columnconfigure([0, 1, 2], minsize=10, weight=1)

    # Number as a label
    numvar = tkinter.StringVar()
    numvar.set(str(int(list2[press]['number'])).zfill(3))
    numb = tkinter.Label(frametopleft2, text='National Dex:', font=('bold', 20), bg='#A9A9A9')
    number = tkinter.Label(frametopleft2, textvariable=numvar, font=('bold', 20), bg='#A9A9A9')

    # Name as a label
    namvar = tkinter.StringVar()
    namvar.set(list2[press]['name'])
    nam = tkinter.Label(framenamel, text='Name:', font=('bold', 20))
    name = tkinter.Label(framenamer, textvariable=namvar, font=('bold', 20))

    # Weight as a label
    wghtvar = tkinter.StringVar()
    wghtvar.set(list2[press]['weight'])
    wght = tkinter.Label(framehw, text='Weight:', font=('bold', 16))
    weight = tkinter.Label(framehw, textvariable=wghtvar, font=('bold', 16))

    # height as a label
    hgtvar = tkinter.StringVar()
    hgtvar.set(list2[press]['height'])
    hgt = tkinter.Label(framehw, text='Height:', font=('bold', 16))
    height = tkinter.Label(framehw, textvariable=hgtvar, font=('bold', 16))

    # Entry and entry region as 2 labels
    entryvar = tkinter.StringVar()
    entryvar.set(f"{list2[press]['RBEntry']}")
    pdentry = tkinter.Label(frameentry2, textvariable=entryvar, wraplength=300)
    entryregvar = tkinter.StringVar()
    entryregvar.set('Red/Blue:')
    entryreg = tkinter.Label(frameentryreg, textvariable=entryregvar)

    defaultentry()
    menustart()
    diable()

    # Image as a canvas
    canvas = tkinter.Canvas(frametopleft, width=170, height=170, bg='#A9A9A9', highlightthickness=0)
    canvas.place(anchor='nw')
    img2 = imagesize(list2[press]['SpriteForm'][place][0], 170, 170)
    canvas.create_image(85, 85, image=img2)
    canvas.pack()

    formvar = tkinter.StringVar()
    formvar.set('Male/Female')
    formname = tkinter.Label(frametopleft, textvariable=formvar, bg='#A9A9A9')

    form = tkinter.Label(frametopleftgrid, text='Forms', bg='#A9A9A9')
    nxtf = tkinter.Button(frametopleftgrid, text=">", command=nextF)
    bkf = tkinter.Button(frametopleftgrid, text="<", command=backF)

    type1var = tkinter.StringVar()
    type2var = tkinter.StringVar()
    type1label = tkinter.Label(frametype1, textvariable=type1var, bg='red', font=('bold', 20))
    type2label = tkinter.Label(frametype2, textvariable=type2var, bg='green', font=('bold', 20))
    pkmtype()

    btn1 = tkinter.Button(framecontrols, text="Next", command=nextentry)
    btn2 = tkinter.Button(framecontrols, text="Back", command=lastentry)
    entrynum = tkinter.Entry(framecontrols)
    btn3 = tkinter.Button(framecontrols, text="Goto", command=goto)

    frametop.pack(side='top', fill='both', expand=1)
    frametopleft.pack(side='left', fill='y')
    frametopright.pack(side='right', fill='both', expand=1)
    framebottom.pack(fill='both', expand=1)
    frametopleftgrid.pack()
    bkf.grid(row=0, column=0, padx=2, pady=2)
    form.grid(row=0, column=1, padx=6, pady=2)
    nxtf.grid(row=0, column=2, padx=2, pady=2)
    formname.pack(fill='x', expand=1)
    frametopleft2.pack()
    numb.pack()
    number.pack()
    frametopright2.pack(side='top', fill='x')
    framename.pack(side='top', fill='x', expand=1)
    framenamel.pack(side='left', fill='x')
    framenamer.pack(side='right', fill='x', expand=1)
    nam.pack()
    name.pack(side='left', padx=80)
    frametype.pack(side='top', fill='x', pady=10, expand=1)
    frametype1.pack(side='left', expand=1)
    frametype2.pack(side='right', expand=1)
    type1label.pack()
    type2label.pack()
    frameentryhw.pack(fill='x')
    frameentryreg.pack(side='top', fill='x')
    frameentry.pack(side='left', fill='both', expand=1)
    frameentry2.pack(fill='both', expand=1)
    entryreg.pack(side='left')
    pdentry.pack(fill='both')
    framehw.pack(side='right')
    wght.grid(row=0, column=0, sticky='w')
    weight.grid(row=1, column=0, sticky='w')
    frameline.grid(row=2, column=0, pady=3, ipadx=80)
    hgt.grid(row=3, column=0, sticky='w')
    height.grid(row=4, column=0, sticky='w')
    framebottommenu.pack(fill='x')
    entrychangebutton1.grid(row=0, column=1, padx=2, pady=10)
    entrychangebutton2.grid(row=0, column=2, padx=2, pady=6)
    entrychangebutton3.grid(row=0, column=3, padx=2, pady=6)
    entrychangebutton4.grid(row=0, column=4, padx=2, pady=6)
    entrychangebutton5.grid(row=0, column=5, padx=2, pady=6)
    entrychangebutton6.grid(row=0, column=6, padx=2, pady=6)
    entrychangebutton7.grid(row=0, column=7, padx=2, pady=6)
    entrychangebutton8.grid(row=0, column=8, padx=2, pady=6)
    framecontrols.pack(fill='x', pady=5)
    btn1.grid(row=0, column=2)
    btn2.grid(row=0, column=0)
    entrynum.grid(row=0, column=1, sticky='n')
    btn3.grid(row=1, column=1, sticky='s')
    evolution()

    listbtn = tkinter.Button(root, text="Search Window", command=des2)
    listbtn.pack()


def searchwindow():
    global entry
    # creates frame for display all pokemon and display evolution
    listFrame = tkinter.Frame(root)
    # Adds a label to the sorting frame
    listL = tkinter.Label(listFrame, text='List:')
    # First sortingFrame in listFrame to organize the buttons (Houses the List pokedex button)
    listframeL = tkinter.Frame(listFrame)
    listframeR = tkinter.Frame(listFrame)

    # Creates first large sortingFrame to organize the buttons
    sortingFrame = tkinter.Frame(root)
    # Adds a label to the sorting frame
    sorting = tkinter.Label(sortingFrame, text='Sorting Options:')
    # First sortingFrame in sortingFrame to organize the buttons (Houses the List Numerically button)
    sortingframeL = tkinter.Frame(sortingFrame)
    # Second sortingFrame in sortingFrame to organize the buttons (Houses the List Alphabetically buttons)
    sortingframeCL = tkinter.Frame(sortingFrame)
    # Third sortingFrame in sortingFrame to organize the buttons (Houses the List by Weight Buttons)
    sortingframeCR = tkinter.Frame(sortingFrame)
    # Fourth sortingFrame in sortingFrame to organize the buttons (Houses the List by Height buttons)
    sortingframeR = tkinter.Frame(sortingFrame)

    # Creates second large sortingFrame to organize the buttons
    searchingFrame = tkinter.Frame(root)
    searchingFrame.rowconfigure([0], weight=1)
    searchingFrame.columnconfigure([0, 1, 2], weight=1)
    # adds label to the searching frame
    search = tkinter.Label(root, text='Searching Options:')
    # First sortingFrame in searchingFrame to organize the buttons (Houses the List from Region button)
    searchingframeL = tkinter.Frame(searchingFrame)
    # Creates a sortingFrame in searchingframeL to shift the button for a better look (Shifts the List from Region button)
    regionframeL = tkinter.Frame(searchingframeL)
    # Second sortingFrame in sortingFrame to organize the buttons (Houses the list by Type button)
    searchingframeCL = tkinter.Frame(searchingFrame)
    # Frame in searchingframeCL to organize the buttons (Houses the Type buttons and helps organize them neatly)
    typeframeCL = tkinter.Frame(searchingframeCL)
    # Third sortingFrame in sortingFrame to organize the buttons (Houses the find pokemon)
    searchingframeCR = tkinter.Frame(searchingFrame)
    # Fourth sortingFrame in sortingFrame to organize the buttons (Houses the find pokemon with)
    searchingframeR = tkinter.Frame(searchingFrame)
    # Creates a sortingFrame in searchingframeCR to shift the button for a better look(Houses the find pokemon)
    findPokeframeCR = tkinter.Frame(searchingframeCR, height="0.5i")
    # Creates a sortingFrame in searchingframeR to shift the button for a better look (Houses the find pokemon with)
    findPokeWframeR = tkinter.Frame(searchingframeR, height="0.5i")

    # a window to show the text of the pokemon
    entry = tkinter.Text(width=75, height=20)
    # creates scroll buttons for the text window
    scroll = tkinter.Scrollbar(root, command=entry.yview)
    # Sets the scroll buttons to scroll in the Y direction
    entry['yscrollcommand'] = scroll.set

    # Creates a button named List Pokedex that runs the subroutine Display
    dispP = tkinter.Button(listframeL, text="List Pokedex", command=DisplayBase)

    # Creates a button named List Numerically that runs the subroutine Display
    Num = tkinter.Button(sortingframeL, text="List Numerically Increasing", command=DisplayNumU)

    # Creates a button named List Alphabetically A-Z that runs the subroutine DisplayAlphA
    alpha = tkinter.Button(sortingframeCL, text="List Alphabetically A-Z", command=DisplayAlphA)

    # Creates a button named List Height Shortest to Tallest that runs the subroutine DisplayHgtU
    Hgt = tkinter.Button(sortingframeCR, text="List Height Shortest to Tallest", command=DisplayHgtU)

    # Creates a button named List Weight Lightest to Heaviest that runs the subroutine DisplayWgtU
    Wgt = tkinter.Button(sortingframeR, text="List Weight Lightest to Heaviest", command=DisplayWgtU)

    # Creates a button named clear that runs the Clr subroutine to clear the window
    clrWind = tkinter.Button(root, text="Clear", command=Clr)

    # Places the data window
    entry.pack()
    # Places the scroll buttons
    scroll.pack()
    # Places the clear button
    clrWind.pack()
    # Places the List Numerically button
    listFrame.pack(side='top', fill='both', expand=1)
    listL.pack()
    listframeL.pack(side='left', fill='both', expand=1)
    listframeR.pack(side='right', fill='both', expand=1)
    dispP.pack()
    startbtn = tkinter.Button(listframeR, text="Pokemon Entry", command=des)
    startbtn.pack()

    # Places the middle sortingFrame that containes 4 frames
    sortingFrame.pack(side='top', fill='both', expand=1)
    sorting.pack()
    # Places the first of 4 frames in the middle sortingFrame
    sortingframeL.pack(side='left', fill='both', expand=1)
    # Places the second of 4 frames in the middle sortingFrame
    sortingframeCL.pack(side='left', fill='both', expand=1)
    # Places the third of 4 frames in the middle sortingFrame
    sortingframeCR.pack(side='right', fill='both', expand=1)
    # Places the fourth of 4 frames in the middle sortingFrame
    sortingframeR.pack(side='right', fill='both', expand=1)

    # Places the List Numerically button
    Num.pack(padx=5, pady=5)
    # Places the List Alphabetically A-Z button
    alpha.pack(padx=5, pady=5)
    # Places the List Height shortest to tallest button
    Hgt.pack(padx=5, pady=5)
    # Places the List Weight lightest to heaviest button
    Wgt.pack(padx=5, pady=5)

    regionframeL.rowconfigure([0, 1, 2, 3], minsize=10, weight=1)
    regionframeL.columnconfigure([0, 1], minsize=10, weight=1)
    rgn1 = "Regions:"
    label2 = tkinter.Label(searchingframeL, text=rgn1)
    Rgn1 = tkinter.Button(regionframeL, text="Kanto", command=DisplayRegKanto)
    Rgn2 = tkinter.Button(regionframeL, text="Johto", command=DisplayRegJohto)
    Rgn3 = tkinter.Button(regionframeL, text="Hoenn", command=DisplayRegHoenn)
    Rgn4 = tkinter.Button(regionframeL, text="Sinnoh", command=DisplayRegSinnoh)
    Rgn5 = tkinter.Button(regionframeL, text="Unova", command=DisplayRegUnova)
    Rgn6 = tkinter.Button(regionframeL, text="Kalos", command=DisplayRegKalos)
    Rgn7 = tkinter.Button(regionframeL, text="Alola", command=DisplayRegAlola)
    Rgn8 = tkinter.Button(regionframeL, text="Galar", command=DisplayRegGalar)

    entry3 = tkinter.Entry(searchingframeCL)
    type1 = "Types of pokemon:" "\n" f"{'Normal':<9} {'Fire':<9} {'Water':<9} {'Grass':<9}"  "\n" \
            f"{'Electric':<9} {'Ice':<9} {'Fighting':<9} {'Poison':<9}" "\n"  f"{'Ground':<9} {'Flying':<9}" \
            f"{'Psychic':<9} {'Bug':<9}"  "\n" f"{'Rock':<9} {'Ghost':<9} {'Dragon':<9} {'Dark':<9}" \
            "\n" f" {'Steel':<9} {'Fairy':<9}"
    label3 = tkinter.Label(searchingframeCL, text=type1)
    typeframeCL.rowconfigure([0, 1], minsize=10, weight=1)
    typeframeCL.columnconfigure([0, 1], minsize=10, weight=1)
    Type = tkinter.Button(typeframeCL, text="Monotype", command=TypeM)
    Type1 = tkinter.Button(typeframeCL, text="Primary", command=TypeP)
    Type2 = tkinter.Button(typeframeCL, text="Secondary", command=TypeS)
    Type3 = tkinter.Button(typeframeCL, text="Both", command=TypeB)

    entry4 = tkinter.Entry(searchingframeCR)
    Pokem = "Pokemon Search:"
    label4 = tkinter.Label(searchingframeCR, text=Pokem)
    Name = tkinter.Button(searchingframeCR, text="Find Pokemon", command=FindPoke)
    NameW = tkinter.Button(searchingframeCR, text="Find Pokemon Containing", command=FindPokeW)

    search.pack()
    searchingFrame.pack(side='bottom', fill='both', expand=1)
    searchingframeL.grid(row=0, column=0)
    searchingframeCL.grid(row=0, column=1)
    searchingframeCR.grid(row=0, column=2)

    label2.pack()
    regionframeL.pack(side='left', fill='both', expand=1)
    Rgn1.grid(row=0, column=0, padx=2, pady=2)
    Rgn2.grid(row=0, column=1, padx=2, pady=2)
    Rgn3.grid(row=1, column=0, padx=2, pady=2)
    Rgn4.grid(row=1, column=1, padx=2, pady=2)
    Rgn5.grid(row=2, column=0, padx=2, pady=2)
    Rgn6.grid(row=2, column=1, padx=2, pady=2)
    Rgn7.grid(row=3, column=0, padx=2, pady=2)
    Rgn8.grid(row=3, column=1, padx=2, pady=2)

    label3.pack()
    entry3.pack(padx=2, pady=2)
    typeframeCL.pack()
    Type.grid(row=0, column=0, padx=2, pady=2)
    Type1.grid(row=0, column=1, padx=2, pady=2)
    Type2.grid(row=1, column=0, padx=2, pady=2)
    Type3.grid(row=1, column=1, padx=2, pady=2)

    label4.pack()
    entry4.pack(pady=4)
    Name.pack()
    NameW.pack()


def RB():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Red/Blue:':<23}")
    entryvar.set(list2[press]['RBEntry'])


def Y():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Yellow:':<23}")
    entryvar.set(list2[press]['YellowEntry'])


def G():
    global entryvar, press, list2, entryregvar
    if list2[press]['CEntry'] == 'N/A' and list2[press]['SilEntry'] == 'N/A':
        entryregvar.set(f"{'Gold/Silver/Crystal:':<23}")
    elif list2[press]['CEntry'] == 'N/A':
        entryregvar.set(f"{'Gold/Crystal:':<23}")
    elif list2[press]['SilEntry'] == 'N/A':
        entryregvar.set(f"{'Gold/Silver:':<23}")
    else:
        entryregvar.set(f"{'Gold:':<23}")
    entryvar.set(list2[press]['GEntry'])


def Sil():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Silver:':<23}")
    entryvar.set(list2[press]['SilEntry'])


def C():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Crystal:':<23}")
    entryvar.set(list2[press]['CEntry'])


def R():
    global entryvar, press, list2, entryregvar
    if list2[press]['SapEntry'] == 'N/A' and list2[press]['EEntry'] == 'N/A':
        entryregvar.set(f"{'Ruby/Sapphire/Emerald:':<23}")
    elif list2[press]['SapEntry'] == 'N/A' or list2[press]['SapEntry'] == list2[press]['REntry']:
        entryregvar.set(f"{'Ruby/Sapphire:':<23}")
    else:
        entryregvar.set(f"{'Ruby:':<23}")
    entryvar.set(list2[press]['REntry'])


def Sap():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Sapphire:':<23}")
    entryvar.set(list2[press]['SapEntry'])


def E():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Emerald:':<23}")
    entryvar.set(list2[press]['EEntry'])


def FR():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Fire Red:':<23}")
    entryvar.set(list2[press]['FREntry'])


def LG():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Leaf Green:':<23}")
    entryvar.set(list2[press]['LGEntry'])


def D():
    global entryvar, press, list2, entryregvar
    if list2[press]['PearlEntry'] == 'N/A' and list2[press]['PlatEntry'] == 'N/A':
        entryregvar.set(f"{'Diamond/Pearl/Platinum:':<23}")
    elif list2[press]['PearlEntry'] == 'N/A':
        entryregvar.set(f"{'Diamond/Pearl:':<23}")
    else:
        entryregvar.set(f"{'Diamond:':<23}")
    entryvar.set(list2[press]['DEntry'])


def Pearl():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Pearl:':<23}")
    entryvar.set(list2[press]['PearlEntry'])


def Plat():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Platinum:':<23}")
    entryvar.set(list2[press]['PlatEntry'])


def HG():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Heart Gold:':<23}")
    entryvar.set(list2[press]['HGEntry'])


def SS():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Soul Silver:':<23}")
    entryvar.set(list2[press]['SSEntry'])


def B():
    global entryvar, press, list2, entryregvar
    if list2[press]['WEntry'] == 'N/A' and list2[press]['B2Entry'] == 'N/A':
        entryregvar.set(f"{'Black/White/Black2/White2:':<23}")
    elif list2[press]['WEntry'] == 'N/A':
        entryregvar.set(f"{'Black/White:':<23}")
    else:
        entryregvar.set(f"{'Black:':<23}")
    entryvar.set(list2[press]['BEntry'])


def W():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'White:':<23}")
    entryvar.set(list2[press]['WEntry'])


def B2():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Black2/White2:':<23}")
    entryvar.set(list2[press]['B2Entry'])


def X():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'X:':<23}")
    entryvar.set(list2[press]['XEntry'])


def Yg():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Y:':<23}")
    entryvar.set(list2[press]['YEntry'])


def OR():
    global entryvar, press, list2, entryregvar
    if list2[press]['ASEntry'] == 'N/A':
        entryregvar.set(f"{'Omega Ruby/Alpha Sapphire:':<23}")
    else:
        entryregvar.set(f"{'Omega Ruby:':<23}")
    entryvar.set(list2[press]['OREntry'])


def AS():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Alpha Sapphire:':<23}")
    entryvar.set(list2[press]['ASEntry'])


def Sun():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Sun:':<23}")
    entryvar.set(list2[press]['SunEntry'])


def M():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Moon:':<23}")
    entryvar.set(list2[press]['MEntry'])


def US():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Ultra Sun:':<23}")
    entryvar.set(list2[press]['USEntry'])


def UM():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Ultra Moon:':<23}")
    entryvar.set(list2[press]['UMEntry'])


def LGP():
    global entryvar, press, list2, entryregvar
    lg = "Let's Go Pikachu/Eevee:"
    entryregvar.set(f"{lg:<23}")
    entryvar.set(list2[press]['LGPEntry'])


def Sword():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Sword:':<23}")
    entryvar.set(list2[press]['SwordEntry'])


def Shield():
    global entryvar, press, list2, entryregvar
    entryregvar.set(f"{'Shield:':<23}")
    entryvar.set(list2[press]['ShieldEntry'])


def nextentry():
    global press, namvar, numvar, entryvar, entryregvar
    global wghtvar, hgtvar, formvar, place
    global img, img2, image
    global list2
    place = 0
    if press >= len(list2):
        press = 1
    else:
        press = press + 1
    namvar.set(list2[press]['name'])
    numvar.set(str(int(list2[press]['number'])).zfill(3))
    wghtvar.set(list2[press]['weight'])
    hgtvar.set(list2[press]['height'])
    defaultentry()
    diable()
    evolution()
    pkmtype()
    image = list2[press]['SpriteForm'][place][0]
    formvar.set(list2[press]['SpriteForm'][place][1])
    img2 = imagesize(image, 170, 170)
    canvas.create_image(85, 85, image=img2)
    canvas.pack()


def lastentry():
    global press, namvar, numvar, entryvar, entryregvar
    global wghtvar, hgtvar, formvar, place
    global img, img2, image
    global list2
    place = 0
    if press == 1:
        press = len(list2)
    else:
        press = press - 1
    namvar.set(list2[press]['name'])
    numvar.set(str(int(list2[press]['number'])).zfill(3))
    wghtvar.set(list2[press]['weight'])
    hgtvar.set(list2[press]['height'])
    defaultentry()
    diable()
    evolution()
    pkmtype()
    image = list2[press]['SpriteForm'][place][0]
    formvar.set(list2[press]['SpriteForm'][place][1])
    img2 = imagesize(image, 170, 170)
    canvas.create_image(85, 85, image=img2)
    canvas.pack()


def des():
    list3 = root.pack_slaves()
    entry.delete("1.0", tkinter.END)
    for l in list3:
        l.destroy()
    entrywindow()


def des2():
    list3 = root.pack_slaves()
    for l in list3:
        l.destroy()
    searchwindow()


def goto():
    global press, list2
    entrynumber = entrynum.get()
    try:
        entrynumber = int(entrynumber)
        for i in list2.keys():
            if entrynumber == list2[i]['number']:
                press = i-1
                nextentry()
                break
    except ValueError:
        list10 = Dex.find_with(list2, entrynum.get())
        for i in list2.keys():
            if list10[1]['number'] == list2[i]['number']:
                press = i - 1
                nextentry()
                break


def diable():
    global entrychangebutton1, entrychangebutton2, entrychangebutton3, entrychangebutton4
    global entrychangebutton5, entrychangebutton6, entrychangebutton7, entrychangebutton8

    if list2[press]['RBEntry'] == 'N/A':
        entrychangebutton1.menu.entryconfig('Red/Blue', state='disabled')
    else:
        entrychangebutton1.menu.entryconfig('Red/Blue', state='normal')

    if list2[press]['YellowEntry'] == 'N/A':
        entrychangebutton1.menu.entryconfig('Yellow', state='disabled')
    else:
        entrychangebutton1.menu.entryconfig('Yellow', state='normal')

    if list2[press]['LGPEntry'] == 'N/A':
        entrychangebutton1.menu.entryconfig("Let's Go Pikachu/Eevee", state='disabled')
    else:
        entrychangebutton1.menu.entryconfig("Let's Go Pikachu/Eevee", state='normal')

    if list2[press]['GEntry'] == 'N/A':
        entrychangebutton2.menu.entryconfig('Gold', state='disabled')
    else:
        entrychangebutton2.menu.entryconfig('Gold', state='normal')

    if list2[press]['SilEntry'] == 'N/A':
        entrychangebutton2.menu.entryconfig('Silver', state='disabled')
    else:
        entrychangebutton2.menu.entryconfig('Silver', state='normal')

    if list2[press]['CEntry'] == 'N/A':
        entrychangebutton2.menu.entryconfig('Crystal', state='disabled')
    else:
        entrychangebutton2.menu.entryconfig('Crystal', state='normal')

    if list2[press]['REntry'] == 'N/A':
        entrychangebutton3.menu.entryconfig('Ruby', state='disabled')
    else:
        entrychangebutton3.menu.entryconfig('Ruby', state='normal')

    if list2[press]['SapEntry'] == 'N/A':
        entrychangebutton3.menu.entryconfig('Sapphire', state='disabled')
    else:
        entrychangebutton3.menu.entryconfig('Sapphire', state='normal')

    if list2[press]['EEntry'] == 'N/A':
        entrychangebutton3.menu.entryconfig('Emerald', state='disabled')
    else:
        entrychangebutton3.menu.entryconfig('Emerald', state='normal')

    if list2[press]['FREntry'] == 'N/A':
        entrychangebutton3.menu.entryconfig('Fire Red', state='disabled')
    else:
        entrychangebutton3.menu.entryconfig('Fire Red', state='normal')

    if list2[press]['LGEntry'] == 'N/A':
        entrychangebutton3.menu.entryconfig('Leaf Green', state='disabled')
    else:
        entrychangebutton3.menu.entryconfig('Leaf Green', state='normal')

    if list2[press]['DEntry'] == 'N/A':
        entrychangebutton4.menu.entryconfig('Diamond', state='disabled')
    else:
        entrychangebutton4.menu.entryconfig('Diamond', state='normal')

    if list2[press]['PearlEntry'] == 'N/A':
        entrychangebutton4.menu.entryconfig('Pearl', state='disabled')
    else:
        entrychangebutton4.menu.entryconfig('Pearl', state='normal')

    if list2[press]['PlatEntry'] == 'N/A':
        entrychangebutton4.menu.entryconfig('Platinum', state='disabled')
    else:
        entrychangebutton4.menu.entryconfig('Platinum', state='normal')

    if list2[press]['HGEntry'] == 'N/A':
        entrychangebutton4.menu.entryconfig('Heart Gold', state='disabled')
    else:
        entrychangebutton4.menu.entryconfig('Heart Gold', state='normal')

    if list2[press]['SSEntry'] == 'N/A':
        entrychangebutton4.menu.entryconfig('Soul Silver', state='disabled')
    else:
        entrychangebutton4.menu.entryconfig('Soul Silver', state='normal')

    if list2[press]['BEntry'] == 'N/A':
        entrychangebutton5.menu.entryconfig('Black', state='disabled')
    else:
        entrychangebutton5.menu.entryconfig('Black', state='normal')

    if list2[press]['WEntry'] == 'N/A':
        entrychangebutton5.menu.entryconfig('White', state='disabled')
    else:
        entrychangebutton5.menu.entryconfig('White', state='normal')

    if list2[press]['B2Entry'] == 'N/A':
        entrychangebutton5.menu.entryconfig('Black2/White2', state='disabled')
    else:
        entrychangebutton5.menu.entryconfig('Black2/White2', state='normal')

    if list2[press]['XEntry'] == 'N/A':
        entrychangebutton6.menu.entryconfig('X', state='disabled')
    else:
        entrychangebutton6.menu.entryconfig('X', state='normal')

    if list2[press]['YEntry'] == 'N/A':
        entrychangebutton6.menu.entryconfig('Y', state='disabled')
    else:
        entrychangebutton6.menu.entryconfig('Y', state='normal')

    if list2[press]['OREntry'] == 'N/A':
        entrychangebutton6.menu.entryconfig('Omega Ruby', state='disabled')
    else:
        entrychangebutton6.menu.entryconfig('Omega Ruby', state='normal')

    if list2[press]['ASEntry'] == 'N/A':
        entrychangebutton6.menu.entryconfig('Alpha Sapphire', state='disabled')
    else:
        entrychangebutton6.menu.entryconfig('Alpha Sapphire', state='normal')

    if list2[press]['SunEntry'] == 'N/A':
        entrychangebutton7.menu.entryconfig('Sun', state='disabled')
    else:
        entrychangebutton7.menu.entryconfig('Sun', state='normal')

    if list2[press]['MEntry'] == 'N/A':
        entrychangebutton7.menu.entryconfig('Moon', state='disabled')
    else:
        entrychangebutton7.menu.entryconfig('Moon', state='normal')

    if list2[press]['USEntry'] == 'N/A':
        entrychangebutton7.menu.entryconfig('Ultra Sun', state='disabled')
    else:
        entrychangebutton7.menu.entryconfig('Ultra Sun', state='normal')

    if list2[press]['UMEntry'] == 'N/A':
        entrychangebutton7.menu.entryconfig('Ultra Moon', state='disabled')
    else:
        entrychangebutton7.menu.entryconfig('Ultra Moon', state='normal')

    if list2[press]['SwordEntry'] == 'N/A':
        entrychangebutton8.menu.entryconfig('Sword', state='disabled')
    else:
        entrychangebutton8.menu.entryconfig('Sword', state='normal')

    if list2[press]['ShieldEntry'] == 'N/A':
        entrychangebutton8.menu.entryconfig('Shield', state='disabled')
    else:
        entrychangebutton8.menu.entryconfig('Shield', state='normal')


def defaultentry():
    global entryvar, entryregvar
    if list2[press]['RBEntry'] == 'N/A':
        if list2[press]['GEntry'] == 'N/A':
            if list2[press]['REntry'] == 'N/A':
                if list2[press]['DEntry'] == 'N/A':
                    if list2[press]['BEntry'] == 'N/A':
                        if list2[press]['XEntry'] == 'N/A':
                            if list2[press]['SunEntry'] == 'N/A':
                                if list2[press]['USEntry'] == 'N/A':
                                    if list2[press]['LGPEntry'] == 'N/A':
                                        entryregvar.set('Sword:')
                                        entryvar.set(list2[press]['SwordEntry'])
                                    else:
                                        entryregvar.set("Let's Go Pikachu/Eevee")
                                        entryvar.set(list2[press]['RBEntry'])
                                else:
                                    entryregvar.set('Ultra Sun:')
                                    entryvar.set(list2[press]['USEntry'])
                            else:
                                entryregvar.set('Sun:')
                                entryvar.set(list2[press]['SunEntry'])
                        else:
                            entryregvar.set('X:')
                            entryvar.set(list2[press]['XEntry'])
                    else:
                        entryregvar.set('Black:')
                        entryvar.set(list2[press]['BEntry'])
                else:
                    entryregvar.set('Diamond:')
                    entryvar.set(list2[press]['DEntry'])
            else:
                entryregvar.set('Ruby:')
                entryvar.set(list2[press]['REntry'])
        else:
            entryregvar.set('Gold:')
            entryvar.set(list2[press]['GEntry'])
    else:
        entryregvar.set('Red/Blue:')
        entryvar.set(list2[press]['RBEntry'])


def nextF():
    global list2, formvar, wghtvar, hgtvar
    global img2, press, place
    megas = []
    megass = []
    abil = []
    typem = []
    typex = []
    typey = []
    wgt = []
    hgt = []

    if place < len(list2[press]['SpriteForm'])-1:
        place += 1
    else:
        place = 0

    if list2[press]['SpriteM'] != ['']:
        megas = list2[press]['SpriteM']
        megass = list2[press]['ShinySpriteM']
        if len(megas) == 2:
            abil = list2[press]['MegaAbil'].split('\n')
            typey = list2[press]['MegaType'].split('\n')[0].split(' ')
            if len(typey) == 1:
                typey.append(' ')
            typex = list2[press]['MegaType'].split('\n')[1].split(' ')
            if len(typex) == 1:
                typex.append(' ')
            wgt = list2[press]['MegaWgt'].split('\n')
            hgt = list2[press]['MegaHgt'].split('\n')
        else:
            abil = list2[press]['MegaAbil'].split('\n')
            typem = list2[press]['MegaType'].split(' ')
            if len(typem) == 1:
                typem.append(' ')

    if len(megas) == 2:
        if list2[press]['SpriteForm'][place][0] in [megas[0], megass[0]]:
            pkmtype2(typey[0], typey[1])
            wghtvar.set(wgt[0] + ' lbs.')
            hgtvar.set(hgt[0])
        elif list2[press]['SpriteForm'][place][0] in [megas[1], megass[1]]:
            pkmtype2(typex[0], typex[1])
            wghtvar.set(wgt[1] + ' lbs.')
            hgtvar.set(hgt[1])
        elif list2[press]['SpriteForm'][place][0] in [list2[press]['SpriteG'], list2[press]['ShinySpriteG']]:
            pkmtype2(list2[press]['type1'], list2[press]['type2'])
            wghtvar.set('???? lbs.')
            hgtvar.set(list2[press]['GigantamaxHgt'])
        else:
            pkmtype2(list2[press]['type1'], list2[press]['type2'])
            wghtvar.set(list2[press]['weight'])
            hgtvar.set(list2[press]['height'])
    elif len(megas) == 1:
        if list2[press]['SpriteForm'][place][0] in [megas[0], megass[0]]:
            pkmtype2(typem[0], typem[1])
            wghtvar.set(list2[press]['MegaWgt'] + ' lbs.')
            hgtvar.set(list2[press]['MegaHgt'])
        elif list2[press]['SpriteForm'][place][0] in [list2[press]['SpriteG'], list2[press]['ShinySpriteG']]:
            pkmtype2(list2[press]['type1'], list2[press]['type2'])
            wghtvar.set('???? lbs.')
            hgtvar.set(list2[press]['GigantamaxHgt'])
        else:
            pkmtype2(list2[press]['type1'], list2[press]['type2'])
            wghtvar.set(list2[press]['weight'])
            hgtvar.set(list2[press]['height'])
    elif list2[press]['SpriteForm'][place][0] in [list2[press]['SpriteG'], list2[press]['ShinySpriteG']]:
        pkmtype2(list2[press]['type1'], list2[press]['type2'])
        wghtvar.set('???? lbs.')
        hgtvar.set(list2[press]['GigantamaxHgt'])
    else:
        pkmtype2(list2[press]['type1'], list2[press]['type2'])
        wghtvar.set(list2[press]['weight'])
        hgtvar.set(list2[press]['height'])

    formvar.set(list2[press]['SpriteForm'][place][1])
    img2 = imagesize(list2[press]['SpriteForm'][place][0], 170, 170)
    canvas.create_image(85, 85, image=img2)
    canvas.pack()


def backF():
    global list2, formvar
    global img2, press, place
    megas = []
    megass = []
    abil = []
    typem = []
    typex = []
    typey = []
    wgt = []
    hgt = []

    if place == 0:
        place = len(list2[press]['SpriteForm'])-1
    else:
        place -= 1

    if list2[press]['SpriteM'] != ['']:
        megas = list2[press]['SpriteM']
        megass = list2[press]['ShinySpriteM']
        if len(megas) == 2:
            abil = list2[press]['MegaAbil'].split('\n')
            typey = list2[press]['MegaType'].split('\n')[0].split(' ')
            if len(typey) == 1:
                typey.append(' ')
            typex = list2[press]['MegaType'].split('\n')[1].split(' ')
            if len(typex) == 1:
                typex.append(' ')
            wgt = list2[press]['MegaWgt'].split('\n')
            hgt = list2[press]['MegaHgt'].split('\n')
        else:
            abil = list2[press]['MegaAbil'].split('\n')
            typem = list2[press]['MegaType'].split(' ')
            if len(typem) == 1:
                typem.append(' ')

    if len(megas) == 2:
        if list2[press]['SpriteForm'][place][0] in [megas[0], megass[0]]:
            pkmtype2(typey[0], typey[1])
            wghtvar.set(wgt[0] + ' lbs.')
            hgtvar.set(hgt[0])
        elif list2[press]['SpriteForm'][place][0] in [megas[1], megass[1]]:
            pkmtype2(typex[0], typex[1])
            wghtvar.set(wgt[1] + ' lbs.')
            hgtvar.set(hgt[1])
        elif list2[press]['SpriteForm'][place][0] in [list2[press]['SpriteG'], list2[press]['ShinySpriteG']]:
            pkmtype2(list2[press]['type1'], list2[press]['type2'])
            wghtvar.set('???? lbs.')
            hgtvar.set(list2[press]['GigantamaxHgt'])
        else:
            pkmtype2(list2[press]['type1'], list2[press]['type2'])
            wghtvar.set(list2[press]['weight'])
            hgtvar.set(list2[press]['height'])
    elif len(megas) == 1:
        if list2[press]['SpriteForm'][place][0] in [megas[0], megass[0]]:
            pkmtype2(typem[0], typem[1])
            wghtvar.set(list2[press]['MegaWgt'] + ' lbs.')
            hgtvar.set(list2[press]['MegaHgt'])
        elif list2[press]['SpriteForm'][place][0] in [list2[press]['SpriteG'], list2[press]['ShinySpriteG']]:
            pkmtype2(list2[press]['type1'], list2[press]['type2'])
            wghtvar.set('???? lbs.')
            hgtvar.set(list2[press]['GigantamaxHgt'])
        else:
            pkmtype2(list2[press]['type1'], list2[press]['type2'])
            wghtvar.set(list2[press]['weight'])
            hgtvar.set(list2[press]['height'])
    elif list2[press]['SpriteForm'][place][0] in [list2[press]['SpriteG'], list2[press]['ShinySpriteG']]:
        pkmtype2(list2[press]['type1'], list2[press]['type2'])
        wghtvar.set('???? lbs.')
        hgtvar.set(list2[press]['GigantamaxHgt'])
    else:
        pkmtype2(list2[press]['type1'], list2[press]['type2'])
        wghtvar.set(list2[press]['weight'])
        hgtvar.set(list2[press]['height'])

    formvar.set(list2[press]['SpriteForm'][place][1])
    img2 = imagesize(list2[press]['SpriteForm'][place][0], 170, 170)
    canvas.create_image(85, 85, image=img2)
    canvas.pack()


def imagesize(file, width, height):
    spr = Image.open(file)
    spr = spr.resize((width, height), Image.ANTIALIAS)
    sprc = ImageTk.PhotoImage(spr)
    return sprc


def evolution():
    global press, list2, evolframe, list1
    global arrow1, arrow2, arrow3, arrow4, arrow5, arrow6, arrow7, arrow8, arrow9
    global sprite1, sprite2, sprite3, sprite4, sprite5, sprite6, sprite7, sprite8, sprite9, sprite10
    clr = evolframe.grid_slaves()
    for cl in clr:
        cl.destroy()
    evolframe.destroy()
    ar = 'D:\\Adam\\PycharmProjects\\pythonProject\\Sprites\\right.png'
    awr = 80
    ahr = 30
    ad = 'D:\\Adam\\PycharmProjects\\pythonProject\\Sprites\\down.png'
    adw = 30
    adh = 40
    adr = 'D:\\Adam\\PycharmProjects\\pythonProject\\Sprites\\downright.png'
    aur = 'D:\\Adam\\PycharmProjects\\pythonProject\\Sprites\\upright.png'
    adb = 'D:\\Adam\\PycharmProjects\\pythonProject\\Sprites\\dbl.png'
    awdb = 80
    ahdb = 30
    adbd = 'D:\\Adam\\PycharmProjects\\pythonProject\\Sprites\\dbldown.png'
    adbu = 'D:\\Adam\\PycharmProjects\\pythonProject\\Sprites\\dblup.png'
    awdbud = 80
    ahdbud = 40
    list3 = list2.copy()
    list3.clear()
    if list2[press]['TreeT'] == 'A':
        # evolution tree 1-2-3
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                else:
                    pass
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)
        evolframe.pack()

        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=0, column=0)
        # If there is a baby pokemon that needs a special breeding method
        if list3[1]['EvoM'] != '':
            evo4 = tkinter.Label(evolframe, text=list3[1]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
            evo4.grid(row=1, column=0, pady=4, sticky='n')
        arrow1 = imagesize(ar, awr, ahr)
        canvasA1 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awr / 2, 17, image=arrow1)
        canvasA1.grid(row=0, column=1)

        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='s')

        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w/2, h/2, image=sprite2)
        canvasE2.grid(row=0, column=2)

        canvasA2 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awr / 2, 17, image=arrow1)
        canvasA2.grid(row=0, column=3)

        evo2 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=0, column=3, pady=4, sticky='s')

        sprite3 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(42, h/2, image=sprite3)
        canvasE3.grid(row=0, column=4)
    elif list2[press]['TreeT'] == 'B':
        # evolution tree 1-2-3/3
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                elif list1[i]['Placement'] == 'D':
                    list3[4] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)
        #first arrow
        arrow1 = imagesize(ar, awr, ahr)
        canvasA1 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awr / 2, 17, image=arrow1)
        canvasA1.grid(row=1, column=1)
        # First to second evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=1, column=1, pady=4, sticky='s')
        # Second Evolution Sprite
        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=1, column=2)
        # Second arrow
        arrow3 = imagesize(adbu, awdbud, ahdbud)
        canvasA3 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA3.create_image(awdbud / 2, ahdbud / 2, image=arrow3)
        canvasA3.grid(row=0, column=3, sticky='e', rowspan=2)
        # Third arrow
        arrow4 = imagesize(adbd, awdbud, ahdbud)
        canvasA4 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA4.create_image(awdbud / 2, ahdbud / 2, image=arrow4)
        canvasA4.grid(row=1, column=3, sticky='e', rowspan=2)
        # Second to Third top evolution method
        evo2 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=0, column=3, pady=4)
        # Third top evolution sprite
        sprite4 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE4.create_image(42, h / 2, image=sprite4)
        canvasE4.grid(row=0, column=4)
        # Second to third bottom evolution method
        evo3 = tkinter.Label(evolframe, text=list3[4]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo3.grid(row=2, column=3, pady=4)
        # Third bottom evolution sprite
        sprite5 = imagesize(list3[4]['SpriteForm'][place][0], w, h)
        canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE5.create_image(42, h / 2, image=sprite5)
        canvasE5.grid(row=2, column=4)
    elif list2[press]['TreeT'] == 'C':
        # evolution tree 1-2-3/2-3
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                elif list1[i]['Placement'] == 'D':
                    list3[4] = list1[i]
                elif list1[i]['Placement'] == 'E':
                    list3[5] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)
        # first arrow
        arrow1 = imagesize(adbu, awdbud, ahdbud)
        canvasA1 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdbud / 2, ahdbud / 2, image=arrow1)
        canvasA1.grid(row=0, column=1, sticky='e', rowspan=2)
        # Second arrow
        arrow2 = imagesize(adbd, awdbud, ahdbud)
        canvasA2 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdbud / 2, ahdbud / 2, image=arrow2)
        canvasA2.grid(row=1, column=1, sticky='e', rowspan=2)
        # First to second evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4)
        # Second Evolution Sprite
        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)
        # Third arrow
        arrow3 = imagesize(ar, awr, ahr)
        canvasA3 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA3.create_image(awr / 2, 17, image=arrow3)
        canvasA3.grid(row=0, column=3)
        # Second to Third top evolution method
        evo2 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=0, column=3, sticky='s')
        # Third top evolution sprite
        sprite3 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(42, h / 2, image=sprite3)
        canvasE3.grid(row=0, column=4)
        # Second to third bottom evolution method
        evo3 = tkinter.Label(evolframe, text=list3[4]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo3.grid(row=2, column=1, pady=4)
        # Third bottom evolution sprite
        sprite4 = imagesize(list3[4]['SpriteForm'][place][0], w, h)
        canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE4.create_image(42, h / 2, image=sprite4)
        canvasE4.grid(row=2, column=2)
        # Fourth Arrow
        arrow4 = imagesize(ar, awr, ahr)
        canvasA4 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA4.create_image(awr / 2, 17, image=arrow4)
        canvasA4.grid(row=2, column=3)
        # Second to third bottom evolution method
        evo4 = tkinter.Label(evolframe, text=list3[5]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo4.grid(row=2, column=3, sticky='s')
        # Third bottom evolution sprite
        sprite5 = imagesize(list3[5]['SpriteForm'][place][0], w, h)
        canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE5.create_image(42, h / 2, image=sprite5)
        canvasE5.grid(row=2, column=4)
    elif list2[press]['TreeT'] == 'D':
        # evolution tree 1-2/2-3
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                elif list1[i]['Placement'] == 'D':
                    list3[4] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)
        # If there is a baby pokemon that needs a special breeding method
        if list3[1]['EvoM'] != '':
            evo4 = tkinter.Label(evolframe, text=list3[1]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
            evo4.grid(row=2, column=0, pady=4, sticky='n')
        # first arrow
        arrow1 = imagesize(aur, awdbud, ahdbud)
        canvasA1 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdbud / 2, ahdbud / 2, image=arrow1)
        canvasA1.grid(row=0, column=1, sticky='e', rowspan=2)
        # Second arrow
        arrow2 = imagesize(adr, awdbud, ahdbud)
        canvasA2 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdbud / 2, ahdbud / 2, image=arrow2)
        canvasA2.grid(row=1, column=1, sticky='e', rowspan=2)
        # First to second evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='n')
        # Second Evolution Sprite
        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)
        # Second to third bottom evolution method
        evo2 = tkinter.Label(evolframe, text=list3[4]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=2, column=1, pady=4)
        # Third bottom evolution sprite
        sprite4 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE4.create_image(42, h / 2, image=sprite4)
        canvasE4.grid(row=2, column=2)
        # Fourth Arrow
        arrow4 = imagesize(ar, awr, ahr)
        canvasA4 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA4.create_image(awr / 2, 17, image=arrow4)
        canvasA4.grid(row=2, column=3)
        # Second to third bottom evolution method
        evo3 = tkinter.Label(evolframe, text=list3[4]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo3.grid(row=2, column=3, sticky='s')
        # Third bottom evolution sprite
        sprite5 = imagesize(list3[4]['SpriteForm'][place][0], w, h)
        canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE5.create_image(42, h / 2, image=sprite5)
        canvasE5.grid(row=2, column=4)
    elif list2[press]['TreeT'] == 'E':
        # evolution tree 1-2
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                else:
                    pass
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.pack()

        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=0, column=0)
        # If there is a baby pokemon that needs a special breeding method
        if list3[1]['EvoM'] != '':
            evo2 = tkinter.Label(evolframe, text=list3[1]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
            evo2.grid(row=1, column=0, pady=4, sticky='n')
        arrow1 = imagesize(ar, awr, ahr)
        canvasA1 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awr / 2, 17, image=arrow1)
        canvasA1.grid(row=0, column=1)

        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='s')

        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)
    elif list2[press]['TreeT'] == 'F':
        # evolution tree 1-2/2
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)
        # first arrow
        arrow1 = imagesize(aur, awdbud, ahdbud)
        canvasA1 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdbud / 2, ahdbud / 2, image=arrow1)
        canvasA1.grid(row=0, column=1, sticky='e', rowspan=2)
        # Second arrow
        arrow2 = imagesize(adr, awdbud, ahdbud)
        canvasA2 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdbud / 2, ahdbud / 2, image=arrow2)
        canvasA2.grid(row=1, column=1, sticky='e', rowspan=2)
        # First to second evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4)
        # Second Evolution Sprite
        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)
        # Second to Third top evolution method
        evo2 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=2, column=1, pady=4)
        # Third top evolution sprite
        sprite3 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(42, h / 2, image=sprite3)
        canvasE3.grid(row=2, column=2)
    elif list2[press]['TreeT'] == 'G':
        # evolution tree 1-2/2/2
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                elif list1[i]['Placement'] == 'D':
                    list3[4] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)
        # first arrow
        arrow1 = imagesize(aur, awdbud, ahdbud)
        canvasA1 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdbud / 2, ahdbud / 2, image=arrow1)
        canvasA1.grid(row=0, column=1, sticky='s')
        # Second arrow
        arrow2 = imagesize(ar, awdbud, ahdbud)
        canvasA2 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdbud / 2, ahdbud / 2, image=arrow2)
        canvasA2.grid(row=1, column=1, sticky='e')
        # Third arrow
        arrow3 = imagesize(adr, awdbud, ahdbud)
        canvasA3 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA3.create_image(awdbud / 2, ahdbud / 2, image=arrow3)
        canvasA3.grid(row=2, column=1, sticky='n')
        # First to second top evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='n')
        # Second Evolution Sprite
        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)
        # first to second middle evolution method
        evo2 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=1, column=1, pady=4)
        # Third top evolution sprite
        sprite3 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(42, h / 2, image=sprite3)
        canvasE3.grid(row=1, column=2)
        # Fir Second to Third top evolution method
        evo3 = tkinter.Label(evolframe, text=list3[4]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo3.grid(row=2, column=1, pady=4, sticky='s')
        # Third top evolution sprite
        sprite4 = imagesize(list3[4]['SpriteForm'][place][0], w, h)
        canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE5.create_image(42, h / 2, image=sprite4)
        canvasE5.grid(row=2, column=2)
    elif list2[press]['TreeT'] == 'H':
        # evolution tree 1-2*8/G
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                elif list1[i]['Placement'] == 'D':
                    list3[4] = list1[i]
                elif list1[i]['Placement'] == 'E':
                    list3[5] = list1[i]
                elif list1[i]['Placement'] == 'F':
                    list3[6] = list1[i]
                elif list1[i]['Placement'] == 'G':
                    list3[7] = list1[i]
                elif list1[i]['Placement'] == 'H':
                    list3[8] = list1[i]
                elif list1[i]['Placement'] == 'I':
                    list3[9] = list1[i]
                else:
                    pass
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=10, weight=1)
        evolframe.pack()
        # First Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=0, column=4)
        # If there is a baby pokemon that needs a special breeding method
        if list3[1]['EvoM'] != '':
            evo4 = tkinter.Label(evolframe, text=list3[1]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
            evo4.grid(row=0, column=3, pady=4, sticky='n')
        # Gigantamax arrow
        arrow1 = imagesize(adb, awr, ahr)
        canvasA1 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awr / 2, 17, image=arrow1)
        canvasA1.grid(row=0, column=5)
        # Gigantamax Label
        evo1 = tkinter.Label(evolframe, text='Gigantamax', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=5, pady=4, sticky='s')
        # Gigantamax Sprite
        sprite2 = imagesize(list3[1]['SpriteG'], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=6)
        # Creates all down arrows
        arrow2 = imagesize(ad, adw, adw)
        canvasA2 = tkinter.Canvas(evolframe, width=adw, height=adh, bg='#333333', highlightthickness=0)
        canvasA2.create_image(adw / 2, adh / 2, image=arrow2)
        canvasA2.grid(row=1, column=0)
        canvasA3 = tkinter.Canvas(evolframe, width=adw, height=adh, bg='#333333', highlightthickness=0)
        canvasA3.create_image(adw / 2, adh / 2, image=arrow2)
        canvasA3.grid(row=1, column=1)
        canvasA4 = tkinter.Canvas(evolframe, width=adw, height=adh, bg='#333333', highlightthickness=0)
        canvasA4.create_image(adw / 2, adh / 2, image=arrow2)
        canvasA4.grid(row=1, column=2)
        canvasA5 = tkinter.Canvas(evolframe, width=adw, height=adh, bg='#333333', highlightthickness=0)
        canvasA5.create_image(adw / 2, adh / 2, image=arrow2)
        canvasA5.grid(row=1, column=3)
        canvasA6 = tkinter.Canvas(evolframe, width=adw, height=adh, bg='#333333', highlightthickness=0)
        canvasA6.create_image(adw / 2, adh / 2, image=arrow2)
        canvasA6.grid(row=1, column=5)
        canvasA7 = tkinter.Canvas(evolframe, width=adw, height=adh, bg='#333333', highlightthickness=0)
        canvasA7.create_image(adw / 2, adh / 2, image=arrow2)
        canvasA7.grid(row=1, column=6)
        canvasA8 = tkinter.Canvas(evolframe, width=adw, height=adh, bg='#333333', highlightthickness=0)
        canvasA8.create_image(adw / 2, adh / 2, image=arrow2)
        canvasA8.grid(row=1, column=7)
        canvasA9 = tkinter.Canvas(evolframe, width=adw, height=adh, bg='#333333', highlightthickness=0)
        canvasA9.create_image(adw / 2, adh / 2, image=arrow2)
        canvasA9.grid(row=1, column=8)
        # Second Sprite
        sprite3 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(w / 2, h / 2, image=sprite3)
        canvasE3.grid(row=2, column=0)
        # Second Evolution method Label
        evo2 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=1, column=0, pady=4)
        # Third Sprite
        sprite4 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE4.create_image(w / 2, h / 2, image=sprite4)
        canvasE4.grid(row=2, column=1)
        # Third Evolution method Label
        evo3 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo3.grid(row=1, column=1, pady=4)
        # Fourth Sprite
        sprite5 = imagesize(list3[4]['SpriteForm'][place][0], w, h)
        canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE5.create_image(w / 2, h / 2, image=sprite5)
        canvasE5.grid(row=2, column=2)
        # Fourth Evolution method Label
        evo4 = tkinter.Label(evolframe, text=list3[4]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo4.grid(row=1, column=2, pady=4)
        # Fifth Sprite
        sprite6 = imagesize(list3[5]['SpriteForm'][place][0], w, h)
        canvasE6 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE6.create_image(w / 2, h / 2, image=sprite6)
        canvasE6.grid(row=2, column=3)
        # Fifth Evolution method Label
        evo5 = tkinter.Label(evolframe, text=list3[5]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo5.grid(row=1, column=3, pady=4)
        # Sixth Sprite
        sprite7 = imagesize(list3[6]['SpriteForm'][place][0], w, h)
        canvasE7 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE7.create_image(w / 2, h / 2, image=sprite7)
        canvasE7.grid(row=2, column=5)
        # Sixth Evolution method Label
        evo6 = tkinter.Label(evolframe, text=list3[6]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo6.grid(row=1, column=5, pady=4)
        # Seventh Sprite
        sprite8 = imagesize(list3[7]['SpriteForm'][place][0], w, h)
        canvasE8 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE8.create_image(w / 2, h / 2, image=sprite8)
        canvasE8.grid(row=2, column=6)
        # Seventh Evolution method Label
        evo7 = tkinter.Label(evolframe, text=list3[7]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo7.grid(row=1, column=6, pady=4)
        # Eighth Sprite
        sprite9 = imagesize(list3[8]['SpriteForm'][place][0], w, h)
        canvasE9 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE9.create_image(w / 2, h / 2, image=sprite9)
        canvasE9.grid(row=2, column=7)
        # Eighth Evolution method Label
        evo8 = tkinter.Label(evolframe, text=list3[8]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo8.grid(row=1, column=7, pady=4)
        # Ninth Sprite
        sprite10 = imagesize(list3[9]['SpriteForm'][place][0], w, h)
        canvasE10 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE10.create_image(w / 2, h / 2, image=sprite10)
        canvasE10.grid(row=2, column=8)
        # Ninth Evolution method Label
        evo9 = tkinter.Label(evolframe, text=list3[9]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo9.grid(row=1, column=8, pady=4)
    elif list2[press]['TreeT'] == 'I':
        # evolution tree 1-2-3-M
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                else:
                    pass
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize=10, weight=1)
        evolframe.pack()

        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=0, column=0)

        arrow1 = imagesize(ar, awr, ahr)
        canvasA1 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awr / 2, 17, image=arrow1)
        canvasA1.grid(row=0, column=1)

        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='s')

        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)

        canvasA2 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awr / 2, 17, image=arrow1)
        canvasA2.grid(row=0, column=3)

        evo2 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=0, column=3, pady=4, sticky='s')

        sprite3 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(42, h / 2, image=sprite3)
        canvasE3.grid(row=0, column=4)

        arrow2 = imagesize(adb, awdb, ahdb)
        canvasA3 = tkinter.Canvas(evolframe, width=awdb, height=ahdb, bg='#333333', highlightthickness=0)
        canvasA3.create_image(awdb/2, ahdb/2, image=arrow2)
        canvasA3.grid(row=0, column=5)

        evo3 = tkinter.Label(evolframe, text='Mega Evolve', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo3.grid(row=0, column=5, pady=4, sticky='s')

        if len(list3[3]['SpriteM']) == 1:
            sprite4 = list3[3]['SpriteM'][0]
            sprite4 = imagesize(sprite4, w, h)
            canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE4.create_image(42, h / 2, image=sprite4)
            canvasE4.grid(row=0, column=6)
        else:
            sprite4 = list3[3]['SpriteM'][0]
            sprite5 = list3[3]['SpriteM'][1]
            sprite4 = imagesize(sprite4, w, h)
            sprite5 = imagesize(sprite5, w, h)
            canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE4.create_image(42, h / 2, image=sprite4)
            canvasE4.grid(row=0, column=6)
            canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE5.create_image(42, h / 2, image=sprite5)
            canvasE5.grid(row=0, column=7)
    elif list2[press]['TreeT'] == 'J':
        # evolution tree 1-2-3-G
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                else:
                    pass
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize=10, weight=1)
        evolframe.pack()

        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=0, column=0)

        arrow1 = imagesize(ar, awr, ahr)
        canvasA1 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awr / 2, 17, image=arrow1)
        canvasA1.grid(row=0, column=1)

        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='s')

        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)

        canvasA2 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awr / 2, 17, image=arrow1)
        canvasA2.grid(row=0, column=3)

        evo2 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=0, column=3, pady=4, sticky='s')

        sprite3 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(42, h / 2, image=sprite3)
        canvasE3.grid(row=0, column=4)

        arrow2 = imagesize(adb, awdb, ahdb)
        canvasA3 = tkinter.Canvas(evolframe, width=awdb, height=ahdb, bg='#333333', highlightthickness=0)
        canvasA3.create_image(awdb / 2, ahdb / 2, image=arrow2)
        canvasA3.grid(row=0, column=5)

        evo3 = tkinter.Label(evolframe, text='Gigantamax', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo3.grid(row=0, column=5, pady=4, sticky='s')

        sprite4 = list3[3]['SpriteG']
        sprite4 = imagesize(sprite4, w, h)
        canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE4.create_image(42, h / 2, image=sprite4)
        canvasE4.grid(row=0, column=6)
    elif list2[press]['TreeT'] == 'K':
        # evolution tree 1-2-3-M/G
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                else:
                    pass
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize=10, weight=1)
        evolframe.pack()

        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)

        arrow1 = imagesize(ar, awr, ahr)
        canvasA1 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awr / 2, 17, image=arrow1)
        canvasA1.grid(row=1, column=1)

        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=1, column=1, pady=4, sticky='s')

        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=1, column=2)

        canvasA2 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awr / 2, 17, image=arrow1)
        canvasA2.grid(row=1, column=3)

        evo2 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=1, column=3, pady=4, sticky='s')

        sprite3 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(42, h / 2, image=sprite3)
        canvasE3.grid(row=1, column=4)

        arrow3 = imagesize(adbu, awdbud, ahdbud)
        canvasA3 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA3.create_image(awdbud / 2, ahdbud/2, image=arrow3)
        canvasA3.grid(row=0, column=5, sticky='e', rowspan=2)

        arrow4 = imagesize(adbd, awdbud, ahdbud)
        canvasA4 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA4.create_image(awdbud/2, ahdbud/2, image=arrow4)
        canvasA4.grid(row=1, column=5, sticky='e', rowspan=2)

        evo3 = tkinter.Label(evolframe, text='Mega Evolve', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo3.grid(row=0, column=5, pady=4)

        if len(list3[3]['SpriteM']) == 1:
            sprite4 = list3[3]['SpriteM'][0]
            sprite4 = imagesize(sprite4, w, h)
            canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE4.create_image(42, h / 2, image=sprite4)
            canvasE4.grid(row=0, column=6)
        else:
            sprite4 = list3[3]['SpriteM'][0]
            sprite5 = list3[3]['SpriteM'][1]
            sprite4 = imagesize(sprite4, w, h)
            sprite5 = imagesize(sprite5, w, h)
            canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE4.create_image(42, h / 2, image=sprite4)
            canvasE4.grid(row=0, column=6)
            canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE5.create_image(42, h / 2, image=sprite5)
            canvasE5.grid(row=0, column=7)

        evo4 = tkinter.Label(evolframe, text='Gigantamax', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo4.grid(row=2, column=5, pady=4)

        sprite6 = imagesize(list3[3]['SpriteG'], w, h)
        canvasE6 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE6.create_image(42, h / 2, image=sprite6)
        canvasE6.grid(row=2, column=6)
    elif list2[press]['TreeT'] == 'L':
        # evolution tree 1-222/2
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                elif list1[i]['Placement'] == 'D':
                    list3[4] = list1[i]
                elif list1[i]['Placement'] == 'E':
                    list3[5] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)
        # If there is a baby pokemon that needs a special breeding method
        if list3[1]['EvoM'] != '':
            evo4 = tkinter.Label(evolframe, text=list3[1]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
            evo4.grid(row=2, column=0, pady=4, sticky='n')
        # first arrow
        arrow1 = imagesize(aur, awdbud, ahdbud)
        canvasA1 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdbud / 2, ahdbud / 2, image=arrow1)
        canvasA1.grid(row=0, column=1, sticky='e', rowspan=2)
        # Second arrow
        arrow2 = imagesize(adr, awdbud, ahdbud)
        canvasA2 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdbud / 2, ahdbud / 2, image=arrow2)
        canvasA2.grid(row=1, column=1, sticky='e', rowspan=2)
        # First to second evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4)
        # Second Evolution Sprite
        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)
        # Third bottom evolution sprite
        sprite3 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(42, h / 2, image=sprite3)
        canvasE3.grid(row=0, column=3)
        # Third bottom evolution sprite
        sprite4 = imagesize(list3[4]['SpriteForm'][place][0], w, h)
        canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE4.create_image(42, h / 2, image=sprite4)
        canvasE4.grid(row=0, column=4)
        # Second to third bottom evolution method
        evo2 = tkinter.Label(evolframe, text=list3[5]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=2, column=1, pady=4)
        # Third bottom evolution sprite
        sprite5 = imagesize(list3[5]['SpriteForm'][place][0], w, h)
        canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE5.create_image(42, h / 2, image=sprite5)
        canvasE5.grid(row=2, column=2)
    elif list2[press]['TreeT'] == 'M':
        # evolution tree 1-G
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                else:
                    pass
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.pack()

        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=0, column=0)

        arrow1 = imagesize(adb, awdb, ahdb)
        canvasA1 = tkinter.Canvas(evolframe, width=awdb, height=ahdb, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdb / 2, ahdb / 2, image=arrow1)
        canvasA1.grid(row=0, column=1)

        evo1 = tkinter.Label(evolframe, text='Gigantamax', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='s')

        sprite2 = imagesize(list3[1]['SpriteG'], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(42, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)
    elif list2[press]['TreeT'] == 'N':
        # evolution tree 1-2-M
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                else:
                    pass
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)
        evolframe.pack()

        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=0, column=0)

        arrow1 = imagesize(ar, awr, ahr)
        canvasA1 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awr / 2, 17, image=arrow1)
        canvasA1.grid(row=0, column=1)

        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='s')

        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)

        arrow2 = imagesize(adb, awdb, ahdb)
        canvasA2 = tkinter.Canvas(evolframe, width=awdb, height=ahdb, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdb / 2, ahdb / 2, image=arrow2)
        canvasA2.grid(row=0, column=3)

        evo2 = tkinter.Label(evolframe, text='Mega Evolve', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=0, column=3, pady=4, sticky='s')

        if len(list3[2]['SpriteM']) == 1:
            sprite3 = list3[2]['SpriteM'][0]
            sprite3 = imagesize(sprite3, w, h)
            canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE3.create_image(42, h / 2, image=sprite3)
            canvasE3.grid(row=0, column=4)
        else:
            sprite3 = list3[2]['SpriteM'][0]
            sprite4 = list3[2]['SpriteM'][1]
            sprite3 = imagesize(sprite3, w, h)
            sprite4 = imagesize(sprite4, w, h)
            canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE3.create_image(42, h / 2, image=sprite3)
            canvasE3.grid(row=0, column=4)
            canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE4.create_image(42, h / 2, image=sprite4)
            canvasE4.grid(row=0, column=5)
    elif list2[press]['TreeT'] == 'O':
        # evolution tree 1-2-M/2
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)
        # first arrow
        arrow1 = imagesize(aur, awdbud, ahdbud)
        canvasA1 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdbud / 2, ahdbud / 2, image=arrow1)
        canvasA1.grid(row=0, column=1, sticky='e', rowspan=2)
        # Second arrow
        arrow2 = imagesize(adr, awdbud, ahdbud)
        canvasA2 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdbud / 2, ahdbud / 2, image=arrow2)
        canvasA2.grid(row=1, column=1, sticky='e', rowspan=2)
        # First to second evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4)
        # Second Evolution Sprite
        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)

        arrow3 = imagesize(adb, awdb, ahdb)
        canvasA3 = tkinter.Canvas(evolframe, width=awdb, height=ahdb, bg='#333333', highlightthickness=0)
        canvasA3.create_image(awdb / 2, ahdb / 2, image=arrow3)
        canvasA3.grid(row=0, column=3)

        evo2 = tkinter.Label(evolframe, text='Mega Evolve', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=0, column=3, pady=4, sticky='s')

        if len(list3[2]['SpriteM']) == 1:
            sprite3 = list3[2]['SpriteM'][0]
            sprite3 = imagesize(sprite3, w, h)
            canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE3.create_image(42, h / 2, image=sprite3)
            canvasE3.grid(row=0, column=4)
        else:
            sprite3 = list3[2]['SpriteM'][0]
            sprite4 = list3[2]['SpriteM'][1]
            sprite3 = imagesize(sprite3, w, h)
            sprite4 = imagesize(sprite4, w, h)
            canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE3.create_image(42, h / 2, image=sprite3)
            canvasE3.grid(row=0, column=4)
            canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE4.create_image(42, h / 2, image=sprite4)
            canvasE4.grid(row=0, column=5)
        # Second to third bottom evolution method
        evo3 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo3.grid(row=2, column=1, pady=4)
        # Third bottom evolution sprite
        sprite5 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE5.create_image(42, h / 2, image=sprite5)
        canvasE5.grid(row=2, column=2)
    elif list2[press]['TreeT'] == 'P':
        # evolution tree 1
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                else:
                    pass
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0], minsize=10, weight=1)
        evolframe.columnconfigure([0], minsize=10, weight=1)
        evolframe.pack()

        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=0, column=0)
    elif list2[press]['TreeT'] == 'Q':
        # evolution tree 1-2-G
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                else:
                    pass
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)
        evolframe.pack()

        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=0, column=0)
        # If there is a baby pokemon that needs a special breeding method
        if list3[1]['EvoM'] != '':
            evo3 = tkinter.Label(evolframe, text=list3[1]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
            evo3.grid(row=1, column=0, pady=4, sticky='n')
        arrow1 = imagesize(ar, awr, ahr)
        canvasA1 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awr / 2, 17, image=arrow1)
        canvasA1.grid(row=0, column=1)

        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='s')

        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)

        arrow2 = imagesize(adb, awdb, ahdb)
        canvasA2 = tkinter.Canvas(evolframe, width=awdb, height=ahdb, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdb / 2, ahdb / 2, image=arrow2)
        canvasA2.grid(row=0, column=3)

        evo2 = tkinter.Label(evolframe, text='Gigantamax', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=0, column=3, pady=4, sticky='s')

        sprite3 = imagesize(list3[2]['SpriteG'], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(42, h / 2, image=sprite3)
        canvasE3.grid(row=0, column=4)
    elif list2[press]['TreeT'] == 'R':
        # evolution tree 1-M
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                else:
                    pass
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.pack()

        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=0, column=0)

        arrow1 = imagesize(adb, awdb, ahdb)
        canvasA1 = tkinter.Canvas(evolframe, width=awdb, height=ahdb, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdb / 2, ahdb / 2, image=arrow1)
        canvasA1.grid(row=0, column=1)

        evo1 = tkinter.Label(evolframe, text='Mega Evolve', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='s')

        if len(list3[1]['SpriteM']) == 1:
            sprite2 = list3[1]['SpriteM'][0]
            sprite2 = imagesize(sprite2, w, h)
            canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE2.create_image(42, h / 2, image=sprite2)
            canvasE2.grid(row=0, column=2)
        else:
            sprite2 = list3[1]['SpriteM'][0]
            sprite3 = list3[1]['SpriteM'][1]
            sprite2 = imagesize(sprite2, w, h)
            sprite3 = imagesize(sprite3, w, h)
            canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE2.create_image(42, h / 2, image=sprite2)
            canvasE2.grid(row=0, column=2)
            canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE3.create_image(42, h / 2, image=sprite3)
            canvasE3.grid(row=0, column=3)
    elif list2[press]['TreeT'] == 'S':
        # evolution tree 1-2/2/G
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                elif list1[i]['Placement'] == 'D':
                    list3[4] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)
        # first arrow
        arrow1 = imagesize(ar, awdbud, ahdbud)
        canvasA1 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdbud / 2, ahdbud / 2, image=arrow1)
        canvasA1.grid(row=1, column=1)
        # First to second top evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=1, column=1, pady=4, sticky='s')

        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=1, column=2)

        arrow2 = imagesize(aur, awdbud, ahdbud)
        canvasA2 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdbud / 2, ahdbud / 2, image=arrow2)
        canvasA2.grid(row=0, column=3, sticky='s')
        # Second arrow
        arrow3 = imagesize(ar, awdbud, ahdbud)
        canvasA3 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA3.create_image(awdbud / 2, ahdbud / 2, image=arrow3)
        canvasA3.grid(row=1, column=3, sticky='e')
        # Third arrow
        arrow4 = imagesize(adbd, awdbud, ahdbud)
        canvasA4 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA4.create_image(awdbud / 2, ahdbud / 2, image=arrow4)
        canvasA4.grid(row=2, column=3, sticky='n')
        # First to second top evolution method
        evo2 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=0, column=3, pady=4, sticky='n')
        # Second Evolution Sprite
        sprite3 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(w / 2, h / 2, image=sprite3)
        canvasE3.grid(row=0, column=4)
        # first to second middle evolution method
        evo3 = tkinter.Label(evolframe, text=list3[4]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo3.grid(row=1, column=3, pady=4)
        # Third top evolution sprite
        sprite4 = imagesize(list3[4]['SpriteForm'][place][0], w, h)
        canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE4.create_image(42, h / 2, image=sprite4)
        canvasE4.grid(row=1, column=4)
        # Fir Second to Third top evolution method
        evo4 = tkinter.Label(evolframe, text='Gigantamax', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo4.grid(row=2, column=3, pady=4, sticky='s')
        # Third top evolution sprite
        sprite5 = imagesize(list3[2]['SpriteG'], w, h)
        canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE5.create_image(42, h / 2, image=sprite5)
        canvasE5.grid(row=2, column=4)
    elif list2[press]['TreeT'] == 'T':
        # evolution 1-22
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=0, column=0)
        # If there is a baby pokemon that needs a special breeding method
        if list3[1]['EvoM'] != '':
            evo2 = tkinter.Label(evolframe, text=list3[1]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
            evo2.grid(row=0, column=0, pady=4, sticky='n')
        # first arrow
        arrow1 = imagesize(ar, awdbud, ahdbud)
        canvasA1 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdbud / 2, ahdbud / 2, image=arrow1)
        canvasA1.grid(row=0, column=1, sticky='e')
        # First to second evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='s')
        # Second Evolution Sprite
        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)
        # Third bottom evolution sprite
        sprite3 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(42, h / 2, image=sprite3)
        canvasE3.grid(row=0, column=3)
    elif list2[press]['TreeT'] == 'U':
        # evolution tree 1-2-3-M/3-M
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                elif list1[i]['Placement'] == 'D':
                    list3[4] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)
        # first arrow
        arrow1 = imagesize(ar, awr, ahr)
        canvasA1 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awr / 2, 17, image=arrow1)
        canvasA1.grid(row=1, column=1)
        # First to second evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=1, column=1, pady=4, sticky='s')
        # Second Evolution Sprite
        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=1, column=2)
        # Second arrow
        arrow2 = imagesize(adbu, awdbud, ahdbud)
        canvasA2 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdbud / 2, ahdbud / 2, image=arrow2)
        canvasA2.grid(row=0, column=3, sticky='e', rowspan=2)
        # Third arrow
        arrow3 = imagesize(adbd, awdbud, ahdbud)
        canvasA3 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA3.create_image(awdbud / 2, ahdbud / 2, image=arrow3)
        canvasA3.grid(row=1, column=3, sticky='e', rowspan=2)
        # Second to Third top evolution method
        evo2 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=0, column=3, pady=4)
        # Third top evolution sprite
        sprite4 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE4.create_image(42, h / 2, image=sprite4)
        canvasE4.grid(row=0, column=4)
        # Second to third bottom evolution method
        evo3 = tkinter.Label(evolframe, text=list3[4]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo3.grid(row=2, column=3, pady=4)
        # Third bottom evolution sprite
        sprite5 = imagesize(list3[4]['SpriteForm'][place][0], w, h)
        canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE5.create_image(42, h / 2, image=sprite5)
        canvasE5.grid(row=2, column=4)

        arrow4 = imagesize(adb, awdbud, ahdbud)
        canvasA4 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA4.create_image(awdbud / 2, ahdbud / 2, image=arrow4)
        canvasA4.grid(row=0, column=5, sticky='e')

        arrow5 = imagesize(adb, awdbud, ahdbud)
        canvasA5 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA5.create_image(awdbud / 2, ahdbud / 2, image=arrow5)
        canvasA5.grid(row=2, column=5, sticky='e')

        evo4 = tkinter.Label(evolframe, text='Mega Evolve', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo4.grid(row=0, column=5, sticky='s')

        if len(list3[3]['SpriteM']) == 1:
            sprite6 = list3[3]['SpriteM'][0]
            sprite6 = imagesize(sprite6, w, h)
            canvasE6 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE6.create_image(42, h / 2, image=sprite6)
            canvasE6.grid(row=0, column=6)
        else:
            sprite6 = list3[3]['SpriteM'][0]
            sprite7 = list3[3]['SpriteM'][1]
            sprite6 = imagesize(sprite6, w, h)
            sprite7 = imagesize(sprite7, w, h)
            canvasE6 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE6.create_image(42, h / 2, image=sprite6)
            canvasE6.grid(row=0, column=6)
            canvasE7 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE7.create_image(42, h / 2, image=sprite7)
            canvasE7.grid(row=0, column=7)

        evo5 = tkinter.Label(evolframe, text='Mega Evolve', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo5.grid(row=2, column=5, sticky='s')

        if len(list3[4]['SpriteM']) == 1:
            sprite8 = list3[4]['SpriteM'][0]
            sprite8 = imagesize(sprite8, w, h)
            canvasE8 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE8.create_image(42, h / 2, image=sprite8)
            canvasE8.grid(row=2, column=6)
        else:
            sprite8 = list3[4]['SpriteM'][0]
            sprite9 = list3[4]['SpriteM'][1]
            sprite8 = imagesize(sprite8, w, h)
            sprite9 = imagesize(sprite9, w, h)
            canvasE8 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE8.create_image(42, h / 2, image=sprite8)
            canvasE8.grid(row=2, column=6)
            canvasE9 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
            canvasE9.create_image(42, h / 2, image=sprite9)
            canvasE9.grid(row=2, column=7)
    elif list2[press]['TreeT'] == 'V':
        # evolution tree 1-2/G
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)
        # first arrow
        arrow1 = imagesize(aur, awdbud, ahdbud)
        canvasA1 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdbud / 2, ahdbud / 2, image=arrow1)
        canvasA1.grid(row=0, column=1, sticky='e', rowspan=2)
        # Second arrow
        arrow2 = imagesize(adr, awdbud, ahdbud)
        canvasA2 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdbud / 2, ahdbud / 2, image=arrow2)
        canvasA2.grid(row=1, column=1, sticky='e', rowspan=2)
        # First to second evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4)
        # Second Evolution Sprite
        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)
        # Second to Third top evolution method
        evo2 = tkinter.Label(evolframe, text='Gigantamax', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=2, column=1, pady=4)
        # Third top evolution sprite
        sprite3 = imagesize(list3[1]['SpriteG'], w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(42, h / 2, image=sprite3)
        canvasE3.grid(row=2, column=2)
    elif list2[press]['TreeT'] == 'W':
        # evolution tree 1-2-G/2-G
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)
        # first arrow
        arrow1 = imagesize(aur, awdbud, ahdbud)
        canvasA1 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdbud / 2, ahdbud / 2, image=arrow1)
        canvasA1.grid(row=0, column=1, sticky='e', rowspan=2)
        # Second arrow
        arrow2 = imagesize(adr, awdbud, ahdbud)
        canvasA2 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdbud / 2, ahdbud / 2, image=arrow2)
        canvasA2.grid(row=1, column=1, sticky='e', rowspan=2)
        # First to second evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='n')
        # Second Evolution Sprite
        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)

        arrow3 = imagesize(adb, awdb, ahdb)
        canvasA3 = tkinter.Canvas(evolframe, width=awdb, height=ahdb, bg='#333333', highlightthickness=0)
        canvasA3.create_image(awdb / 2, ahdb / 2, image=arrow3)
        canvasA3.grid(row=0, column=3)

        evo2 = tkinter.Label(evolframe, text='Gigantamax', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=0, column=3, pady=4, sticky='s')

        sprite3 = list3[2]['SpriteG']
        sprite3 = imagesize(sprite3, w, h)
        canvasE3 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE3.create_image(42, h / 2, image=sprite3)
        canvasE3.grid(row=0, column=4)

        # Second to third bottom evolution method
        evo3 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo3.grid(row=2, column=1, pady=4)
        # Third bottom evolution sprite
        sprite4 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE4.create_image(42, h / 2, image=sprite4)
        canvasE4.grid(row=2, column=2)

        arrow4 = imagesize(adb, awdb, ahdb)
        canvasA4 = tkinter.Canvas(evolframe, width=awdb, height=ahdb, bg='#333333', highlightthickness=0)
        canvasA4.create_image(awdb / 2, ahdb / 2, image=arrow3)
        canvasA4.grid(row=2, column=3)

        evo4 = tkinter.Label(evolframe, text='Gigantamax', wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo4.grid(row=2, column=3, pady=4, sticky='s')

        sprite5 = list3[3]['SpriteG']
        sprite5 = imagesize(sprite5, w, h)
        canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE5.create_image(42, h / 2, image=sprite5)
        canvasE5.grid(row=2, column=4)
    elif list2[press]['TreeT'] == 'X':
        # Unused
        evolframe = tkinter.Frame(framebottom)
        pass
    elif list2[press]['TreeT'] == 'Y':
        # evolution tree 1-2/2+3
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                elif list1[i]['Placement'] == 'C':
                    list3[3] = list1[i]
                else:
                    pass
        # Sets the frame up
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2, 3], minsize=10, weight=1)
        evolframe.pack()
        # First Evolution Sprite
        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=1, column=0)
        # If there is a baby pokemon that needs a special breeding method
        if list3[1]['EvoM'] != '':
            evo3 = tkinter.Label(evolframe, text=list3[1]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
            evo3.grid(row=2, column=0, pady=4, sticky='n')
        # first arrow
        arrow1 = imagesize(aur, awdbud, ahdbud)
        canvasA1 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awdbud / 2, ahdbud / 2, image=arrow1)
        canvasA1.grid(row=0, column=1, sticky='e', rowspan=2)
        # Second arrow
        arrow2 = imagesize(adr, awdbud, ahdbud)
        canvasA2 = tkinter.Canvas(evolframe, width=awdbud, height=ahdbud, bg='#333333', highlightthickness=0)
        canvasA2.create_image(awdbud / 2, ahdbud / 2, image=arrow2)
        canvasA2.grid(row=1, column=1, sticky='e', rowspan=2)
        # First to second evolution method
        evo1 = tkinter.Label(evolframe, text=list3[2]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='n')
        # Second Evolution Sprite
        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)
        # Second to third bottom evolution method
        evo2 = tkinter.Label(evolframe, text=list3[3]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo2.grid(row=2, column=1, pady=4)
        # Third bottom evolution sprite
        sprite4 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE4 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE4.create_image(42, h / 2, image=sprite4)
        canvasE4.grid(row=2, column=2)
        # Third bottom evolution sprite
        sprite5 = imagesize(list3[3]['SpriteForm'][place][0], w, h)
        canvasE5 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE5.create_image(42, h / 2, image=sprite5)
        canvasE5.grid(row=2, column=3)
    elif list2[press]['TreeT'] == 'Z':
        # Shows multiple forms
        evolframe = tkinter.Frame(framebottom)
        pass
    elif list2[press]['TreeT'] == 'AA':
        # evolution tree 1<-2
        h = 80
        w = 80
        group = list2[press]['Group']
        for i in list1.keys():
            if group == list1[i]['Group']:
                if list1[i]['Placement'] == 'A':
                    list3[1] = list1[i]
                elif list1[i]['Placement'] == 'B':
                    list3[2] = list1[i]
                else:
                    pass
        evolframe = tkinter.Frame(framebottom, bg='#333333')
        evolframe.rowconfigure([0], minsize=10, weight=1)
        evolframe.columnconfigure([0, 1, 2], minsize=10, weight=1)
        evolframe.pack()

        sprite1 = imagesize(list3[1]['SpriteForm'][place][0], w, h)
        canvasE1 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE1.create_image(w / 2, h / 2, image=sprite1)
        canvasE1.grid(row=0, column=0)

        arrow1 = Image.open(ar)
        arrow1 = arrow1.resize((awr, ahr), Image.ANTIALIAS)
        arrow1 = arrow1.transpose(method=Image.FLIP_LEFT_RIGHT)
        arrow1 = ImageTk.PhotoImage(arrow1)
        canvasA1 = tkinter.Canvas(evolframe, width=awr, height=ahr, bg='#333333', highlightthickness=0)
        canvasA1.create_image(awr / 2, 17, image=arrow1)
        canvasA1.grid(row=0, column=1)

        evo1 = tkinter.Label(evolframe, text=list3[1]['EvoM'], wraplength=awr, bg='#333333', fg='#FFFFFF')
        evo1.grid(row=0, column=1, pady=4, sticky='s')

        sprite2 = imagesize(list3[2]['SpriteForm'][place][0], w, h)
        canvasE2 = tkinter.Canvas(evolframe, width=w, height=h, bg='#333333', highlightthickness=0)
        canvasE2.create_image(w / 2, h / 2, image=sprite2)
        canvasE2.grid(row=0, column=2)
    else:
        pass


def menustart():
    # Menubuttons for Pokedex Entry Change
    global entrychangebutton1, entrychangebutton2, entrychangebutton3, entrychangebutton4
    global entrychangebutton5, entrychangebutton6, entrychangebutton7, entrychangebutton8
    entrychangebutton1 = tkinter.Menubutton(framebottommenu, text='Gen 1', relief='raised', bg='#4DED30')
    entrychangebutton1.config(activebackground='#26D701')
    entrychangebutton1.menu = tkinter.Menu(entrychangebutton1, tearoff=0)
    entrychangebutton1['menu'] = entrychangebutton1.menu
    entrychangebutton1.menu.add_command(label="Red/Blue", command=RB)
    entrychangebutton1.menu.add_command(label="Yellow", command=Y)
    entrychangebutton1.menu.add_command(label="Let's Go Pikachu/Eevee", command=LGP)

    entrychangebutton2 = tkinter.Menubutton(framebottommenu, text='Gen 2', relief='raised', bg='#4DED30')
    entrychangebutton2.config(activebackground='#26D701')
    entrychangebutton2.menu = tkinter.Menu(entrychangebutton2, tearoff=0)
    entrychangebutton2['menu'] = entrychangebutton2.menu
    entrychangebutton2.menu.add_command(label="Gold", command=G)
    entrychangebutton2.menu.add_command(label="Silver", command=Sil)
    entrychangebutton2.menu.add_command(label="Crystal", command=C)

    entrychangebutton3 = tkinter.Menubutton(framebottommenu, text='Gen 3', relief='raised', bg='#4DED30')
    entrychangebutton3.config(activebackground='#26D701')
    entrychangebutton3.menu = tkinter.Menu(entrychangebutton3, tearoff=0)
    entrychangebutton3['menu'] = entrychangebutton3.menu
    entrychangebutton3.menu.add_command(label="Ruby", command=R)
    entrychangebutton3.menu.add_command(label="Sapphire", command=Sap)
    entrychangebutton3.menu.add_command(label="Emerald", command=E)
    entrychangebutton3.menu.add_command(label="Fire Red", command=FR)
    entrychangebutton3.menu.add_command(label="Leaf Green", command=LG)

    entrychangebutton4 = tkinter.Menubutton(framebottommenu, text='Gen 4', relief='raised', bg='#4DED30')
    entrychangebutton4.config(activebackground='#26D701')
    entrychangebutton4.menu = tkinter.Menu(entrychangebutton4, tearoff=0)
    entrychangebutton4['menu'] = entrychangebutton4.menu
    entrychangebutton4.menu.add_command(label="Diamond", command=D)
    entrychangebutton4.menu.add_command(label="Pearl", command=Pearl)
    entrychangebutton4.menu.add_command(label="Platinum", command=Plat)
    entrychangebutton4.menu.add_command(label="Heart Gold", command=HG)
    entrychangebutton4.menu.add_command(label="Soul Silver", command=SS)

    entrychangebutton5 = tkinter.Menubutton(framebottommenu, text='Gen 5', relief='raised', bg='#4DED30')
    entrychangebutton5.config(activebackground='#26D701')
    entrychangebutton5.menu = tkinter.Menu(entrychangebutton5, tearoff=0)
    entrychangebutton5['menu'] = entrychangebutton5.menu
    entrychangebutton5.menu.add_command(label="Black", command=B)
    entrychangebutton5.menu.add_command(label="White", command=W)
    entrychangebutton5.menu.add_command(label="Black2/White2", command=B2)

    entrychangebutton6 = tkinter.Menubutton(framebottommenu, text='Gen 6', relief='raised', bg='#4DED30')
    entrychangebutton6.config(activebackground='#26D701')
    entrychangebutton6.menu = tkinter.Menu(entrychangebutton6, tearoff=0)
    entrychangebutton6['menu'] = entrychangebutton6.menu
    entrychangebutton6.menu.add_command(label="X", command=X)
    entrychangebutton6.menu.add_command(label="Y", command=Yg)
    entrychangebutton6.menu.add_command(label="Omega Ruby", command=OR)
    entrychangebutton6.menu.add_command(label="Alpha Sapphire", command=AS)

    entrychangebutton7 = tkinter.Menubutton(framebottommenu, text='Gen 7', relief='raised', bg='#4DED30')
    entrychangebutton7.config(activebackground='#26D701')
    entrychangebutton7.menu = tkinter.Menu(entrychangebutton7, tearoff=0)
    entrychangebutton7['menu'] = entrychangebutton7.menu
    entrychangebutton7.menu.add_command(label="Sun", command=Sun)
    entrychangebutton7.menu.add_command(label="Moon", command=M)
    entrychangebutton7.menu.add_command(label="Ultra Sun", command=US)
    entrychangebutton7.menu.add_command(label="Ultra Moon", command=UM)

    entrychangebutton8 = tkinter.Menubutton(framebottommenu, text='Gen 8', relief='raised', bg='#4DED30')
    entrychangebutton8.config(activebackground='#26D701')
    entrychangebutton8.menu = tkinter.Menu(entrychangebutton8, tearoff=0)
    entrychangebutton8['menu'] = entrychangebutton8.menu
    entrychangebutton8.menu.add_command(label="Sword", command=Sword)
    entrychangebutton8.menu.add_command(label="Shield", command=Shield)


def pkmtype():
    global press, list2
    global type1var, type2var
    global type1label, type2label
    global frametype1, frametype2
    typel = [list2[press]['type1'], list2[press]['type2']]
    for i in typel:
        if i == 'Normal':       # A8A77A
            norm = '#A8A77A'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=norm)
                frametype1.config(bg=norm)
            else:
                type2var.set(i)
                type2label.config(bg=norm)
                frametype2.config(bg=norm)
        elif i == 'Fire':       # EE8130
            fire = '#EE8130'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=fire)
                frametype1.config(bg=fire)
            else:
                type2var.set(i)
                type2label.config(bg=fire)
                frametype2.config(bg=fire)
        elif i == 'Water':      # 6390F0
            water = '#6390F0'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=water)
                frametype1.config(bg=water)
            else:
                type2var.set(i)
                type2label.config(bg=water)
                frametype2.config(bg=water)
        elif i == 'Electric':   # F7D02C
            elect = '#F7D02C'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=elect)
                frametype1.config(bg=elect)
            else:
                type2var.set(i)
                type2label.config(bg=elect)
                frametype2.config(bg=elect)
        elif i == 'Grass':      # 7AC74C
            grass = '#7AC74C'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=grass)
                frametype1.config(bg=grass)
            else:
                type2var.set(i)
                type2label.config(bg=grass)
                frametype2.config(bg=grass)
        elif i == 'Ice':        # 96D9D6
            ice = '#96D9D6'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=ice)
                frametype1.config(bg=ice)
            else:
                type2var.set(i)
                type2label.config(bg=ice)
                frametype2.config(bg=ice)
        elif i == 'Fighting':   # C22E28
            fight = '#C22E28'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=fight)
                frametype1.config(bg=fight)
            else:
                type2var.set(i)
                type2label.config(bg=fight)
                frametype2.config(bg=fight)
        elif i == 'Poison':     # A33EA1
            pois = '#A33EA1'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=pois)
                frametype1.config(bg=pois)
            else:
                type2var.set(i)
                type2label.config(bg=pois)
                frametype2.config(bg=pois)
        elif i == 'Ground':     # E2BF65
            ground = '#E2BF65'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=ground)
                frametype1.config(bg=ground)
            else:
                type2var.set(i)
                type2label.config(bg=ground)
                frametype2.config(bg=ground)
        elif i == 'Flying':     # A98FF3
            fly = '#A98FF3'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=fly)
                frametype1.config(bg=fly)
            else:
                type2var.set(i)
                type2label.config(bg=fly)
                frametype2.config(bg=fly)
        elif i == 'Psychic':    # F95587
            psy = '#F95587'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=psy)
                frametype1.config(bg=psy)
            else:
                type2var.set(i)
                type2label.config(bg=psy)
                frametype2.config(bg=psy)
        elif i == 'Bug':        # A6B91A
            bug = '#A6B91A'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=bug)
                frametype1.config(bg=bug)
            else:
                type2var.set(i)
                type2label.config(bg=bug)
                frametype2.config(bg=bug)
        elif i == 'Rock':       # B6A136
            rock = '#B6A136'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=rock)
                frametype1.config(bg=rock)
            else:
                type2var.set(i)
                type2label.config(bg=rock)
                frametype2.config(bg=rock)
        elif i == 'Ghost':      # 735797
            ghost = '#735797'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=ghost)
                frametype1.config(bg=ghost)
            else:
                type2var.set(i)
                type2label.config(bg=ghost)
                frametype2.config(bg=ghost)
        elif i == 'Dragon':     # 6F35FC
            drag = '#6F35FC'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=drag)
                frametype1.config(bg=drag)
            else:
                type2var.set(i)
                type2label.config(bg=drag)
                frametype2.config(bg=drag)
        elif i == 'Dark':       # 705746
            dark = '#705746'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=dark)
                frametype1.config(bg=dark)
            else:
                type2var.set(i)
                type2label.config(bg=dark)
                frametype2.config(bg=dark)
        elif i == 'Steel':      # B7B7CE
            steel = '#B7B7CE'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=steel)
                frametype1.config(bg=steel)
            else:
                type2var.set(i)
                type2label.config(bg=steel)
                frametype2.config(bg=steel)
        elif i == 'Fairy':      # D685AD
            fairy = '#D685AD'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=fairy)
                frametype1.config(bg=fairy)
            else:
                type2var.set(i)
                type2label.config(bg=fairy)
                frametype2.config(bg=fairy)
        else:
            pass
    if typel[1] == '':
        type2label.config(bg='blue')
        type2label.pack_forget()
        frametype2.config(bg='blue', highlightbackground='blue')
    else:
        frametype2.config(highlightbackground='black')
        frametype2.pack()
        type2label.pack()


def pkmtype2(type1, type2):
    global press, list2
    global type1var, type2var
    global type1label, type2label
    global frametype1, frametype2
    typel = [type1, type2]
    for i in typel:
        if i == 'Normal':       # A8A77A
            norm = '#A8A77A'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=norm)
                frametype1.config(bg=norm)
            else:
                type2var.set(i)
                type2label.config(bg=norm)
                frametype2.config(bg=norm)
        elif i == 'Fire':       # EE8130
            fire = '#EE8130'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=fire)
                frametype1.config(bg=fire)
            else:
                type2var.set(i)
                type2label.config(bg=fire)
                frametype2.config(bg=fire)
        elif i == 'Water':      # 6390F0
            water = '#6390F0'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=water)
                frametype1.config(bg=water)
            else:
                type2var.set(i)
                type2label.config(bg=water)
                frametype2.config(bg=water)
        elif i == 'Electric':   # F7D02C
            elect = '#F7D02C'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=elect)
                frametype1.config(bg=elect)
            else:
                type2var.set(i)
                type2label.config(bg=elect)
                frametype2.config(bg=elect)
        elif i == 'Grass':      # 7AC74C
            grass = '#7AC74C'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=grass)
                frametype1.config(bg=grass)
            else:
                type2var.set(i)
                type2label.config(bg=grass)
                frametype2.config(bg=grass)
        elif i == 'Ice':        # 96D9D6
            ice = '#96D9D6'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=ice)
                frametype1.config(bg=ice)
            else:
                type2var.set(i)
                type2label.config(bg=ice)
                frametype2.config(bg=ice)
        elif i == 'Fighting':   # C22E28
            fight = '#C22E28'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=fight)
                frametype1.config(bg=fight)
            else:
                type2var.set(i)
                type2label.config(bg=fight)
                frametype2.config(bg=fight)
        elif i == 'Poison':     # A33EA1
            pois = '#A33EA1'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=pois)
                frametype1.config(bg=pois)
            else:
                type2var.set(i)
                type2label.config(bg=pois)
                frametype2.config(bg=pois)
        elif i == 'Ground':     # E2BF65
            ground = '#E2BF65'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=ground)
                frametype1.config(bg=ground)
            else:
                type2var.set(i)
                type2label.config(bg=ground)
                frametype2.config(bg=ground)
        elif i == 'Flying':     # A98FF3
            fly = '#A98FF3'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=fly)
                frametype1.config(bg=fly)
            else:
                type2var.set(i)
                type2label.config(bg=fly)
                frametype2.config(bg=fly)
        elif i == 'Psychic':    # F95587
            psy = '#F95587'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=psy)
                frametype1.config(bg=psy)
            else:
                type2var.set(i)
                type2label.config(bg=psy)
                frametype2.config(bg=psy)
        elif i == 'Bug':        # A6B91A
            bug = '#A6B91A'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=bug)
                frametype1.config(bg=bug)
            else:
                type2var.set(i)
                type2label.config(bg=bug)
                frametype2.config(bg=bug)
        elif i == 'Rock':       # B6A136
            rock = '#B6A136'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=rock)
                frametype1.config(bg=rock)
            else:
                type2var.set(i)
                type2label.config(bg=rock)
                frametype2.config(bg=rock)
        elif i == 'Ghost':      # 735797
            ghost = '#735797'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=ghost)
                frametype1.config(bg=ghost)
            else:
                type2var.set(i)
                type2label.config(bg=ghost)
                frametype2.config(bg=ghost)
        elif i == 'Dragon':     # 6F35FC
            drag = '#6F35FC'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=drag)
                frametype1.config(bg=drag)
            else:
                type2var.set(i)
                type2label.config(bg=drag)
                frametype2.config(bg=drag)
        elif i == 'Dark':       # 705746
            dark = '#705746'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=dark)
                frametype1.config(bg=dark)
            else:
                type2var.set(i)
                type2label.config(bg=dark)
                frametype2.config(bg=dark)
        elif i == 'Steel':      # B7B7CE
            steel = '#B7B7CE'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=steel)
                frametype1.config(bg=steel)
            else:
                type2var.set(i)
                type2label.config(bg=steel)
                frametype2.config(bg=steel)
        elif i == 'Fairy':      # D685AD
            fairy = '#D685AD'
            if i == typel[0]:
                type1var.set(i)
                type1label.config(bg=fairy)
                frametype1.config(bg=fairy)
            else:
                type2var.set(i)
                type2label.config(bg=fairy)
                frametype2.config(bg=fairy)
        else:
            pass
    if typel[1] == '' or typel[1] == ' ':
        type2label.config(bg='blue')
        type2label.pack_forget()
        frametype2.config(bg='blue', highlightbackground='blue')
    else:
        frametype2.config(highlightbackground='black')
        frametype2.pack()
        type2label.pack()


def Display():
    # Runs the Pokedex code to display Pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    Poke = Dex.display(list2)           # Saves the string of Pokedex entries in Poke
    return Poke           # Displays the pokedex entries in the text window


def DisplayBase():
    # Runs the Pokedex code to display Pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    Poke = Dex.display(list1)           # Saves the string of Pokedex entries in Poke
    list2 = list1
    entry.insert("1.0", Poke)           # Displays the pokedex entries in the text window


def DisplayAlphZ():
    # Runs the Pokedex code to display Pokemon in alphabetical order Z-A
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = Dex.alpha(list2, "0")  # Saves the alphabetized list of Pokemon in Poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window
    alpha.config(text="List Alphabetically A-Z", command=DisplayAlphA)


def DisplayAlphA():
    # Runs the Pokedex code to display Pokemon in alphabetical order A-Z
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = Dex.alpha(list2, "1")  # Saves the alphabetized list of Pokemon in Poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window
    alpha.config(text="List Alphabetically Z-A", command=DisplayAlphZ)


def DisplayWgtU():
    # Runs the Pokedex code to sort the pokemon by weight lightest to heaviest
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = Dex.weight_order(list2, "1")  # Saves the weight list in poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window
    Wgt.config(text="List Weight Heaviest to Lightest", command=DisplayWgtD)


def DisplayWgtD():
    # Runs the Pokedex code to sort the pokemon by weight heaviest to lightest
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = Dex.weight_order(list2, "0")  # Saves the weight list in poke
    Poke = Display()
    entry.insert("1.0", Poke)           # displays the list in the text window
    Wgt.config(text="List Weight Lightest to Heaviest", command=DisplayWgtU)


def DisplayHgtU():
    # Runs the Pokedex code to sort the pokemon by height shortest to tallest
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = Dex.height_order(list2, "1")  # Saves the height list in Poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window
    Hgt.config(text="List Height Tallest to Shortest", command=DisplayHgtD)


def DisplayHgtD():
    # Runs the Pokedex code to sort the pokemon by height tallest to shortest
    global  list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = Dex.height_order(list2, "0")  # Saves the height list in Poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window
    Hgt.config(text="List Height Shortest to Tallest", command=DisplayHgtU)


def DisplayNumU():
    # Runs the Pokedex code to display Pokemon in numerical order upwards
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = Dex.numerical_order(list2, "1")  # Saves the alphabetized list of Pokemon in Poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window
    Num.config(text="List Numerically Decreasing", command=DisplayNumD)


def DisplayNumD():
    # Runs the Pokedex code to display Pokemon in numerical order downwards
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = Dex.numerical_order(list2, "0")  # Saves the alphabetized list of Pokemon in Poke
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window
    Num.config(text="List Numerically Increasing", command=DisplayNumU)


def DisplayRegKanto():
    # Runs the Pokedex code to display the pokemon from certain regions
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = Dex.region(list2, 'Kanto')
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window


def DisplayRegJohto():
    # Runs the Pokedex code to display the pokemon from certain regions
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    list2 = Dex.region(list2, 'Johto')
    Poke = Display()
    entry.insert("1.0", Poke)           # Displays the list in the text window


def DisplayRegHoenn():
    # Runs the Pokedex code to display the pokemon from certain regions
    global list2
    entry.delete("1.0", tkinter.END)  # Clears the text window
    list2 = Dex.region(list2, 'Hoenn')
    Poke = Display()
    entry.insert("1.0", Poke)  # Displays the list in the text window


def DisplayRegSinnoh():
    # Runs the Pokedex code to display the pokemon from certain regions
    global list2
    entry.delete("1.0", tkinter.END)  # Clears the text window
    list2 = Dex.region(list2, 'Sinnoh')
    Poke = Display()
    entry.insert("1.0", Poke)  # Displays the list in the text window


def DisplayRegUnova():
    # Runs the Pokedex code to display the pokemon from certain regions
    global list2
    entry.delete("1.0", tkinter.END)  # Clears the text window
    list2 = Dex.region(list2, 'Unova')
    Poke = Display()
    entry.insert("1.0", Poke)  # Displays the list in the text window


def DisplayRegKalos():
    # Runs the Pokedex code to display the pokemon from certain regions
    global list2
    entry.delete("1.0", tkinter.END)  # Clears the text window
    list2 = Dex.region(list2, 'Kalos')
    Poke = Display()
    entry.insert("1.0", Poke)  # Displays the list in the text window


def DisplayRegAlola():
    # Runs the Pokedex code to display the pokemon from certain regions
    global list2
    entry.delete("1.0", tkinter.END)  # Clears the text window
    list2 = Dex.region(list2, 'Alola')
    Poke = Display()
    entry.insert("1.0", Poke)  # Displays the list in the text window


def DisplayRegGalar():
    # Runs the Pokedex code to display the pokemon from certain regions
    global list2
    entry.delete("1.0", tkinter.END)  # Clears the text window
    list2 = Dex.region(list2, 'Galar')
    Poke = Display()
    entry.insert("1.0", Poke)  # Displays the list in the text window


def TypeM():
    # Runs the Pokedex code to display Monotype pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    typ = entry3.get()                  # Saves the entered type for easier testing in if statement
    typ = typ.capitalize()              # Saves the type as a capitalized string for easier testing
    typlist = ['Normal', 'Fire', 'Water', 'Grass', 'Poison', 'Fighting', 'Ice', 'Electric', 'Ground', 'Flying',
               'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']
    if typ in typlist:
        list2 = Dex.show_type(list2, entry3.get(), "4")
        Poke = Display()
    else:
        Poke = "Type does not exist"
    entry.insert("1.0", Poke)           # Displays the list in the text window


def TypeP():
    # Runs the Pokedex code to display Primary type pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    typ = entry3.get()                  # Saves the entered type for easier testing in if statement
    typ = typ.capitalize()              # Saves the type as a capitalized string for easier testing
    typlist = ['Normal', 'Fire', 'Water', 'Grass', 'Poison', 'Fighting', 'Ice', 'Electric', 'Ground', 'Flying',
               'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']
    if typ in typlist:
        list2 = Dex.show_type(list2, entry3.get(), "2")
        Poke = Display()
    else:
        Poke = "Type does not exist"
    entry.insert("1.0", Poke)           # Displays the list in the text window


def TypeS():
    # Runs the Pokedex code to display Secondary type pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    typ = entry3.get()                  # Saves the entered type for easier testing in if statement
    typ = typ.capitalize()              # Saves the type as a capitalized string for easier testing
    typlist = ['Normal', 'Fire', 'Water', 'Grass', 'Poison', 'Fighting', 'Ice', 'Electric', 'Ground', 'Flying',
               'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']
    if typ in typlist:
        list2 = Dex.show_type(list2, entry3.get(), "3")
        Poke = Display()
    else:
        Poke = "Type does not exist"
    entry.insert("1.0", Poke)           # Displays the list in the text window


def TypeB():
    # Runs the Pokedex code to display Primary and Secondary type pokemon
    global list2
    entry.delete("1.0", tkinter.END)    # Clears the text window
    typ = entry3.get()                  # Saves the entered type for easier testing in if statement
    typ = typ.capitalize()              # Saves the type as a capitalized string for easier testing
    typlist = ['Normal', 'Fire', 'Water', 'Grass', 'Poison', 'Fighting', 'Ice', 'Electric', 'Ground', 'Flying',
               'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']
    # If statement to ensure a type was entered, if incorrect type entered then states it
    if typ in typlist:
        list2 = Dex.show_type(list2, entry3.get(), "1")
        Poke = Display()
    else:
        Poke = "Type does not exist"
    entry.insert("1.0", Poke)           # Displays the list in the text window


def FindPoke():
    # Runs the Pokedex code to find and display Pokemon
    global list2
    entry.delete("1.0", tkinter.END)        # Clears the text window
    list2 = Dex.find(list2, entry4.get())  # Saves the data of the found pokemon in Poke
    Poke = Display()
    entry.insert("1.0", Poke)               # Displays the list in the text window


def FindPokeW():
    # Runs the Pokedex code to find and display Pokemon containing the entered characters
    global list2
    entry.delete("1.0", tkinter.END)            # Clears the text window
    list2 = Dex.find_with(list2, entry4.get())  # Saves the data of the found pokemon in Poke
    Poke = Display()
    entry.insert("1.0", Poke)                   # Displays the list in the text window


def Clr():
    # Clearts the text window of any characters
    global list2
    list2 = list1
    entry.delete("1.0", tkinter.END)


global namvar, numvar, entryvar, entryregvar
global wghtvar, hgtvar, formvar
global img, img2, image, canvas, entrynum
global framebottom, framebottommenu, type1var, type1label, frametype1, type2var, type2label
global frametype2, evolframe, listbtn
global entrychangebutton1, entrychangebutton2, entrychangebutton3, entrychangebutton4
global entrychangebutton5, entrychangebutton6, entrychangebutton7, entrychangebutton8

# Runs code to save the pokedex in the CSV in the list
list1 = Dex.define_list()
# Creates a copy and clears the list for global variable
list2 = Dex.define_list()
# Creates a global string
Poke = ''
# Creates the master window
root = tkinter.Tk()
root.minsize(680, 660)
place = 0
press = 1
# Titles the window
root.title("Pokedex")

# creates frame for display all pokemon and display evolution
listFrame = tkinter.Frame(root)
# Adds a label to the sorting frame
listL = tkinter.Label(listFrame, text='List:')
# First sortingFrame in listFrame to organize the buttons (Houses the List pokedex button)
listframeL = tkinter.Frame(listFrame)
listframeR = tkinter.Frame(listFrame)

# Creates first large sortingFrame to organize the buttons
sortingFrame = tkinter.Frame(root)
# Adds a label to the sorting frame
sorting = tkinter.Label(sortingFrame, text='Sorting Options:')
# First sortingFrame in sortingFrame to organize the buttons (Houses the List Numerically button)
sortingframeL = tkinter.Frame(sortingFrame)
# Second sortingFrame in sortingFrame to organize the buttons (Houses the List Alphabetically buttons)
sortingframeCL = tkinter.Frame(sortingFrame)
# Third sortingFrame in sortingFrame to organize the buttons (Houses the List by Weight Buttons)
sortingframeCR = tkinter.Frame(sortingFrame)
# Fourth sortingFrame in sortingFrame to organize the buttons (Houses the List by Height buttons)
sortingframeR = tkinter.Frame(sortingFrame)

# Creates second large sortingFrame to organize the buttons
searchingFrame = tkinter.Frame(root)
searchingFrame.rowconfigure([0],weight=1)
searchingFrame.columnconfigure([0, 1, 2], weight=1)
# adds label to the searching frame
search = tkinter.Label(root, text='Searching Options:')
# First sortingFrame in searchingFrame to organize the buttons (Houses the List from Region button)
searchingframeL = tkinter.Frame(searchingFrame)
# Creates a sortingFrame in searchingframeL to shift the button for a better look (Shifts the List from Region button)
regionframeL = tkinter.Frame(searchingframeL)
# Second sortingFrame in sortingFrame to organize the buttons (Houses the list by Type button)
searchingframeCL = tkinter.Frame(searchingFrame)
# Frame in searchingframeCL to organize the buttons (Houses the Type buttons and helps organize them neatly)
typeframeCL = tkinter.Frame(searchingframeCL)
# Third sortingFrame in sortingFrame to organize the buttons (Houses the find pokemon)
searchingframeCR = tkinter.Frame(searchingFrame)

# a window to show the text of the pokemon
entry = tkinter.Text(width=75, height=20)
# creates scroll buttons for the text window
scroll = tkinter.Scrollbar(root, command=entry.yview)
# Sets the scroll buttons to scroll in the Y direction
entry['yscrollcommand'] = scroll.set

# Creates a button named List Pokedex that runs the subroutine Display
dispP = tkinter.Button(listframeL, text="List Pokedex", command=DisplayBase)

# Creates a button named List Numerically that runs the subroutine Display
Num = tkinter.Button(sortingframeL, text="List Numerically Increasing", command=DisplayNumU)

# Creates a button named List Alphabetically A-Z that runs the subroutine DisplayAlphA
alpha = tkinter.Button(sortingframeCL, text="List Alphabetically A-Z", command=DisplayAlphA)

# Creates a button named List Height Shortest to Tallest that runs the subroutine DisplayHgtU
Hgt = tkinter.Button(sortingframeCR, text="List Height Shortest to Tallest", command=DisplayHgtU)

# Creates a button named List Weight Lightest to Heaviest that runs the subroutine DisplayWgtU
Wgt = tkinter.Button(sortingframeR, text="List Weight Lightest to Heaviest", command=DisplayWgtU)

# Creates a button named clear that runs the Clr subroutine to clear the window
clrWind = tkinter.Button(root, text="Clear", command=Clr)

# Places the data window
entry.pack()
# Places the scroll buttons
scroll.pack()
# Places the clear button
clrWind.pack()
# Places the List Numerically button
listFrame.pack(side='top', fill='both', expand=1)
listL.pack()
listframeL.pack(side='left', fill='both', expand=1)
listframeR.pack(side='right', fill='both', expand=1)
dispP.pack()
startbtn = tkinter.Button(listframeR, text="Pokemon Entry", command=des)
startbtn.pack()

# Places the middle sortingFrame that containes 4 frames
sortingFrame.pack(side='top', fill='both', expand=1)
sorting.pack()
# Places the first of 4 frames in the middle sortingFrame
sortingframeL.pack(side='left', fill='both', expand=1)
# Places the second of 4 frames in the middle sortingFrame
sortingframeCL.pack(side='left', fill='both', expand=1)
# Places the third of 4 frames in the middle sortingFrame
sortingframeCR.pack(side='right', fill='both', expand=1)
# Places the fourth of 4 frames in the middle sortingFrame
sortingframeR.pack(side='right', fill='both', expand=1)

# Places the List Numerically button
Num.pack(padx=5, pady=5)
# Places the List Alphabetically A-Z button
alpha.pack(padx=5, pady=5)
# Places the List Height shortest to tallest button
Hgt.pack(padx=5, pady=5)
# Places the List Weight lightest to heaviest button
Wgt.pack(padx=5, pady=5)

regionframeL.rowconfigure([0, 1, 2, 3], minsize=10, weight=1)
regionframeL.columnconfigure([0, 1], minsize=10, weight=1)
rgn1 = "Regions:"
label2 = tkinter.Label(searchingframeL, text=rgn1)
Rgn1 = tkinter.Button(regionframeL, text="Kanto", command=DisplayRegKanto)
Rgn2 = tkinter.Button(regionframeL, text="Johto", command=DisplayRegJohto)
Rgn3 = tkinter.Button(regionframeL, text="Hoenn", command=DisplayRegHoenn)
Rgn4 = tkinter.Button(regionframeL, text="Sinnoh", command=DisplayRegSinnoh)
Rgn5 = tkinter.Button(regionframeL, text="Unova", command=DisplayRegUnova)
Rgn6 = tkinter.Button(regionframeL, text="Kalos", command=DisplayRegKalos)
Rgn7 = tkinter.Button(regionframeL, text="Alola", command=DisplayRegAlola)
Rgn8 = tkinter.Button(regionframeL, text="Galar", command=DisplayRegGalar)

entry3 = tkinter.Entry(searchingframeCL)
type1 = "Types of pokemon:" "\n" f"{'Normal':<9} {'Fire':<9} {'Water':<9} {'Grass':<9}"  "\n" \
       f"{'Electric':<9} {'Ice':<9} {'Fighting':<9} {'Poison':<9}" "\n"  f"{'Ground':<9} {'Flying':<9}" \
       f"{'Psychic':<9} {'Bug':<9}"  "\n" f"{'Rock':<9} {'Ghost':<9} {'Dragon':<9} {'Dark':<9}" \
        "\n" f" {'Steel':<9} {'Fairy':<9}"
label3 = tkinter.Label(searchingframeCL, text=type1)
typeframeCL.rowconfigure([0, 1], minsize=10, weight=1)
typeframeCL.columnconfigure([0, 1], minsize=10, weight=1)
Type = tkinter.Button(typeframeCL, text="Monotype", command=TypeM)
Type1 = tkinter.Button(typeframeCL, text="Primary", command=TypeP)
Type2 = tkinter.Button(typeframeCL, text="Secondary", command=TypeS)
Type3 = tkinter.Button(typeframeCL, text="Both", command=TypeB)

entry4 = tkinter.Entry(searchingframeCR)
Pokem = "Pokemon Search:"
label4 = tkinter.Label(searchingframeCR, text=Pokem)
Name = tkinter.Button(searchingframeCR, text="Find Pokemon", command=FindPoke)
NameW = tkinter.Button(searchingframeCR, text="Find Pokemon Containing", command=FindPokeW)

search.pack()
searchingFrame.pack(side='bottom', fill='both', expand=1)
searchingframeL.grid(row=0, column=0)
searchingframeCL.grid(row=0, column=1)
searchingframeCR.grid(row=0, column=2)

label2.pack()
regionframeL.pack(side='left', fill='both', expand=1)
Rgn1.grid(row=0, column=0, padx=2, pady=2)
Rgn2.grid(row=0, column=1, padx=2, pady=2)
Rgn3.grid(row=1, column=0, padx=2, pady=2)
Rgn4.grid(row=1, column=1, padx=2, pady=2)
Rgn5.grid(row=2, column=0, padx=2, pady=2)
Rgn6.grid(row=2, column=1, padx=2, pady=2)
Rgn7.grid(row=3, column=0, padx=2, pady=2)
Rgn8.grid(row=3, column=1, padx=2, pady=2)

label3.pack()
entry3.pack(padx=2, pady=2)
typeframeCL.pack()
Type.grid(row=0, column=0, padx=2, pady=2)
Type1.grid(row=0, column=1, padx=2, pady=2)
Type2.grid(row=1, column=0, padx=2, pady=2)
Type3.grid(row=1, column=1, padx=2, pady=2)

label4.pack()
entry4.pack(pady=4)
Name.pack()
NameW.pack()

root.mainloop()
