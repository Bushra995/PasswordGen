#twinker is used to build graphical user interface *gui)
import random
from tkinter import *
from tkinter import messagebox
#creating instance
parent=Tk()
#here parent is a display window widht x height
parent.geometry('700x500') #setting parent window size
#setting background colour
parent['bg']='Black'
parent.title("Password Generator ")

#setting label font size and bold
other_label=Label(parent,bg='orangered', text="---Welcome to password Generator--", font=('Arial Bold',25))
other_label.grid(column=0, row=0,pady=40,padx=20)
#pady=space in y axis
print("\n")
#enter password
#setting by default colour for label

#creating label with tkinter

my_label= Label(parent,text="Enter number of  digit  for  setting  password   : > ",bd=10)
my_label.config(bg='olivedrab1',font=('Times New Roman', 17, 'bold'))
my_label.grid(column=0 , row=1)
#taking input  for numbe of digits
number_box=Entry(parent,width=5,font=('Times New Roman', 15, 'bold'))
number_box.grid(column=1,row=1)

#mking empt label
lbl= Label(parent,bg='bisque',font=('Times New Roman', 12, 'bold'))

lbl.grid(row=4,column=0)
#password container
l = []
def clicked():
    l.clear()
    num = int(number_box.get()) #setting varaible as integer to genrtae password

    for i in range(num):
        l.append(chr(random.randint(33,126)))

    lbl.configure(text=l)
#function to clear and copy from clipboard
def copy():
    #clear clipp
    parent.clipboard_clear()
    #copy to clipboard
    parent.clipboard_append(number_box.get())
    #copied sucesfuklly popup window
    messagebox.showinfo('Clip', 'Password copied Sucesfully! ')
#button to generate password
btn = Button(parent, text="Generate", command=clicked)
btn.configure(bg="blue" , font=('Times New Roman',10,'bold'))
btn.grid(column=1, row=3,pady=10,padx=5,ipadx=5,ipady=5)
#button for clear and copy
btn2 = Button(parent, text="Clipper", command=copy)
btn2.configure(bg="yellow" , font=('Times New Roman',10,'bold'))
btn2.grid(column=0, row=3,pady=10,padx=5,ipadx=5,ipady=5)
#starting gui


parent.mainloop()
