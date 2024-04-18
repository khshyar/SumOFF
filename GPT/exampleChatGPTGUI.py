import tkinter as tk
from db.mysql_python_connector import DatabaseConnector

class UserCreationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Create a new user!")
        self.db_connector = DatabaseConnector()
        self.setup_widgets()

    def setup_widgets(self):
        labels_frame = tk.Frame(master=self.root)
        username_lbl = tk.Label(master=labels_frame, text="Username:")
        email_lbl = tk.Label(master=labels_frame, text="Email Address:")
        password_lbl = tk.Label(master=labels_frame, text="Password:")
        rep_pass_lbl = tk.Label(master=labels_frame, text="Repeat Password:")
        labels_frame.grid(column=0, row=0, padx=5, pady=5)
        username_lbl.grid(column=0, row=0, sticky="W", pady=5)
        email_lbl.grid(column=0, row=1, sticky="W", pady=5)
        password_lbl.grid(column=0, row=2, sticky="W", pady=5)
        rep_pass_lbl.grid(column=0, row=3, sticky="W", pady=5)
        # Entries
        entry_frame = tk.Frame(master=self.root)
        entry_frame.grid(column=1, row=0, padx=5, pady=5)
        self.entry_username = tk.Entry(master=entry_frame)
        self.entry_email = tk.Entry(master=entry_frame)
        self.entry_password = tk.Entry(master=entry_frame)
        self.entry_rep_pass = tk.Entry(master=entry_frame)
        self.entry_username.grid(column=0, row=0, sticky="W", pady=5)
        self.entry_email.grid(column=0, row=1, sticky="W", pady=5)
        self.entry_password.grid(column=0, row=2, sticky="W", pady=5)
        self.entry_rep_pass.grid(column=0, row=3, sticky="SW", pady=5)
        # Button
        sign_btn = tk.Button(text="Sign up!", command=self.get_user)
        sign_btn.grid(column=0, row=2, columnspan=2, pady=5)

    def get_user(self):
        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        rep_pass = self.entry_rep_pass.get()
        if self.validate_input(username, email, password, rep_pass):
            self.db_connector.push_db(email, username, password)
            self.clear_entries()

    def validate_input(self, username, email, password, rep_pass):
        # Implement validation logic here
        return True

    def clear_entries(self):
        self.entry_username.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_password.delete(0, "end")
        self.entry_rep_pass.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserCreationApp(root)
    root.mainloop()
