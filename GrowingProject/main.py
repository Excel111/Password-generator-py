# Importing necessary libraries
from tkinter import *       # For GUI components
import random               # For generating random characters
import pyperclip            # For copying text to the clipboard

# Step 1: Initialize the root window
# This creates the main window of the application
root = Tk()
root.geometry('350x350')          # Set window size
root.configure(background='lightblue')  # Set window background color

# Step 2: Define Variables
# Variables to store user input and output
password_var = StringVar()        # Variable to store the generated password
length_var = IntVar()             # Variable to store password length entered by user
length_var.set(8)                 # Default password length set to 8

# Step 3: Password Generation Function
# This function generates a random password based on the specified length
def generate_password():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ''
    if length_var.get() >= 8:     # Check if password length is at least 8
        for _ in range(length_var.get()):
            password += random.choice(chars)  # Add a random character from chars
        password_var.set(password)           # Set the generated password to password_var

# Step 4: Copy to Clipboard Function
# This function copies the generated password to the clipboard
def copy_to_clipboard():
    pyperclip.copy(password_var.get())      # Copy password to clipboard
    Label(root, text="Password copied!", bg="green", fg="white").pack(pady=5)  # Confirmation message

# Step 5: GUI Components
# Adding labels, buttons, and input fields to the GUI

# Label for instructions
Label(root, text="Enter the password length (min 8):", bg='blue', fg='white').pack(pady=10)

# Input field for password length
Entry(root, textvariable=length_var, width=20).pack(pady=5)

# Button to generate password
Button(root, text="Generate Password", command=generate_password, bg='black', fg='white').pack(pady=10)

# Display generated password
Entry(root, textvariable=password_var, width=30).pack(pady=5)

# Button to copy password to clipboard
Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg='black', fg='white').pack(pady=10)

# Step 6: Mainloop to run the application
# Keeps the window open until user closes it
root.mainloop()
