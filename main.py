import tkinter as tk
from encryption import encrypt_file
from decryption import decrypt_file
import os
from tkinter import filedialog, messagebox #to get access of file explorer & messagebox for pop up any msg like alert ...used in validation

selected_file = "" #global variable

def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        eye_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        eye_button.config(text="Show")

def browse_file():
    global selected_file #to infron interpreter theat we are using the same global variable we have created already...
                         #or else it would have created  another local variable again

    selected_file = filedialog.askopenfilename()

    if selected_file:
        filename = os.path.basename(selected_file) #returns only filename and not the whole path
        selected_file_label.config(text=filename)
        status_label.config(
            text="🟢 File Selected Successfully"
        )



def encrypt_button_clicked():

    if selected_file == "":
        messagebox.showerror(
            "Error",
            "Please select a file first."
        )
        return

    password = password_entry.get()

    if password == "":
        messagebox.showerror(
            "Error",
            "Please enter a password."
        )
        return

    if len(password) < 8:
        messagebox.showwarning(
            "Weak Password",
            "Password should contain at least 8 characters."
        )
        return

    try:
        output_path = encrypt_file(selected_file, password)
        status_label.config(
            text="✅ File Encrypted Successfully",
            fg="green"
        )

        messagebox.showinfo(
            "Success",
            f"File encrypted successfully!\n\nSaved at:\n{output_path}"
        )

    except Exception as e:
        messagebox.showerror(
            "Encryption Error",
            str(e)
        )

        status_label.config(
            text="❌ Encryption Failed",
            fg="red"
        )





def decrypt_button_clicked():

    if selected_file == "":
        messagebox.showerror(
            "Error",
            "Please select an encrypted file first."
        )
        return

    if not selected_file.endswith(".encrypted"):
        messagebox.showerror(
            "Invalid File",
            "Please select an encrypted file (.encrypted)."
        )
        return

    password = password_entry.get()

    if password == "":
        messagebox.showerror(
            "Error",
            "Please enter a password."
        )
        return

    if len(password) < 8:
        messagebox.showwarning(
            "Weak Password",
            "Password should contain at least 8 characters."
        )
        return

    try:
        output_path = decrypt_file(selected_file, password)

        status_label.config(
            text="✅ File Decrypted Successfully",
            fg="green"
        )

        messagebox.showinfo(
            "Success",
            f"File decrypted successfully!\n\nSaved at:\n{output_path}"
        )

    except Exception as e:
        messagebox.showerror(
            "Decryption Error",
            str(e)
        )

        status_label.config(
            text="❌ Decryption Failed",
            fg="red"
        )






# ============================
# Create Main Window
# ============================

window = tk.Tk()
window.title("Secure File Encryption-Decryption System")
window.geometry("760x500")
window.resizable(False, False)
window.configure(bg="#F5F5F5")


# ============================
# Title Frame
# ============================

title_frame = tk.Frame(
    window,
    bg="#F5F5F5"
)

title_frame.pack(fill="x", pady=15)
title_label = tk.Label(
    title_frame,
    text="🔒 Secure File Encryption-Decryption System",
    font=("Arial", 20, "bold"),
    fg="#003366",
    bg="#F5F5F5"
)

title_label.pack()


subtitle = tk.Label(
    title_frame,
    text="Encrypt and Decrypt Files Securely Using AES Algorithm",
    font=("Arial",10),
    fg="gray",
    bg="#F5F5F5"
)

subtitle.pack(pady=(0,20))

# ============================
# File Frame
# ============================

file_frame = tk.Frame(
    window,
    bg="#F5F5F5"
)

file_frame.pack(fill="x", padx=30, pady=10)

file_label = tk.Label(
    file_frame,
    text="📂 Select File",
    font=("Arial", 12, "bold"),
    bg="#F5F5F5"
)

file_label.grid(row=0, column=0, sticky="w")

# ============================
# Selected File Label
# ============================

selected_file_label = tk.Label(
    file_frame,
    text="No file selected",
    font=("Arial", 11),
    bg="#F5F5F5",
    fg="gray",
    width=40,
    anchor="w",
    relief="solid",
    padx=10,
    pady=5
)

selected_file_label.grid(row=1, column=0, padx=(0,10), pady=10)

# ============================
# Browse Button
# ============================

browse_button = tk.Button(
    file_frame,
    text="Browse",
    font=("Arial",11),
    width=12,
    bg="#E3F2FD",
    cursor="hand2",
    command=browse_file,
)


browse_button.grid(row=1, column=1, pady=10)

# ============================
# Password Frame
# ============================

password_frame = tk.Frame(
    window,
    bg="#F5F5F5"
)

password_frame.pack(fill="x", padx=30, pady=10)

# ============================
# Password Label
# ============================

password_label = tk.Label(
    password_frame,
    text="🔑 Enter Password",
    font=("Arial", 12, "bold"),
    bg="#F5F5F5"
)

password_label.grid(row=0, column=0, sticky="w")

# ============================
# Password Entry
# ============================

password_entry = tk.Entry(
    password_frame,
    font=("Arial", 12),
    width=35,
    show="*",
    bg="#F5F5F5"
)

password_entry.grid(row=1, column=0, pady=10, padx=(0, 5))

eye_button = tk.Button(
    password_frame,
    text="Show",
    font=("Arial", 11),
    width=12,
    bg="#E3F2FD",
    command=toggle_password,
    cursor="hand2",


)

eye_button.grid(row=1, column=1, pady=10)



# ============================
# Button Frame
# ============================

button_frame = tk.Frame(
    window,
    bg="#F5F5F5"
)

button_frame.pack( pady=20)

# ============================
# Encrypt Button
# ============================

encrypt_button = tk.Button(
    button_frame,
    text="Encrypt 🔒",
    font=("Arial", 12, "bold"),
    width=15,
    bg="#2E8B57",
    fg="white",
    cursor="hand2",
    command=encrypt_button_clicked
)

encrypt_button.grid(row=0, column=0, padx=10)

# ============================
# Decrypt Button
# ============================

decrypt_button = tk.Button(
    button_frame,
    text="Decrypt 🔓",
    font=("Arial", 12, "bold"),
    width=15,
    bg="#1E90FF",
    fg="white",
    cursor="hand2",
    command=decrypt_button_clicked 
)

decrypt_button.grid(row=0, column=1, padx=10)


# ============================
# Status Frame
# ============================

status_frame = tk.Frame(
    window,
    bg="#F5F5F5"
)

status_frame.pack(fill="x", padx=30)

# ============================
# Status Label
# ============================

status_label = tk.Label(
    status_frame,
    text="🟢 Status : Ready",
    font=("Arial", 11),
    fg="green",
    bg="#F5F5F5"
)

status_label.pack(anchor="w")


window.mainloop()