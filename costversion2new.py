import tkinter as tk
from tkinter import *
#Pillow

from PIL import Image

# shirtsilk = None 

price = 0
length = 0
a = 0
b = 0
c = 0

#PriceIncrement
colorprice = 0
fabricprice = 0

#LengthIncrement
lensleeve = 0

root=Tk()
root.configure(width=1000, height=600)

# def stripes():
# 	global shirtsilk
# 	design = Image.open("source/stripe.png").convert("RGBA")
# 	shirtsketchtrans = Image.open("source/shirtsketchtrans.png").convert("RGBA")

# 	design.paste(shirtsketchtrans, (0,0), shirtsketchtrans)

# 	mask = Image.open("source/shirtsketchmask.png").convert("RGBA")
# 	design.paste(mask, (0,0), mask)
# 	design.save("source/output1.png")
# 	shirtsilk = tk.PhotoImage(file="source/output1.png")

testcircleorange = tk.PhotoImage(file="source/orange.png")
testcirclered = tk.PhotoImage(file="source/red.png")

testshirtone = tk.PhotoImage(file="source/shirt1.png")
testshirttwo = tk.PhotoImage(file="source/shirt2.png")

headerprice = tk.Label(root, text="Price: " + str(price), font=("", 22))
headerprice.grid(row=0, column=2)

#From this line till colorbutton.grid is the parameter of color, use this syntax for each additional criterion

#Color
colorlist = ["Red", "Green", "Blue", "Pink", "White", "Orange"]

colorvar = tk.StringVar(root)
colorvar.set(colorlist[0])

colormenu = tk.OptionMenu(root, colorvar, colorlist[0], colorlist[1], colorlist[2], colorlist[3], colorlist[4], colorlist[5])
colormenu.grid(row=0, column=0)

def colorget():
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
		test1label = tk.Label(root, image=testcirclered).place(x=200, y=50)
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
		test1label = tk.Label(root, image=testcircleorange).place(x=200, y=50)
	headerprice.configure(text="Price: " + str(price))



colorbutton = tk.Button(root, text="Enter", command=colorget)
colorbutton.grid(row=0, column=1)

#Sleeve Type

sleevelist = ["Full Sleeves", "Half Sleeves", "No Sleeves"]

sleevevar = tk.StringVar(root)
sleevevar.set(sleevelist[1])

sleevemenu = tk.OptionMenu(root, sleevevar, sleevelist[0], sleevelist[1], sleevelist[2])
sleevemenu.grid(row=1, column=0)

def sleeveget():
	global price
	global length
	global b
	global lensleeve
	global shirtsilk
	getsleeve = sleevevar.get()

	#b = Value Indicator to see what kind of sleeve was selected (Used for sleeve re-selection)
	if getsleeve == "Full Sleeves":
		lensleeve = 2
		if b==1:
			length = length - 2
		elif b==2:
			length = length - 1
		elif b==3:
			length = length - 0
		b=1
	elif getsleeve == "Half Sleeves":
		lensleeve = 1
		if b==1:
			length = length - 2
		elif b==2:
			length = length - 1
		elif b==3:
			length = length - 0
		b=2
	elif getsleeve == "No Sleeves":
		lensleeve = 0
		if b==1:
			length = length - 2
		elif b==2:
			length = length - 1
		elif b==3:
			length = length - 0
		b=3

	length = length + lensleeve
	print(length)
	# print(lensleeve)

sleevebutton = tk.Button(root, text="Enter", command=sleeveget)
sleevebutton.grid(row=1, column=1)

#Fabric
fabriclist = ["Silk", "Cotton", "Polyester", "Nylon"]
fabricvar = tk.StringVar(root)
fabricvar.set(fabriclist[1])

fabricmenu = tk.OptionMenu(root, fabricvar, fabriclist[0], fabriclist[1], fabriclist[2], fabriclist[3])
fabricmenu.grid(row=2, column=0)

def fabricget():
	global price
	global length
	global fabricprice
	global c
	global shirtsilk

	getfabric = fabricvar.get()
	price = price - fabricprice
	if getfabric == "Silk":
		# stripes()
		fabricprice = length*180
		price = price + length*180
		# test2label = tk.Label(root, image=shirtsilk).place(x=190,y=110)
		test2label = tk.Label(root, image=testshirtone).place(x=190,y=110)	
		c=0
	elif getfabric == "Cotton":
		fabricprice = length*150
		price = price + length*150
		test2label = tk.Label(root, image=testshirttwo).place(x=190,y=110)
		c=0
	elif getfabric == "Polyester":
		fabricprice = length*115
		price = price + length*115
		c=0
	elif getfabric == "Nylon":
		fabricprice = length*130
		price = price + length*130
		c=0
	headerprice.configure(text="Price " + str(price))

fabricbutton = tk.Button(root, text="Enter", command=fabricget)
fabricbutton.grid(row=2, column=1)


root.mainloop()
