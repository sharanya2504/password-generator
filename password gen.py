#importing modules
from tkinter import *
from tkinter import messagebox
import string
import random

root=Tk()
root.title("Password Generator")
root.geometry("325x275")
root.resizable(0,0)

#code for generating password
def generate_password():
    len=lenvalue.get()
    uc = string.ascii_uppercase if uppercasevalue.get() else ""
    lc = string.ascii_lowercase if lowercasevalue.get() else ""
    dig= string.digits if digitvalue.get() else ""
    special = string.punctuation if splcharvalue.get() else ""

    all_char=uc+lc+dig+special

    if int(len)<4 or int(len)>20:
        messagebox.showerror("Error","Please enter valid length of characters!")
        return
    if not all_char:
        messagebox.showerror("Error","Error,Please select atleast one option")
        return
    password = ''.join(random.choice(all_char) for _ in range(int(len)))
    resultvalue.set(f"GENERATE PASSWORD: {password}")


f1=Frame(root,bg="grey",borderwidth=3,relief=SUNKEN)
f1.grid()

lenght=Label(f1,text="Enter the length of Password")
lenght.grid(row=0)

#declaring variables
lenvalue=StringVar()
uppercasevalue=IntVar()
lowercasevalue=IntVar()
digitvalue=IntVar()
splcharvalue=IntVar()
resultvalue=IntVar()

#Lenth of password entry
lenentry=Entry(root,textvariable=lenvalue)
lenentry.grid(row=0,column=1)

#Checkbuttons
upper=Checkbutton(text="Include upper case letters?",variable=uppercasevalue)
upper.grid(row=1, column=0, pady=5, padx=10, sticky='w')

lower=Checkbutton(text="Include lower case letters?",variable=lowercasevalue)
lower.grid(row=2, column=0, pady=5, padx=10, sticky='w')

digit=Checkbutton(text="Include digits?",variable=digitvalue)
digit.grid(row=3, column=0, pady=5, padx=10, sticky='w')

spl=Checkbutton(text="Include special characters?",variable=splcharvalue)
spl.grid(row=4, column=0, pady=5, padx=10, sticky='w')

#password generating button
gen_btn=Button(text="Generate Password!", command=generate_password)
gen_btn.grid(row=6, column=0, columnspan=2, pady=10)

#show result label
result_label =Label(textvariable=resultvalue)
result_label.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()