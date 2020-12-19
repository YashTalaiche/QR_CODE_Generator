##########################            Talaiche.in             #################################

####  Load necessary packages
import pyqrcode
from PIL import ImageTk, Image
from pyzbar.pyzbar import decode
from tkinter import *


root= Tk()
root.title("QR Code Generator")
root.geometry('500x400')
root.configure(background='snow')

###################-----Title-----###############

Title =Label(root, font=('arial',20,'bold'),text='QR Code Generator',bd=21,bg='#708090',fg='Cornsilk',justify=CENTER)
Title.place(x=110,y=10)
 
##### main function for create QR code
def Create():
	global data
	data =str(txt1.get())
	qr=pyqrcode.create(data)
	img=qr.png(  str(data) + ".png" ,scale=5)
	print("done")
	from PIL import ImageTk, Image
	load = Image.open(str(data) +'.png')
	render = ImageTk.PhotoImage(load)
	img = Label(root, image=render)
	img.image = render
	img.place(x=180,y=220)

######  for QUIT the program
def Quit():
	root.destroy()

###### for Saving QRCODE
def save():
	pass
 
hed = Label(root, text="Enter Text", width=9, height=2, fg="Cornsilk", bg="#778899", font=('arial', 15, ' bold '))
hed.place(x=10, y=150)

txt1 = Entry(root, validate="key", width=15, bg="#778899", fg="Cornsilk", font=('times', 25, ' bold '))
txt1.place(x=135, y=155)

btnCreate=Button(root, padx=8, pady=1, bd=6, fg='black', font=('arial',16,'bold'),width=4, text="Create", bg="#778899", command=Create)
btnCreate.place(x=405,y=150)

btnquit=Button(root, padx=7, pady=1, bd=6, fg='black', font=('arial',15,'bold'),width=4, text="Quit", bg="#778899", command=Quit)
btnquit.place(x=420,y=350)

btnsave=Button(root, padx=7, pady=1, bd=6, fg='black', font=('arial',15,'bold'),width=4, text="Save", bg="#778899", command=save)
btnsave.place(x=1,y=350)

root.mainloop()