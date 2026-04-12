#-------------------------------#
#     BIT502 - Assessment 3     #
#         Thomas Bernard        #
#      Student ID 5142644       #
#-------------------------------#

import sqlite3
import tkinter as tk
import os
from tkinter import *
from tkinter import messagebox

# ------------------------------
# Database Setup
# ------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "theauroraarchive_database.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Memberships (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_Name TEXT,
    Last_Name TEXT,
    Address TEXT,
    Mobile TEXT,
    Membership_Plan TEXT,
    Payment_Plan TEXT,
    Extra_Book_Rental INTEGER,
    Extra_Private_Area INTEGER,
    Extra_Booklet INTEGER,
    Extra_Ebook_Rental INTEGER,
    Has_Library_Card INTEGER,
    Library_Card_Number TEXT
)
""")
conn.commit()

# ------------------------------
# Tkinter Setup
# ------------------------------

window = tk.Tk()
window.title("The Aurora Archive")

# ❌ Block closing via window X
def block_close():
    messagebox.showinfo("Exit Disabled", "Please exit via the menu of the program only.")

window.protocol("WM_DELETE_WINDOW", block_close)

# ⭐ Minimum size so title bar always visible
window.minsize(550, 500)

# Default size for form
window.geometry("550x700")

# ------------------------------
# Clear Window
# ------------------------------

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# ------------------------------
# Validation Functions
# ------------------------------

def only_five_digits(new_value):
    return new_value.isdigit() and len(new_value) <= 5 or new_value == ""

def only_letters(new_value):
    return all(char.isalpha() or char == " " for char in new_value) or new_value == ""

def only_numbers(new_value):
    return new_value.isdigit() or new_value == ""

# ------------------------------
# Global Variables
# ------------------------------

membership_cost = 0
extras_cost = 0
discount = 0
total_cost = 0
weekly_cost = 0

plan_standard = "Standard - $10"
plan_premium = "Premium - $15"
plan_kids = "Kids - $5"

plan_monthly = "Monthly"
plan_annual = "Annual"

optional_1 = "Book Rental"
optional_2 = "Private Area Access"
optional_3 = "Monthly Booklet"
optional_4 = "Online Ebook Rental"

membership_plan = tk.StringVar(window, plan_standard)
payment_plan = tk.StringVar(window, plan_monthly)

extra1 = tk.BooleanVar(window, False)
extra2 = tk.BooleanVar(window, False)
extra3 = tk.BooleanVar(window, False)
extra4 = tk.BooleanVar(window, False)

has_library_card = tk.BooleanVar(window, False)

# ------------------------------
# Live Update
# ------------------------------

def update_totals(*args):
    try:
        calculate()
    except:
        pass

def update_totals_key(event):
    try:
        calculate()
    except:
        pass

membership_plan.trace_add("write", update_totals)
payment_plan.trace_add("write", update_totals)
extra1.trace_add("write", update_totals)
extra2.trace_add("write", update_totals)
extra3.trace_add("write", update_totals)
extra4.trace_add("write", update_totals)
has_library_card.trace_add("write", update_totals)

# ------------------------------
# Reset Function
# ------------------------------

def reset_form():
    entry_first_name.delete(0, END)
    entry_last_name.delete(0, END)
    entry_address.delete(0, END)
    entry_mobile.delete(0, END)
    entry_library_number.delete(0, END)

    membership_plan.set(plan_standard)
    payment_plan.set(plan_monthly)

    extra1.set(False)
    extra2.set(False)
    extra3.set(False)
    extra4.set(False)

    has_library_card.set(False)

    label_total_cost_base.config(text="--")
    label_total_cost_extras.config(text="--")
    label_total_cost_discount.config(text="--")
    label_total_cost_total.config(text="--")
    label_total_cost_weekly.config(text="--")

    entry_first_name.config(bg="white")
    entry_last_name.config(bg="white")
    entry_address.config(bg="white")
    entry_mobile.config(bg="white")
    entry_library_number.config(bg="white")

# ------------------------------
# Calculate Function
# ------------------------------

def calculate():
    global membership_cost, extras_cost, discount, total_cost, weekly_cost

    # Red error highlighting
    entry_first_name.config(bg="white")
    entry_last_name.config(bg="white")
    entry_address.config(bg="white")
    entry_mobile.config(bg="white")
    entry_library_number.config(bg="white")

    if entry_first_name.get().strip() == "":
        entry_first_name.config(bg="misty rose")

    if entry_last_name.get().strip() == "":
        entry_last_name.config(bg="misty rose")

    if entry_address.get().strip() == "":
        entry_address.config(bg="misty rose")

    mobile_val = entry_mobile.get().strip()
    if mobile_val == "" or not mobile_val.isdigit():
        entry_mobile.config(bg="misty rose")

    if has_library_card.get():
        card_val = entry_library_number.get().strip()
        if card_val == "" or not (card_val.isdigit() and len(card_val) == 5):
            entry_library_number.config(bg="misty rose")

    # Base membership cost
    if membership_plan.get() == plan_standard:
        base_price = 10
    elif membership_plan.get() == plan_premium:
        base_price = 15
    else:
        base_price = 5

    # Extras
    extras_total = 0
    if extra1.get(): extras_total += 5
    if extra2.get(): extras_total += 15
    if extra3.get(): extras_total += 2
    if extra4.get(): extras_total += 5

    # Monthly vs Annual
    if payment_plan.get() == plan_monthly:
        membership_cost = base_price
        extras_cost = extras_total
    else:
        membership_cost = base_price * 11
        extras_cost = extras_total * 12

    # Discount
    discount = 0
    card = entry_library_number.get()
    if has_library_card.get() and card.isdigit() and len(card) == 5:
        discount = (membership_cost + extras_cost) * 0.10

    total_cost = membership_cost + extras_cost - discount

    # Weekly cost
    if payment_plan.get() == plan_monthly:
        weekly_cost = total_cost / 4
    else:
        weekly_cost = total_cost / 52

    # Update labels
    label_total_cost_base.config(text=f"${membership_cost:.2f}")
    label_total_cost_extras.config(text=f"${extras_cost:.2f}")
    label_total_cost_discount.config(text=f"${discount:.2f}")
    label_total_cost_total.config(text=f"${total_cost:.2f}")
    label_total_cost_weekly.config(text=f"${weekly_cost:.2f}")

# ------------------------------
# Submit Function
# ------------------------------

def submit():
    first = entry_first_name.get()
    last = entry_last_name.get()
    address = entry_address.get()
    mobile = entry_mobile.get()
    card = entry_library_number.get()

    # Reset colours
    entry_first_name.config(bg="white")
    entry_last_name.config(bg="white")
    entry_address.config(bg="white")
    entry_mobile.config(bg="white")
    entry_library_number.config(bg="white")

    errors = False
    empty_fields = []

    if first.strip() == "":
        entry_first_name.config(bg="red")
        empty_fields.append("First name")
        errors = True

    if last.strip() == "":
        entry_last_name.config(bg="red")
        empty_fields.append("Last name")
        errors = True

    if address.strip() == "":
        entry_address.config(bg="red")
        empty_fields.append("Address")
        errors = True

    if mobile.strip() == "":
        entry_mobile.config(bg="red")
        empty_fields.append("Mobile")
        errors = True
    elif not mobile.isdigit():
        entry_mobile.config(bg="red")
        errors = True

    if has_library_card.get():
        if card.strip() == "":
            entry_library_number.config(bg="red")
            empty_fields.append("Library card number")
            errors = True
        elif not (card.isdigit() and len(card) == 5):
            entry_library_number.config(bg="red")
            messagebox.showwarning("Invalid Library Card", "Library card number must be exactly 5 digits.")
            errors = True

    if errors:
        if empty_fields:
            messagebox.showwarning("Error", "These fields are empty or invalid:\n" + "\n".join(empty_fields))
        else:
            messagebox.showwarning("Error", "Some fields contain invalid data.")
        return

    # Insert into database
    cursor.execute("""
        INSERT INTO Memberships 
        (First_Name, Last_Name, Address, Mobile, Membership_Plan, Payment_Plan,
         Extra_Book_Rental, Extra_Private_Area, Extra_Booklet, Extra_Ebook_Rental,
         Has_Library_Card, Library_Card_Number)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        first, last, address, mobile,
        membership_plan.get(), payment_plan.get(),
        int(extra1.get()), int(extra2.get()), int(extra3.get()), int(extra4.get()),
        int(has_library_card.get()), card if has_library_card.get() else ""
    ))

    conn.commit()
    messagebox.showinfo("Success", "Membership submitted!")
    reset_form()

# ------------------------------
# MEMBERSHIP FORM SCREEN
# ------------------------------

def open_membership_form():
    clear_window()

    # Restore full form size
    window.geometry("550x700")

    global entry_first_name, entry_last_name, entry_address, entry_mobile
    global entry_library_number
    global label_total_cost_base, label_total_cost_extras, label_total_cost_discount
    global label_total_cost_total, label_total_cost_weekly

    # PERSONAL DETAILS (LEFT)
    frame_personal = tk.LabelFrame(window, text="Personal Details", padx=10, pady=10)
    frame_personal.grid(row=0, column=0, padx=10, pady=5, sticky="nw")
    frame_personal.grid_columnconfigure(1, weight=1)

    vcmd_name = (window.register(only_letters), "%P")
    vcmd_mobile = (window.register(only_numbers), "%P")
    vcmd_card = (window.register(only_five_digits), "%P")

    tk.Label(frame_personal, text="First Name:*").grid(row=0, column=0, sticky="w")
    entry_first_name = tk.Entry(frame_personal, validate="key", validatecommand=vcmd_name)
    entry_first_name.grid(row=0, column=1, sticky="we")

    tk.Label(frame_personal, text="Last Name:*").grid(row=1, column=0, sticky="w")
    entry_last_name = tk.Entry(frame_personal, validate="key", validatecommand=vcmd_name)
    entry_last_name.grid(row=1, column=1, sticky="we")

    tk.Label(frame_personal, text="Address:*").grid(row=2, column=0, sticky="w")
    entry_address = tk.Entry(frame_personal)
    entry_address.grid(row=2, column=1, sticky="we")

    tk.Label(frame_personal, text="Mobile:*").grid(row=3, column=0, sticky="w")
    entry_mobile = tk.Entry(frame_personal, validate="key", validatecommand=vcmd_mobile)
    entry_mobile.grid(row=3, column=1, sticky="we")

    entry_first_name.bind("<KeyRelease>", update_totals_key)
    entry_last_name.bind("<KeyRelease>", update_totals_key)
    entry_address.bind("<KeyRelease>", update_totals_key)
    entry_mobile.bind("<KeyRelease>", update_totals_key)

    # MEMBERSHIP PLAN (LEFT)
    frame_membership = tk.LabelFrame(window, text="Membership Plan", padx=10, pady=10)
    frame_membership.grid(row=1, column=0, padx=10, pady=5, sticky="nw")

    tk.Radiobutton(frame_membership, text=plan_standard, variable=membership_plan, value=plan_standard).grid(row=0, column=0, sticky="w")
    tk.Radiobutton(frame_membership, text=plan_premium, variable=membership_plan, value=plan_premium).grid(row=1, column=0, sticky="w")
    tk.Radiobutton(frame_membership, text=plan_kids, variable=membership_plan, value=plan_kids).grid(row=2, column=0, sticky="w")

    # OPTIONAL EXTRAS (LEFT)
    frame_extras = tk.LabelFrame(window, text="Optional Extras", padx=10, pady=10)
    frame_extras.grid(row=2, column=0, padx=10, pady=5, sticky="nw")

    tk.Checkbutton(frame_extras, text=optional_1, variable=extra1).grid(row=0, column=0, sticky="w")
    tk.Checkbutton(frame_extras, text=optional_2, variable=extra2).grid(row=1, column=0, sticky="w")
    tk.Checkbutton(frame_extras, text=optional_3, variable=extra3).grid(row=2, column=0, sticky="w")
    tk.Checkbutton(frame_extras, text=optional_4, variable=extra4).grid(row=3, column=0, sticky="w")

    # PAYMENT PLAN (RIGHT)
    frame_payment = tk.LabelFrame(window, text="Payment Plan", padx=10, pady=10)
    frame_payment.grid(row=0, column=1, padx=10, pady=5, sticky="ne")

    tk.Radiobutton(frame_payment, text=plan_monthly, variable=payment_plan, value=plan_monthly).grid(row=0, column=0, sticky="w")
    tk.Radiobutton(frame_payment, text=plan_annual, variable=payment_plan, value=plan_annual).grid(row=1, column=0, sticky="w")

    # LIBRARY CARD (RIGHT)
    frame_library = tk.LabelFrame(window, text="Library Card", padx=10, pady=10)
    frame_library.grid(row=1, column=1, padx=10, pady=5, sticky="ne")
    frame_library.grid_columnconfigure(1, weight=1)

    tk.Checkbutton(frame_library, text="Has Library Card", variable=has_library_card).grid(row=0, column=0, sticky="w")

    tk.Label(frame_library, text="Card Number:").grid(row=1, column=0, sticky="w")
    entry_library_number = tk.Entry(frame_library, validate="key", validatecommand=vcmd_card)
    entry_library_number.grid(row=1, column=1, sticky="we")

    entry_library_number.bind("<KeyRelease>", update_totals_key)

    # TOTALS (BOTTOM FULL WIDTH)
    frame_totals = tk.LabelFrame(window, text="Totals", padx=10, pady=10)
    frame_totals.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")
    frame_totals.grid_columnconfigure(1, weight=1)

    tk.Label(frame_totals, text="Membership Cost:").grid(row=0, column=0, sticky="w")
    label_total_cost_base = tk.Label(frame_totals, text="--")
    label_total_cost_base.grid(row=0, column=1, sticky="e")

    tk.Label(frame_totals, text="Extras Cost:").grid(row=1, column=0, sticky="w")
    label_total_cost_extras = tk.Label(frame_totals, text="--")
    label_total_cost_extras.grid(row=1, column=1, sticky="e")

    tk.Label(frame_totals, text="Discount:").grid(row=2, column=0, sticky="w")
    label_total_cost_discount = tk.Label(frame_totals, text="--")
    label_total_cost_discount.grid(row=2, column=1, sticky="e")

    tk.Label(frame_totals, text="Total Cost:").grid(row=3, column=0, sticky="w")
    label_total_cost_total = tk.Label(frame_totals, text="--")
    label_total_cost_total.grid(row=3, column=1, sticky="e")

    tk.Label(frame_totals, text="Weekly Cost:").grid(row=4, column=0, sticky="w")
    label_total_cost_weekly = tk.Label(frame_totals, text="--")
    label_total_cost_weekly.grid(row=4, column=1, sticky="e")

    # BUTTONS (BOTTOM FULL WIDTH)
    tk.Button(window, text="Calculate", command=calculate).grid(row=4, column=0, pady=10)
    tk.Button(window, text="Submit", command=submit).grid(row=4, column=1, pady=10)
    tk.Button(window, text="Reset", command=reset_form).grid(row=5, column=0, pady=10)
    tk.Button(window, text="Back to Menu", command=open_main_menu).grid(row=5, column=1, pady=10)

# ------------------------------
# OTHER SCREENS
# ------------------------------

def open_search_form():
    clear_window()
    window.geometry("550x500")

    Label(window, text="Search Screen Coming Soon").pack(pady=20)
    Button(window, text="Back to Menu", command=open_main_menu).pack(pady=10)

def open_statistics_form():
    clear_window()
    window.geometry("550x500")

    Label(window, text="Statistics Screen Coming Soon").pack(pady=20)
    Button(window, text="Back to Menu", command=open_main_menu).pack(pady=10)

def open_help_screen():
    clear_window()
    window.geometry("550x500")

    Label(window, text="Help Screen Coming Soon").pack(pady=20)
    Button(window, text="Back to Menu", command=open_main_menu).pack(pady=10)

# ------------------------------
# MAIN MENU
# ------------------------------

def open_main_menu():
    clear_window()

    # Menu size (matches your screenshot)
    window.geometry("550x500")

    Label(window, text="Main Menu", font=("Arial", 20, "bold")).pack(pady=20)

    Button(window, text="Membership Form", width=25, command=open_membership_form).pack(pady=10)
    Button(window, text="Search Members", width=25, command=open_search_form).pack(pady=10)
    Button(window, text="Statistics", width=25, command=open_statistics_form).pack(pady=10)
    Button(window, text="Help", width=25, command=open_help_screen).pack(pady=10)

    Button(window, text="Exit", width=25, command=window.destroy).pack(pady=20)

# ------------------------------
# START PROGRAM
# ------------------------------

open_main_menu()
window.mainloop()
