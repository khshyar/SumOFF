import tkinter as tk
from tkinter import ttk, font
from db.mysql_python_connector import push_db

class CreateUser:
    def __init__(self, root):
        self.root = root
        self.root.title("Create a new user!")
        self.root.geometry("250x180")
        self.ui_setup()


# COMMANDS

    def get_user(self):

        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        rep_pass = self.entry_rep_pass.get()

        push_db(email, username, password)

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
