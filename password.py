from  tkinter import*
import random, string

root=Tk()
root.geometry("400x280")
root.title("Password Generator")

# intro text
title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("The strength of password")

def selection():
    selection=choice.get()

choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=SEL).pack(anchor=CENTER)
R1 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=SEL).pack(anchor=CENTER)
R1 = Radiobutton(root, text="ADVANCED", variable=choice, value=3, command=SEL).pack(anchor=CENTER)

labelchoice = Label(root)
labelchoice.pack()

lenlabel=StringVar()
lenlabel.set("Password length")
lentitle = Label(root,textvariable=lenlabel).pack()

val=IntVar()
spinlenght = Spinbox(root,from_=8, to_=24, textvariable=val,width=13).pack()

def callback():
    Isum.config(text=passgen())

passgenButton=Button(root,text="Generate password",bd=5,height=2,command=callback,pady=3)
passgenButton.pack()
password=str(callback)

Isum=Label(root,text="")
Isum.pack(side=BOTTOM)

#logic
poor = string.ascii_uppercase+string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols="""'`!@#$%^&*()_-+=[]{}\|;:""<>,./"""
advance = poor + average + symbols
 

def passgen():
    if choice.get() == 1:
        return"".join(random.sample(poor,val.get()))
    elif choice.get() == 2:
        return"".join(random.sample(average,val.get()))
    elif choice.get() == 3:
        return"".join(random.sample(advance,val.get()))

root.mainloop()


              
