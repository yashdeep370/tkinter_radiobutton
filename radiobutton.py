from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

root.geometry("455x233")
root.title("radiobutton")

def order():
    tmsg.showinfo("order done",f"gotcha {var.get()} done with oder")
    
var = StringVar()
var.set("radio")
# var = IntVar()
#var.set(1)
Label(root,text="what would u like to order?"
      , font="lucida 19 bold", justify = LEFT, padx=14).pack()

radio = Radiobutton(root, text="dosa",padx=14,variable=var,value="dosa").pack(
    anchor="w")
radio = Radiobutton(root, text="idli",padx=14,variable=var,value="idli").pack(
    anchor="w")
radio = Radiobutton(root, text="vada",padx=14,variable=var,value="vada").pack(
    anchor="w")
radio = Radiobutton(root, text="appam",padx=14,variable=var,value="appam").pack(
    anchor="w")

Button(text="order now", command=order).pack()

root.mainloop()