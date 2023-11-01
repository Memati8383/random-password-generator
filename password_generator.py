from tkinter import *
from random import choice
import string
import pyperclip  # for copying to clipboard

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title('Password Generator')
        self.window.geometry('400x300')
        self.window.config(bg='lightgray')

        self.label()
        self.entry()
        self.length_entry()
        self.generate_button()
        self.copy_button()

    def label(self):
        label_title = Label(self.window, text='Password Generator', font=('Courier', 20), bg='lightgray', fg='black')
        label_title.pack(pady=20)

    def entry(self):
        self.password_entry = Entry(self.window, font=('Courier', 16), bg='white', fg='black', width=25, relief='solid')
        self.password_entry.pack(pady=10)

    def length_entry(self):
        self.length_var = IntVar()
        length_frame = Frame(self.window, bg='lightgray')
        length_label = Label(length_frame, text='Password Length:', font=('Courier', 12), bg='lightgray', fg='black')
        length_label.pack(side=LEFT, padx=5)
        self.length_entry = Entry(length_frame, font=('Courier', 12), textvariable=self.length_var, width=5)
        self.length_entry.pack(side=LEFT)
        length_frame.pack()

    def generate_button(self):
        password_generator = Button(self.window, text="Generate Password", font=('Courier', 12), bg='white', fg='black', width=20, command=self.generate_password)
        password_generator.pack(pady=15)

    def copy_button(self):
        copy_to_clipboard = Button(self.window, text="Copy to Clipboard", font=('Courier', 12), bg='white', fg='black', width=20, command=self.copy_password)
        copy_to_clipboard.pack()

    def generate_password(self):
        length = self.length_var.get()
        if length <= 0:
            return

        characters = string.ascii_letters + string.punctuation + string.digits
        password = "".join(choice(characters) for _ in range(length))
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)

    def copy_password(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)

# Display
app = App()
app.window.mainloop()
