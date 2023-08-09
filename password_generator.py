#-----------------------CODSOFT (INTERNSHIP ..... PYTHON PROGRAMMING)-------------------------------------

# NAME - SMRITI SAROJ SINHA
# COLLEGE - CENTRAL UNIVERSITY OF HARYANA

#-----------------------------------------PASSWORD GENERATOR ---------------------------------------------


# IMPORTING MODULES OF PYTHON 
from tkinter import *
import string 
import random 
import pyperclip # MODULE FOR 'COPY' INSTRUCTION

# DEFINING THE FUNCTION FOR GENERATING THE PASSOWRD ACCORDING TO THE SIZE AND THE STRENGTH SELECTED BY THE USER
def generator():
    small_alph = string.ascii_lowercase
    capital_alph = string.ascii_uppercase
    numbers =  string.digits
    special_char = string.punctuation

    all =  small_alph + capital_alph + numbers + special_char 
    passwordlength = int(length_box.get())

    if choice.get() == 1 :
        passwordfield.insert(0 , random.sample(small_alph + capital_alph ,passwordlength))
    if choice.get() == 2 :
        passwordfield.insert(0 , random.sample(small_alph + capital_alph + numbers ,passwordlength))
    if choice.get() == 3 :
        passwordfield.insert(0 , random.sample(all ,passwordlength))

# DEFINING THE FUNCTION FOR COPING THR PASSWORD GENERATED THE  PASSWORD GENERATOR SO THAT THE PASSWORD CAN BE USED BY THE USER AT THE 
# DESIRED PLACE
def copy():
    random_password = passwordfield.get()
    pyperclip.copy(random_password)

# GUI WINDOW
root = Tk()
root.config(bg='light blue')
root.title("Password Generator")
choice = IntVar()
font = ('Comic Sans MS' , 13 , 'bold')
passwordlabel = Label(root, text =  'PASSWORD GENERATOR' , font=('Times New Roman' , 20 , 'bold') , 
                      bg='light blue')
passwordlabel.grid()

weakradiobutton = Radiobutton(root , text='Weak' , value=1 , variable=choice ,  font = font)
weakradiobutton.grid(pady=5)

mediumradiobutton = Radiobutton(root , text='Medium' , value=2 , variable=choice ,  font = font)
mediumradiobutton.grid(pady=5)

strongradiobutton = Radiobutton(root , text='Strong' , value=3 , variable=choice ,  font = font)
strongradiobutton.grid(pady=5)

lengthlabel = Label(root, text =  'PASSWORD LENGTH' , font=('Comic Sans MS' , 15 , 'bold') , 
                      bg='light blue')
lengthlabel.grid()

length_box = Spinbox(root , from_=5 , to_= 15 , width=5 , font=font)
length_box.grid()

generatebutton = Button(root , text = 'Generate' , font = font , command =  generator )
generatebutton.grid(pady=10)

passwordfield = Entry(root , width=25 , bd = 2 , font=font )
passwordfield.grid()

copybutton = Button(root , text = 'copy' , font = font , command = copy)
copybutton.grid(pady=10)


root.mainloop()


