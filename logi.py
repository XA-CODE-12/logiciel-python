from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

background = "#06283D"
framefg = "#EDEDED"

root = Tk()
root.title("REGISTRE DE ODIN")
root.geometry("1250x700+210+100")
root.config(bg=background)

file = pathlib.Path('student_data.xlsx')
if not file.exists():
    file = Workbook()
    sheet = file.active
    sheet['A1'] = "N° Registre"
    sheet['B1'] = "Nom"
    sheet['C1'] = "Classe"
    sheet['D1'] = "Genre"
    sheet['E1'] = "DOB"
    sheet['F1'] = "Date du Registre"
    sheet['G1'] = "Religion"
    sheet['H1'] = "Skill"
    sheet['I1'] = "Nom du père"
    sheet['J1'] = "Nom de la mère"
    sheet['K1'] = "Travail du père"
    sheet['L1'] = "Travail de la mère"

    file.save('student_data.xlsx')


# exit
def Exit():
    root.destroy()


def showimage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select image file",
                                          filetypes=(("JPEG file", "*.jpeg"),
                                                     ("PNG file", "*.png"),
                                                     ("All files", ".")))

    if filename:
        img = Image.open(filename)
        resized_image = img.resize((190, 190), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(resized_image)
        lbl.config(image=photo2)
        lbl.image = photo2


# agender
def selection():
    value = radio.get()
    if value == 1:
        Gender = "Male"
    else:
        Gender = "Female"


# top frames
Label(root, text="Email : dogblakleist04@gmail.com", width=10, height=3, bg="#f0687c", anchor='e').pack(side=TOP, fill=X)
Label(root, text="CEET REGISTER", width=10, height=2, bg="#c36464", fg='#fff', font='arial 20 bold').pack(side=TOP, fill=X)

# recherche box to update
Search = StringVar()
Entry(root, textvariable=Search, width=15, bd=2, font="arial 20").place(x=820, y=70)

# Verify the image path and load images
try:
    imageicon3 = PhotoImage(file="PhotoImage/i.jpeg")
    Srch = Button(root, text="Search", compound=LEFT, image=imageicon3, width=123, bg='#68ddfa', font="arial 13 bold")
    Srch.place(x=1060, y=66)
except Exception as e:
    messagebox.showerror("Error", f"Unable to load search image: {e}")
    Srch = Button(root, text="Search", width=123, bg='#68ddfa', font="arial 13 bold")
    Srch.place(x=1060, y=66)

try:
    imageicon4 = PhotoImage(file="PhotoImage/i.jpeg")
    Update_button = Button(root, image=imageicon4, bg="#c36463")
    Update_button.place(x=110, y=64)
except Exception as e:
    messagebox.showerror("Error", f"Unable to load update image: {e}")
    Update_button = Button(root, text="Update", bg="#c36463")
    Update_button.place(x=110, y=64)

Label(root, text="N° Registre : ", font="arial 13", fg=framefg, bg=background).place(x=30, y=150)
Label(root, text="Date : ", font="arial 13", fg=framefg, bg=background).place(x=500, y=150)
registration = StringVar()
Date = StringVar()

reg_entry = Entry(root, textvariable=registration, width=15, font="arial 10")
reg_entry.place(x=160, y=150)

# reg no
today = date.today()
dl = today.strftime("%d/%m/%Y")
date_entry = Entry(root, textvariable=Date, width=15, font="arial 10")
date_entry.place(x=550, y=150)

Date.set(dl)

# detail etudiant
obj = LabelFrame(root, text="Client's Details", font=20, width=900, bg=framefg, fg=framefg, height=250, relief=GROOVE)
obj.place(x=30, y=200)

Label(obj, text="Full Name : ", font="arial 13", bg=framefg, fg=background).place(x=30, y=50)
Label(obj, text="Date of Birthday : ", font="arial 13", bg=framefg, fg=background).place(x=30, y=100)
Label(obj, text="Gender : ", font="arial 13", bg=framefg, fg=background).place(x=30, y=150)

Label(obj, text="Classe : ", font="arial 13", bg=framefg, fg=background).place(x=500, y=50)
Label(obj, text="Religion : ", font="arial 13", bg=framefg, fg=background).place(x=500, y=100)
Label(obj, text="Skills : ", font="arial 13", bg=framefg, fg=background).place(x=500, y=150)

Name = StringVar()
name_entry = Entry(obj, textvariable=Name, width=20, font="arial 10")
name_entry.place(x=160, y=50)

DOB = StringVar()
dob_entry = Entry(obj, textvariable=DOB, width=20, font="arial 10")
dob_entry.place(x=160, y=100)

radio = IntVar()
R1 = Radiobutton(obj, text="Male", variable=radio, value=1, bg=framefg, fg=background, command=selection)
R1.place(x=160, y=150)

R2 = Radiobutton(obj, text="Female", variable=radio, value=2, bg=framefg, fg=background, command=selection)
R2.place(x=230, y=150)

Religion = StringVar()
religion_entry = Entry(obj, textvariable=Religion, width=20, font="arial 10")
religion_entry.place(x=630, y=100)

Skill = StringVar()
skill_entry = Entry(obj, textvariable=Skill, width=20, font="arial 10")
skill_entry.place(x=630, y=150)

classe = Combobox(obj, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], font="Robot 10", width=17, state="readonly")
classe.place(x=630, y=50)
classe.set("Select Classe")

# detail parents
obj2 = LabelFrame(root, text="Parent's Details", font=20, width=900, bg=framefg, fg=background, height=250, relief=GROOVE)
obj2.place(x=30, y=470)

Label(obj2, text="Father's Name : ", font="arial 13", bg=framefg, fg=background).place(x=30, y=50)
Label(obj2, text="Occupation : ", font="arial 13", bg=framefg, fg=background).place(x=30, y=100)

F_Name = StringVar()
f_entry = Entry(obj2, textvariable=F_Name, width=20, font="arial 10")
f_entry.place(x=160, y=50)

Father_Occupation = StringVar()
FO_entry = Entry(obj2, textvariable=Father_Occupation, width=20, font="arial 10")
FO_entry.place(x=160, y=100)

Label(obj2, text="Mother's Name : ", font="arial 13", bg=framefg, fg=background).place(x=500, y=50)
Label(obj2, text="Occupation : ", font="arial 13", bg=framefg, fg=background).place(x=500, y=100)

M_Name = StringVar()
m_entry = Entry(obj2, textvariable=M_Name, width=20, font="arial 10")
m_entry.place(x=630, y=50)

Mother_Occupation = StringVar()
MO_entry = Entry(obj2, textvariable=Mother_Occupation, width=20, font="arial 10")
MO_entry.place(x=630, y=100)

# image
f = Frame(root, bd=3, bg="black", width=200, height=200, relief=GROOVE)
f.place(x=1000, y=150)

lbl = Label(f, bg="black")
lbl.place(x=0, y=0)

# buttons
Button(root, text="Upload", width=19, height=2, font="arial 12 bold", bg="lightblue", command=showimage).place(x=1000, y=370)

saveButton = Button(root, text="Save", width=19, height=2, font="arial 12 bold", bg="lightgreen")
saveButton.place(x=1000, y=450)

Button(root, text="Reset", width=19, height=2, font="arial 12 bold", bg="lightpink").place(x=1000, y=530)

Button(root, text="Exit", width=19, height=2, font="arial 12 bold", bg="grey", command=Exit).place(x=1000, y=610)

root.mainloop()