import tkinter as tk
from tkinter import messagebox
import random
import string
import time

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for password length.")
        return
    
    char_pool = ""
    if lowercase_var.get():
        char_pool += string.ascii_lowercase
    if uppercase_var.get():
        char_pool += string.ascii_uppercase
    if digits_var.get():
        char_pool += string.digits
    if special_var.get():
        char_pool += string.punctuation
    
    if not char_pool:
        messagebox.showerror("Invalid Criteria", "Please select at least one character type!")
        return
    
    password = "".join(random.choice(char_pool) for _ in range(length))
    password_label.config(text=password)

def animate_name(index=0):
    colors = ["#e74c3c", "#3498db", "#2ecc71", "#f1c40f"]
    name_label.config(fg=colors[index % len(colors)])
    root.after(500, animate_name, index + 1)

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")
root.configure(bg="#2c3e50")

# Top frame for name and created by text (left aligned)
top_frame = tk.Frame(root, bg="#2c3e50")
top_frame.pack(pady=10, anchor="w")

name_label = tk.Label(top_frame, text="Farhana Ahsan", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white")
name_label.pack(side="left", padx=10)

created_label = tk.Label(top_frame, text=" - Created by", font=("Arial", 12, "italic"), bg="#2c3e50", fg="white")
created_label.pack(side="left")

# Title for Password Generator
title_label = tk.Label(root, text="Strong Random Password Generator", font=("Arial", 16, "bold"), bg="#2c3e50", fg="#f1c40f")
title_label.pack(pady=10)

# Frame for criteria inputs
criteria_frame = tk.Frame(root, bg="#2c3e50")
criteria_frame.pack(pady=10)

# Password length input
length_label = tk.Label(criteria_frame, text="Password Length:", font=("Arial", 12), bg="#2c3e50", fg="white")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
length_entry = tk.Entry(criteria_frame, font=("Arial", 12), width=5)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, "12")  # Default length

# Checkboxes for criteria
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

lowercase_check = tk.Checkbutton(criteria_frame, text="Include Lowercase", variable=lowercase_var, font=("Arial", 12), bg="#2c3e50", fg="white", selectcolor="#2c3e50")
lowercase_check.grid(row=1, column=0, sticky="w", padx=5, pady=5)

uppercase_check = tk.Checkbutton(criteria_frame, text="Include Uppercase", variable=uppercase_var, font=("Arial", 12), bg="#2c3e50", fg="white", selectcolor="#2c3e50")
uppercase_check.grid(row=1, column=1, sticky="w", padx=5, pady=5)

digits_check = tk.Checkbutton(criteria_frame, text="Include Digits", variable=digits_var, font=("Arial", 12), bg="#2c3e50", fg="white", selectcolor="#2c3e50")
digits_check.grid(row=2, column=0, sticky="w", padx=5, pady=5)

special_check = tk.Checkbutton(criteria_frame, text="Include Special Characters", variable=special_var, font=("Arial", 12), bg="#2c3e50", fg="white", selectcolor="#2c3e50")
special_check.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# Generate Password button
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14, "bold"), bg="#e67e22", fg="white", command=generate_password)
generate_button.pack(pady=10)

# Label to display the generated password
password_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#2c3e50", fg="#2ecc71")
password_label.pack(pady=10)

animate_name()  # Start animated name
root.mainloop()
