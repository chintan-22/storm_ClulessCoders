from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from random import choice,randint,shuffle
import array
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    MAX_LEN = 12
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list=password_letters+password_numbers+password_symbols
    shuffle(password_list)
    Password = "".join(password_list)
    Password_entry.insert(0,Password)
    pyperclip.copy(Password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    generate_password()
    Website = Website_entry.get()
    Email = Email_entry.get()
    Password = Password_entry.get()
    if len(Website) == 0 or len(Password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any field empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=Website, message=f"These are the details entered: \nEmail:{Email}\nPassword:{Password}\n Is it OK to save?")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{Website}  |  {Email}  |  {Password} \n")
            Website_entry.delete(0, END)
            Email_entry.delete(0, END)
            Password_entry.delete(0, END)
           

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=390, pady=125)
canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
Website_label = Label(text="Website")
Website_label.grid(row=1, column=0)
Email_label = Label(text="Email/Username")
Email_label.grid(row=2, column=0)
Password_label = Label(text="Password")
Password_label.grid(row=3, column=0)
Website_entry = Entry(width=35)
Website_entry.grid(row=1, column=1)
Website_entry.focus()
Email_entry = Entry(width=35)
Email_entry.grid(row=2, column=1)
Email_entry.insert(0, "")
Password_entry = Entry(width=21)
Password_entry.grid(row=3, column=1)
add_button = Button(text="ADD", width=36, command=save)
add_button.grid(row=4, column=1)
window.mainloop()