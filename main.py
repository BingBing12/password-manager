from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip

FILE = "password_data.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get().title()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if messagebox.askokcancel(title=website, message=f"username: {username}\npassword: {password}\n"
                                                     f"Would you like to proceed?"):
        try:
            with open(FILE, "r") as file_data:
                data = json.load(file_data)
        except FileNotFoundError:
            with open(FILE, "w") as file_data:
                json.dump(new_data, file_data, indent=4)
                messagebox.showinfo(title=website, message=f"{website} data successfully saved.")
        else:
            data.update(new_data)
            with open(FILE, "w") as file_data:
                json.dump(data, file_data, indent=4)
                messagebox.showinfo(title=website, message=f"{website} data successfully saved.")
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
filename = PhotoImage(file="logo.png")
image = canvas.create_image(100, 100, image=filename)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry()
website_input.grid(row=1, column=1, sticky="we")

username_input = Entry()
username_input.grid(row=2, column=1, columnspan=2, sticky="we")

password_input = Entry()
password_input.grid(row=3, column=1, sticky="we")

search_button = Button(text="Search")
search_button.grid(row=1, column=2, sticky="we")

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2, sticky="we")

add_button = Button(text="Add", command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="we")

window.mainloop()
