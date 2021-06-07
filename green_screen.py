from tkinter import Tk
from tkinter import colorchooser


root = Tk()
root.geometry("600x400")
root.title("custom background")
bg='#00FF00'
root.config(bg=bg)
try:
	bg = colorchooser.askcolor(title ="Choose color")[1]
except:
	pass
root.config(bg=bg)
root.mainloop()