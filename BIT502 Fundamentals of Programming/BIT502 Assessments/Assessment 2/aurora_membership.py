
# BIT502 - Assessment 2
# Thomas Bernard 
# Student ID 5142644 

import tkinter as tk

root = tk.Tk()
root.title("Aurora Archive Membership Form")
root.geometry("800x600")

# personal details frame

frame_personal = tk.LabelFrame(
    root,
    text="Personal Details",
    bg="lightblue",
    padx=20,
    pady=20
)
frame_personal.pack(fill="x", padx=20, pady=20)

frame_membership = tk.LabelFrame(
    root,
    text="Membership Options",
    bg="lightblue",
    padx=20,
    pady=20
)
frame_membership.pack(fill="x", padx=20, pady=20)

frame_extras = tk.LabelFrame(
    root,
    text="Extras",
    bg="lightblue",
    padx=20,
    pady=20
)
frame_extras.pack(fill="x", padx=20, pady=20)

frame_totals = tk.LabelFrame(
    root,
    text="totals",
    bg="lightblue",
    padx=20,
    pady=20
)
frame_totals .pack(fill="x", padx=20, pady=20)

frame_buttons = tk.Frame(root, padx=10, pady=10)
frame_buttons.pack(fill="x", padx=10, pady=10)


root.mainloop()

