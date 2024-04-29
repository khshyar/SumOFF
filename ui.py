import tkinter as tk
from tkinter import ttk, font
from tkinter import messagebox
from db.mysql_python_connector import SqlPy

class CreateUser:
    def __init__(self, root):
        self.root = root
        self.root.title("Create a new user!")
        self.root.geometry("250x200")
        self.root.resizable(0, 0)
        self.ui_setup()


# COMMANDS

    def check_validation(self):
        
        letters_lower = set('abcdefghijklmnopqrstuvwxyz')
        letters_upper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        numbers = set('0123456789')
        symbols = set('!@#$%^&*()')
        mail_val = set('@.')

        contains_lower = any(char in self.password for char in letters_lower)
        contains_upper = any(char in self.password for char in letters_upper)
        contains_number = any(char in self.password for char in numbers)
        contains_symbol = any(char in self.password for char in symbols)
        contains_at = any(char in self.email for char in mail_val)

        if len(self.username) >= 4:
            if not any(char in self.username for char in symbols):
                if len(self.email) >= 8:
                    if contains_at:
                        if len(self.password) >= 8:
                            if contains_lower and contains_upper and contains_number and contains_symbol:
                                if self.password == self.rep_pass:
                                    return True
                                else:
                                    messagebox.showwarning(title="Error", message="Please make sure you entered your password twice correctly")
                            else:
                                messagebox.showwarning(title="Error", message="Please make sure you've put all symbols, lower-case, upper-case, numbers in your password!")
                        else:
                            messagebox.showwarning(title="Error", message="Please make sure the password you entered is equal or more than 8 characters!")
                    else:
                            messagebox.showwarning(title="Error", message="Please make sure you entered your Email Correctly!")
                else:
                    messagebox.showwarning(title="Error", message="Please make sure you entered your Email Correctly!")
            else:
                messagebox.showwarning(title="Error", message="Please make sure your username doesnt contain any special characters!")
        else:
            messagebox.showwarning(title="Error", message="Please make sure your username is more than 4 characters!")


                

    def get_user(self):

        sql = SqlPy()

        if self.check_validation():
            if sql.user_exists(self.username, self.email) == "username":
                messagebox.showerror(title="error", message="This Username alrady Exists!")
            elif sql.user_exists(self.username, self.email) == "email":
                messagebox.showerror(title="error", message="This Email alrady Exists!")
            else:
                sql.push_db(self.email, self.username, self.password)

                messagebox.showinfo(title="Done", message="Sign up Completed!")

                self.clear_entires()
    

    def get_user_data(self):
        self.username = self.entry_username.get().lower()
        self.email = self.entry_email.get().lower()
        self.password = self.entry_password.get()
        self.rep_pass = self.entry_rep_pass.get()


    def enable_button(self):
        # Get the current values from the entry fields
        self.username = self.entry_username.get().lower()
        self.email = self.entry_email.get().lower()
        self.password = self.entry_password.get()
        self.rep_pass = self.entry_rep_pass.get()
        
        # Check if all conditions are met to enable the button
        if (len(self.password) > 7 and 
            len(self.rep_pass) > 7 and 
            len(self.username) > 4 and 
            len(self.email) > 7):
            self.sign_btn.config(state="normal")
        else:
            self.sign_btn.config(state="disabled")
        
        # Schedule the enable_button method to run again after 100 milliseconds
        self.root.after(100, self.get_user_data)

    def clear_entires(self):

        self.entry_username.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_password.delete(0, "end")
        self.entry_rep_pass.delete(0, "end")

    def checked(self):
        if self.on_or_off.get() == True:
            self.entry_password.config(show="")
            self.entry_rep_pass.config(show="")
        else:
            self.entry_password.config(show="*")
            self.entry_rep_pass.config(show="*")


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
        self.entry_password = ttk.Entry(master=entry_frame, show="*")
        self.entry_rep_pass = ttk.Entry(master=entry_frame, show="*")

        self.entry_username.grid(column=0, row=0, sticky="W", pady=10)
        self.entry_email.grid(column=0, row=1, sticky="W", pady=5)
        self.entry_password.grid(column=0, row=2, sticky="W", pady=5)
        self.entry_rep_pass.grid(column=0, row=3, sticky="W", pady=5)

        #Checkbox
        self.on_or_off = tk.BooleanVar()
        pass_checkbox = ttk.Checkbutton(text="Show password",variable=self.on_or_off, command=self.checked, state='!alternate')
        pass_checkbox.grid(column=0, row=2, columnspan=2, padx=5, sticky="W")

        # Button
        self.sign_btn = ttk.Button(text="Sign up!", command=self.get_user, state="disabled")
        self.sign_btn.grid(column=0, row=3, columnspan=2, pady=8)

        # self.username = self.entry_username.get().lower()
        # self.email = self.entry_email.get()
        # self.password = self.entry_password.get()
        # self.rep_pass = self.entry_rep_pass.get()

        self.enable_button()

if __name__ == "__main__":
    root = tk.Tk()
    app = CreateUser(root)
    root.mainloop()