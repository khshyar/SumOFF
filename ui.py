import tkinter as tk
from tkinter import ttk, font
from tkinter import messagebox
from db.mysql_python_connector import SqlPy

class CreateUser:
    def __init__(self, root):
        self.root = root
        self.root.title("Create a new user!")
        self.root.geometry("250x180")
        self.sql = SqlPy()
        self.ui_setup()


# COMMANDS

    def check_validation(self):
        letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        if len(self.password) >= 8:
            if any(char in self.password for char in letters_lower) and any(char in self.password for char in letters_upper) and any(char in self.password for char in numbers) and any(char in self.password for char in symbols):
                if self.password == self.rep_pass:
                    return True
                else:
                    messagebox.showwarning(title="Error", message="Please make sure you entered your password twice correctly")
            
            else:
                messagebox.showwarning(title="Error", message="Please make sure you've put all symbols, lower-case, upper-case, numbers in your password!")
        else:
            messagebox.showwarning(title="Error", message="Please make sure the password you entered is equal or more than 8 characters!")
                

    def get_user(self):

        self.username = self.entry_username.get()
        self.email = self.entry_email.get()
        self.password = self.entry_password.get()
        self.rep_pass = self.entry_rep_pass.get()

        if self.check_validation():

            self.sql.push_db(self.email, self.username, self.password)

            self.clear_entires()


    def clear_entires(self):

        self.entry_username.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_password.delete(0, "end")
        self.entry_rep_pass.delete(0, "end")


    def ui_setup(self):
        labels_frame = ttk.Frame(master=self.root)
        username_lbl = ttk.Label(master=labels_frame, text="Username:")
        email_lbl = ttk.Label(master=labels_frame, text="Email Address:")
        password_lbl = ttk.Label(master=labels_frame, text="Password:")
        rep_pass_lbl = ttk.Label(master=labels_frame, text="Repeat Password:")

        labels_frame.grid(column=0, row=0, padx=5, pady=5)

        username_lbl.grid(column=0, row=0, sticky="W", pady=5)
        email_lbl.grid(column=0, row=1, sticky="W", pady=5)
        password_lbl.grid(column=0, row=2, sticky="W", pady=5)
        rep_pass_lbl.grid(column=0, row=3, sticky="W", pady=5)

        # ENTRY

        entry_frame = ttk.Frame(master=self.root)

        entry_frame.grid(column=1, row=0, padx=5, pady=5)

        self.entry_username = ttk.Entry(master=entry_frame)
        self.entry_username.focus()
        self.entry_email = ttk.Entry(master=entry_frame)
        self.entry_password = ttk.Entry(master=entry_frame)
        self.entry_rep_pass = ttk.Entry(master=entry_frame)

        self.entry_username.grid(column=0, row=0, sticky="W", pady=5)
        self.entry_email.grid(column=0, row=1, sticky="W", pady=5)
        self.entry_password.grid(column=0, row=2, sticky="W", pady=5)
        self.entry_rep_pass.grid(column=0, row=3, sticky="W", pady=5)

        # Button

        sign_btn = ttk.Button(text="Sign up!", command=self.get_user)

        sign_btn.grid(column=0, row=2, columnspan=2, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = CreateUser(root)
    root.mainloop()
