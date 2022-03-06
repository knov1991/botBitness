import tkinter as tk
from tkinter import scrolledtext
#Declare Root
root = tk.Tk()
root.title("Scrolltext Widget")
tk.Label(root,text="My Scrolled Text Widget",font=("Times New Roman",25))\
	.grid(row=0,column=1)
#Define ScrollTextWidget
#wrap keyword used to wrap around text
myScrollTextWidget = scrolledtext.ScrolledText(root,wrap=tk.WORD,width=50,height=20,font=("Times New Roman",15),state="disabled")
myScrollTextWidget.grid(row=1,column=1)

def printToConsole():
	myScrollTextWidget.config(state="normal")
	myScrollTextWidget.insert('insert','hello\n')
	myScrollTextWidget.config(state="disabled")

#Buttons
myButton = tk.Button(root,text="Print to console!",command=printToConsole).grid(row=2,column=1)

root.mainloop()