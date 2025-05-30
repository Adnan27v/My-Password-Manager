from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_password():

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,"end")
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get().title()
    password = password_entry.get()
    email = email_entry.get()

    new_data = {
                website:
                    {
                      "email": email,
                      "password": password,
                    }
                }

    if len(password)<=0 or len(website)<=0 or len(email) <= 0:
        messagebox.showerror(title="Error",message="Please don't leave any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=f"{website}",message=f"You entered the following details:\nEmail: {email}\nPassword: {password}\nWould you like to save these details?")
        
        try:
            with open("data.json",mode="r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json",mode="w") as f:
                json.dump(new_data,f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
            website_entry.focus()

#----------------------- Search --------------------------#

def search():
    """Helps to look up email and password for a certain website"""
    website = website_entry.get().title()
    try:
        with open("data.json", mode='r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data exists")
    else:
        try:
            email = data[website]["email"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showerror(title="Error", message="Website info not found")
        else:
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            website_entry.delete(0,"end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#Canvas
canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

#Website text
website_text = Label(text="Website:")
website_text.grid(row=1,column=0)

#Website Entry
website_entry = Entry(width=32)
website_entry.grid(row=1,column=1)
website_entry.focus()

#Email/Username text
email_text = Label(text="Email/Username:")
email_text.grid(row=2,column=0)

#Email Entry
email_entry = Entry(width=51)
email_entry.grid(row=2,column=1, columnspan=2)
email_entry.insert(0, "abc@gmail.com")

#Password text
password_text = Label(text="Password:")
password_text.grid(row=3,column=0)

#Password Entry
password_entry = Entry(width=32)
password_entry.grid(row=3,column=1)

#Generate Button
generate_button = Button(text="Generate Password",command=gen_password)
generate_button.grid(row=3,column=2)

#Search Button
generate_button = Button(text="Search",command=search,width=15)
generate_button.grid(row=1,column=2)

#Add Button
add_button = Button(text="Add",width=44, command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()