import tkinter as tk
from tkinter import Button, Label, messagebox, Spinbox, Text
import random
import string


def random_password(length):
    """
    Generates a random password of length 'length'
    Parameters: length (int) - length of password
    Returns: password (str) - random password
    """
    password = ""
    for _ in range(length):
        password += random.choice(string.ascii_letters + string.digits)
    
    return password

def insert_password():
    """
    Inserts a random password into the password box
    """
    if not length_box.get():
        messagebox.showerror("Error", "Please enter a password length")
        return
    elif not length_box.get().isdigit():
        messagebox.showerror("Error", "Please enter a valid password length")
        return
    password_box.delete(1.0, tk.END)
    password_box.insert(tk.END, random_password(int(length_box.get())))
    
def copy_password():
    """
    Copies the password in the password box to the clipboard
    """
    root.clipboard_clear()
    root.clipboard_append(password_box.get(1.0, tk.END))
    messagebox.showinfo("Password Copied", "Password copied to clipboard")


root = tk.Tk()
root.title("Apollo Password Generator")
root.geometry("500x250")
root.resizable(False, False)

root.configure(bg="#FFC0CB")

label1 = Label(root, text="Password Length", bg="#FFC0CB", font=("Arial", 12))
label1.place(x=190, y=10)

length_box = Spinbox(root, from_=1, to=100, width=5, background="pink", font=("Arial", 12))
length_box.place(x=220, y=40)

password_box = Text(root,
                    width=15,
                    height=1,
                    bg="pink",
                    font=("Arial", 12))

password_box.place(x=180, y=120)

generate_btn = Button(root,
                      text="Generate",
                      command=lambda: insert_password())

generate_btn.place(x=220, y=80)

copy_btn = Button(root,
                  text="Copy",
                  command=lambda: copy_password())
copy_btn.place(x=230, y=160)

name = Label(root, text="by m1v", fg="#FF34B3",bg="#FFC0CB", font=("Orator Std", 9, "normal"))
name.place(x=450, y=220)

root.mainloop()