#X - Comment out/remove in release
#T - Temporary, remove after testing
import tkinter as tk
from tkinter import *
#Pillow

from PIL import Image

#Calling pattern variables to none for global usage in functions
pastepattern = None

price = 0
length = 0
a = 0
b = 0
c = 0

#Indicators
ct = 0 #Indicator for collar type
st = 0 #Indicator for sleeve type
pt = 0 #Indicator for pocket type
dt = 0 #Indicator for design/pattern type


#PriceIncrement
colorprice = 0
fabricprice = 0
patternprice = 0
collarprice = 0

#LengthIncrement
lensleeve = 0

#Global variables for start() function
bshirt = None
bcollar = None
bmask = None
baselabel = None
baseshirtimg = None

#Global variables for pattern
collarreg = None

root=Tk()
root.configure(width=1000, height=600, bg="#F0F0F0")

# X - For base white shirt; only to be removed in final release
def start():  # Start Base
    global bcollar
    global bshirt
    global bmask
    global baselabel
    global ct
    global st
    global pt
    global baseshirtimg

    if dt == 0:

        if ct == 0:
            bcollar = Image.open('source/collar_regular.png')
        elif ct == 1:
            bcollar = Image.open('source/collar_standing.png')
        elif ct == 2:
            bcollar = Image.open('source/collar_buttondown.png')

        if st == 0:
            bshirt = Image.open('source/torso_half_sleeve.png')
            bmask = Image.open('source/mask_half_sleeve.png')
        elif st == 1:
            bshirt = Image.open('source/torso_half_sleeve.png')
            bmask = Image.open('source/mask_half_sleeve.png')

        bmask.paste(bshirt, (0, 0), bshirt)
        bmask.paste(bcollar, (0, 0), bcollar)
        bmask.save('dump/baseinit.png')

        baseshirt = tk.PhotoImage(file='dump/baseinit.png')
        baseshirtimg = baseshirt

    if dt == 1:

        if ct == 0:
            bcollar = Image.open('source/collar_regular.png')
        elif ct == 1:
            bcollar = Image.open('source/collar_standing.png')
        elif ct == 2:
            bcollar = Image.open('source/collar_buttondown.png')

        if st == 0:
            bshirt = Image.open('source/torso_half_sleeve.png')
            bmask = Image.open('source/mask_half_sleeve.png')
        elif st == 1:
            bshirt = Image.open('source/torso_half_sleeve.png')
            bmask = Image.open('source/mask_half_sleeve.png')

        bmask.paste(bshirt, (0, 0), bshirt)
        bmask.paste(bcollar, (0, 0), bcollar)
        design = Image.open('source/stripes.png')
        design.paste(bmask, (0,0), bmask)
        design.save('dump/baseinit.png')

        baseshirt = tk.PhotoImage(file='dump/baseinit.png')
        baseshirtimg = baseshirt

    if dt == 2:

        if ct == 0:
            bcollar = Image.open('source/collar_regular.png')
        elif ct == 1:
            bcollar = Image.open('source/collar_standing.png')
        elif ct == 2:
            bcollar = Image.open('source/collar_buttondown.png')

        if st == 0:
            bshirt = Image.open('source/torso_half_sleeve.png')
            bmask = Image.open('source/mask_half_sleeve.png')
        elif st == 1:
            bshirt = Image.open('source/torso_half_sleeve.png')
            bmask = Image.open('source/mask_half_sleeve.png')

        bmask.paste(bshirt, (0, 0), bshirt)
        bmask.paste(bcollar, (0, 0), bcollar)
        design = Image.open('source/polka.png')
        design.paste(bmask, (0,0), bmask)
        design.save('dump/baseinit.png')

        baseshirt = tk.PhotoImage(file='dump/baseinit.png')
        baseshirtimg = baseshirt

    if dt == 3:

        if ct == 0:
            bcollar = Image.open('source/collar_regular.png')
        elif ct == 1:
            bcollar = Image.open('source/collar_standing.png')
        elif ct == 2:
            bcollar = Image.open('source/collar_buttondown.png')

        if st == 0:
            bshirt = Image.open('source/torso_half_sleeve.png')
            bmask = Image.open('source/mask_half_sleeve.png')
        elif st == 1:
            bshirt = Image.open('source/torso_half_sleeve.png')
            bmask = Image.open('source/mask_half_sleeve.png')

        bmask.paste(bshirt, (0, 0), bshirt)
        bmask.paste(bcollar, (0, 0), bcollar)
        design = Image.open('source/flowers.png')
        design.paste(bmask, (0,0), bmask)
        design.save('dump/baseinit.png')

        baseshirt = tk.PhotoImage(file='dump/baseinit.png')
        baseshirtimg = baseshirt

start()
baselabel = tk.Label(root, image=baseshirtimg)
baselabel.place(x=400, y=0)

def stripes():
    global pastepattern
    global ct
    global collarreg
    design = Image.open('source/stripes.png')
    mask = Image.open('source/mask_half_sleeve.png')
    shirt = Image.open('source/torso_half_sleeve.png')

    if ct == 0:
        collarreg = Image.open('source/collar_regular.png')
    elif ct == 1:
        collarreg = Image.open('source/collar_standing.png')
    elif ct == 2:
        collarreg = Image.open('source/collar_buttondown.png')

    shirt.paste(mask, (0,0), mask)
    shirt.paste(collarreg, (0,0), collarreg)
    design.paste(shirt, (0,0), shirt)

    design.save('dump/output1.png')
    pastepattern = tk.PhotoImage(file='dump/output1.png')

def none():
    global pastepattern
    global ct
    shirt = Image.open("source/torso_half_sleeve.png").convert("RGBA")
    mask = Image.open("source/mask_half_sleeve.png").convert("RGBA")
    collar = Image.open("source/collar_regular.png").convert("RGBA")

    shirt.paste(mask, (0,0), mask)
    shirt.paste(collar, (0,0), collar)
    shirt.save("source/output1.png")
    pastepattern = tk.PhotoImage(file="source/output1.png")

def polka():
    global pastepattern
    global ct
    global collarreg
    design = Image.open('source/polka.png')
    mask = Image.open('source/mask_half_sleeve.png')
    shirt = Image.open('source/torso_half_sleeve.png')

    if ct == 0:
        collarreg = Image.open('source/collar_regular.png')
    elif ct == 1:
        collarreg = Image.open('source/collar_standing.png')
    elif ct == 2:
        collarreg = Image.open('source/collar_buttondown.png')

    shirt.paste(mask, (0,0), mask)
    shirt.paste(collarreg, (0,0), collarreg)
    design.paste(shirt, (0,0), shirt)

    design.save('dump/output1.png')
    pastepattern = tk.PhotoImage(file='dump/output1.png')

def flowers():
    global pastepattern
    global ct
    global collarreg
    design = Image.open('source/flowers.png')
    mask = Image.open('source/mask_half_sleeve.png')
    shirt = Image.open('source/torso_half_sleeve.png')

    if ct == 0:
        collarreg = Image.open('source/collar_regular.png')
    elif ct == 1:
        collarreg = Image.open('source/collar_standing.png')
    elif ct == 2:
        collarreg = Image.open('source/collar_buttondown.png')

    shirt.paste(mask, (0,0), mask)
    shirt.paste(collarreg, (0,0), collarreg)
    design.paste(shirt, (0,0), shirt)

    design.save('dump/output1.png')
    pastepattern = tk.PhotoImage(file='dump/output1.png')


# #X - Tests, comment out in release

# testcircleorange = tk.PhotoImage(file="source/orange.png")
# testcirclered = tk.PhotoImage(file="source/red.png")

# testshirtone = tk.PhotoImage(file="source/shirt1.png")
# testshirttwo = tk.PhotoImage(file="source/shirt2.png")

#Test ends here ---

#To provide gap in grid
gaplabel = tk.Label(root,text="               ")
gaplabel.grid(row=0, column=2)

headerprice = tk.Label(root, text="Price:  " + str(price), font=("Impact", 22))
headerprice.grid(row=0, column=3)

#From this line till colorbutton.grid is the parameter of color, use this syntax for each additional criterion

#Color
colorlist = ["Red", "Green", "Blue", "Pink", "White", "Orange"]

colorvar = tk.StringVar(root)
colorvar.set(colorlist[0])

colormenu = tk.OptionMenu(root, colorvar, colorlist[0], colorlist[1], colorlist[2], colorlist[3], colorlist[4], colorlist[5])
colormenu.config(width=10)
colormenu.grid(row=0, column=0)

def colorget(): #Make the color pricing based on length & not just a flat cost
    global price
    global length
    global colorprice
    global a
    getcolor = colorvar.get()
    price = price - colorprice
    colorprice = 0
    if getcolor == "Red":
        colorprice = 125
        price = price + colorprice
        # test1label = tk.Label(root, image=testcirclered).place(x=200, y=50)
    elif getcolor == "Blue":
        colorprice = 100
        price = price + colorprice
    elif getcolor == "Green":
        colorprice = 90
        price = price + colorprice
    elif getcolor == "Pink":
        colorprice = 140
        price = price + colorprice
    elif getcolor == "White":
        colorprice = 50
        price = price + colorprice
    elif getcolor == "Orange":
        colorprice = 155
        price = price + colorprice
        # test1label = tk.Label(root, image=testcircleorange).place(x=200, y=50)
    headerprice.configure(text="Price:  " + str(price))



colorbutton = tk.Button(root, text="Enter", command=colorget)
colorbutton.grid(row=0, column=1)

#Sleeve Type

sleevelist = ["Full Sleeves", "Half Sleeves", "No Sleeves"]

sleevevar = tk.StringVar(root)
sleevevar.set(sleevelist[1])

sleevemenu = tk.OptionMenu(root, sleevevar, sleevelist[0], sleevelist[1], sleevelist[2])
sleevemenu.config(width = 10)
sleevemenu.grid(row=1, column=0)

def sleeveget():
    global price
    global length
    global b
    global lensleeve
    global stripespattern
    global ct
    getsleeve = sleevevar.get()

    #b = Value Indicator to see what kind of sleeve was selected (Used for sleeve re-selection)
    if getsleeve == "Full Sleeves":
        lensleeve = 3
        if b==1:
            length = length - 3
        elif b==2:
            length = length - 2
        elif b==3:
            length = length - 1
        b=1
    elif getsleeve == "Half Sleeves":
        lensleeve = 2
        if b==1:
            length = length - 3
        elif b==2:
            length = length - 2
        elif b==3:
            length = length - 1
        b=2
    elif getsleeve == "No Sleeves":
        lensleeve = 1
        if b==1:
            length = length - 3
        elif b==2:
            length = length - 2
        elif b==3:
            length = length - 1

    length = length + lensleeve
    # print(length)
    # print(lensleeve)

sleevebutton = tk.Button(root, text="Enter", command=sleeveget)
sleevebutton.grid(row=1, column=1)

#Fabric
fabriclist = ["Silk", "Cotton", "Polyester", "Nylon"]
fabricvar = tk.StringVar(root)
fabricvar.set(fabriclist[1])

fabricmenu = tk.OptionMenu(root, fabricvar, fabriclist[0], fabriclist[1], fabriclist[2], fabriclist[3])
fabricmenu.config(width=10)
fabricmenu.grid(row=4, column=0)

def fabricget():
    global price
    global length
    global fabricprice
    global c
    global stripespattern

    getfabric = fabricvar.get()
    price = price - fabricprice
    if getfabric == "Silk":
        fabricprice = length*180
        price = price + length*180
        # test2label = tk.Label(root, image=testshirtone).place(x=190,y=110) #Testing   
        c=0
    elif getfabric == "Cotton":
        fabricprice = length*150
        price = price + length*150
        # test2label = tk.Label(root, image=testshirttwo).place(x=190,y=110)
        c=0
    elif getfabric == "Polyester":
        fabricprice = length*115
        price = price + length*115
        c=0
    elif getfabric == "Nylon":
        fabricprice = length*130
        price = price + length*130
        c=0
    headerprice.configure(text="Price  " + str(price))

fabricbutton = tk.Button(root, text="Enter", command=fabricget)
fabricbutton.grid(row=4, column=1)

#Collar
collarlist = ["Standing", "Regular", "Buttondown"]
collarvar = tk.StringVar(root)
collarvar.set(collarlist[1])

patternmenu = tk.OptionMenu(root, collarvar, collarlist[0], collarlist[1], collarlist[2])
patternmenu.config(width=10)
patternmenu.grid(row=2, column=0)

def collarget():
    global ct 
    global length
    global price
    global collarprice
    getcollar = collarvar.get()

    price = price - collarprice

    if getcollar == "Regular":
        collarprice = 40
        price = price + 40
        ct = 0
        start()
        baselabel = tk.Label(root, image=baseshirtimg)
        baselabel.place(x=400, y=0)
    if getcollar == "Standing":
        collarprice = 50
        price = price + 50
        ct = 1
        start()
        baselabel = tk.Label(root, image=baseshirtimg)
        baselabel.place(x=400, y=0)
    if getcollar == "Buttondown":
        collarprice = 70
        price = price + 70
        ct = 2
        start()
        baselabel = tk.Label(root, image=baseshirtimg)
        baselabel.place(x=400, y=0)
    headerprice.configure(text="Price  " + str(price))


fabricbutton = tk.Button(root, text="Enter", command=collarget)
fabricbutton.grid(row=2, column=1)

#Pattern
patternlist = ["Stripes", "Polka Dots", "Flowers", "None"]
patternvar = tk.StringVar(root)
patternvar.set(patternlist[3])

patternmenu = tk.OptionMenu(root, patternvar, patternlist[0], patternlist[1], patternlist[2], patternlist[3])
patternmenu.config(width=10)
patternmenu.grid(row=3, column=0)

def patternget():
    global price
    global length
    global patternprice
    global dt
    getpattern = patternvar.get()

    price = price - patternprice

    if getpattern == "Stripes":
        patternprice = length*25
        price = price + length*25
        stripes()
        patternlabel = tk.Label(root, image=pastepattern).place(x=400,y=0)
        dt = 1

    if getpattern == "Polka Dots":
        patternprice = length*20
        price = price + length*20
        polka()
        patternlabel = tk.Label(root, image=pastepattern).place(x=400, y=0)
        dt = 2

    if getpattern == "Flowers":
        patternprice = length*35
        price = price + length*35
        flowers()
        patternlabel = tk.Label(root, image=pastepattern).place(x=400, y=0) 
        dt = 3

    if getpattern == "None":
        none()
        patternlabel = tk.Label(root, image=pastepattern).place(x=400, y=0)
        dt = 0

    headerprice.configure(text="Price  " + str(price))

patternbutton = tk.Button(root, text="Enter", command=patternget)
patternbutton.grid(row=3, column=1)


root.mainloop() #Ending the tkinter mainloop, all code that should appear in GUI or is related to Tkinter tobe written abover this and before root = Tk()
#---End of Code---