from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

generate_password = Button(text="Generate Password")
generate_password.grid(row=3, column=2, sticky="we")

add_button = Button(text="Add")
add_button.grid(row=4, column=1, columnspan=2, sticky="we")

window.mainloop()
