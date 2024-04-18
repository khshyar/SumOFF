import tkinter as tk

root = tk.Tk()
root.title("Create a new user!")


#COMMANDS 

def get_user():

    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    rep_pass = entry_rep_pass.get()

    entry_username.delete(0, "end")
    entry_email.delete(0, "end")
    entry_password.delete(0, "end")
    entry_rep_pass.delete(0, "end")


labels_frame = tk.Frame(master=root) 
username_lbl = tk.Label(master=labels_frame ,text="Username:")
email_lbl = tk.Label(master=labels_frame, text="Email Address:")
password_lbl = tk.Label(master=labels_frame, text="Password:")
rep_pass_lbl = tk.Label(master=labels_frame, text="Repeat Password:")

labels_frame.grid(column=0, row=0, padx=5, pady=5)

username_lbl.grid(column=0, row=0, sticky="W", pady=5)
email_lbl.grid(column=0, row=1, sticky="W", pady=5)
password_lbl.grid(column=0, row=2, sticky="W", pady=5)
rep_pass_lbl.grid(column=0, row=3, sticky="W", pady=5)

#ENTRY

entry_frame = tk.Frame(master=root)

entry_frame.grid(column=1, row=0, padx=5, pady=5)

entry_username = tk.Entry(master=entry_frame)
entry_email = tk.Entry(master=entry_frame)
entry_password = tk.Entry(master=entry_frame)
entry_rep_pass = tk.Entry(master=entry_frame)

entry_username.grid(column=0, row=0, sticky="W", pady=5)
entry_email.grid(column=0, row=1, sticky="W", pady=5)
entry_password.grid(column=0, row=2, sticky="W", pady=5)
entry_rep_pass.grid(column=0, row=3, sticky="SW", pady=5)

#Button

sign_btn = tk.Button(text="Sign up!", command=get_user)

sign_btn.grid(column=0, row=2, columnspan=2, pady=5)



root.mainloop()