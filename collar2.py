import tkinter as tk
from tkinter import *

from PIL import Image

root = Tk()
root.configure(width=1000, height=600, bg="#F0F0F0")

bshirt = Image.open('source/torso_half_sleeve.png')
bmask = Image.open('source/mask_half_sleeve.png')

bmask.paste(shirt, (0,0), shirt)

bcollar = Image.open('source/collar_regular.png')
bmask.paste(collar, (0,0), collar)

root.mainloop()
