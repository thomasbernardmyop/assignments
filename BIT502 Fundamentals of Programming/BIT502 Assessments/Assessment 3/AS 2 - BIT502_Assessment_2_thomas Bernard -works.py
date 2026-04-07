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



# Setup database connection
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "theauroraarchive_database.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


#### Clear windows when switching

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# ------------------------------
# Tkinter setup
# ------------------------------

window = tk.Tk()
window.withdraw()   # Hide membership form at startup
window.title("The Aurora Archive")
window.geometry("550x658")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# ------------------------------
# Global Variables
# ------------------------------

membership_cost = 0
extras_cost = 0
discount = 0
total_cost = 0
weekly_cost = 0

# ------------------------------
# Variables
# ------------------------------

plan_standard = "Standard - $10 "
plan_premium = "Premium - $15 "
plan_kids = "Kids - $5 "

plan_monthly = "Monthly"
plan_annual = "Annual"

optional_1 = "Book Rental"
optional_2 = "Private Area Access"
optional_3 = "Monthly Booklet"
optional_4 = "Online ebook Rental"

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
    calculate()

def update_totals_key(event):
    calculate()

membership_plan.trace_add("write", update_totals)
payment_plan.trace_add("write", update_totals)
extra1.trace_add("write", update_totals)
extra2.trace_add("write", update_totals)
extra3.trace_add("write", update_totals)
extra4.trace_add("write", update_totals)
has_library_card.trace_add("write", update_totals)

# ------------------------------
# Validation Functions
# ------------------------------

def only_five_digits(new_value):
    if new_value == "":
        return True
    return new_value.isdigit() and len(new_value) <= 5

def only_letters(new_value):
    if new_value == "":
        return True
    return all(char.isalpha() or char == " " for char in new_value)

def only_numbers(new_value):
    if new_value == "":
        return True
    return new_value.isdigit()

# ------------------------------
# Reset Function
# ------------------------------

def reset_form():
    answer = messagebox.askyesno("Reset Form", "Are you sure you want to reset the form?")
    if answer:
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
        label_total_cost_annual.config(text="--")
        label_total_cost_discount.config(text="--")
        label_total_cost_total.config(text="--")
        label_total_cost_weekly.config(text="--")

        global membership_cost, extras_cost, discount, total_cost, weekly_cost
        membership_cost = 0
        extras_cost = 0
        discount = 0
        total_cost = 0
        weekly_cost = 0

# ------------------------------
# Calculate Function
# ------------------------------

def calculate():
    global membership_cost, extras_cost, discount, total_cost, weekly_cost

    choice = membership_plan.get()

    if choice == plan_standard:
        base_price = 10
    elif choice == plan_premium:
        base_price = 15
    elif choice == plan_kids:
        base_price = 5
    else:
        base_price = 0

    extras_total = 0
    if extra1.get():
        extras_total += 5
    if extra2.get():
        extras_total += 15
    if extra3.get():
        extras_total += 2
    if extra4.get():
        extras_total += 5

    plan = payment_plan.get()

    if plan == plan_monthly:
        membership_cost = base_price
        extras_cost = extras_total
    else:
        membership_cost = base_price * 11
        extras_cost = extras_total * 12

    label_total_cost_base.config(text=f"${membership_cost:.2f}")
    label_total_cost_extras.config(text=f"${extras_cost:.2f}")

    annual_cost = membership_cost + extras_cost
    if plan == plan_annual:
        label_total_cost_annual.config(text=f"${annual_cost:.2f}")
    else:
        label_total_cost_annual.config(text="N/A")

    total_cost = membership_cost + extras_cost

    discount = 0
    card = entry_library_number.get()
    if has_library_card.get() and card.isdigit() and len(card) == 5:
        discount = total_cost * 0.10

    total_cost -= discount

    if plan == plan_monthly:
        weekly_cost = total_cost / 4
    else:
        weekly_cost = total_cost / 52

    label_total_cost_discount.config(text=f"${discount:.2f}")
    label_total_cost_total.config(text=f"${total_cost:.2f}")
    label_total_cost_weekly.config(text=f"${weekly_cost:.2f}")

# ------------------------------
# Submit Function
# ------------------------------

def submit():
    global membership_cost, extras_cost, discount, total_cost, weekly_cost

    first = entry_first_name.get()
    last = entry_last_name.get()
    mobile = entry_mobile.get()
    card = entry_library_number.get()

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

    if entry_address.get().strip() == "":
        entry_address.config(bg="red")
        empty_fields.append("Address")
        errors = True

    if mobile.strip() == "":
        entry_mobile.config(bg="red")
        empty_fields.append("Mobile")
        errors = True

    if mobile.strip() != "" and not mobile.isdigit():
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
            messagebox.showwarning("Error", "These fields are empty:\n" + "\n".join(empty_fields))
        else:
            messagebox.showwarning("Error", "Some fields contain invalid data.")
        return

    # Save to Database
    extra_book_rental = 1 if extra1.get() else 0
    extra_private_area = 1 if extra2.get() else 0
    extra_booklet = 1 if extra3.get() else 0
    extra_ebook_rental = 1 if extra4.get() else 0
    has_card = 1 if has_library_card.get() else 0
    card_number = entry_library_number.get() if has_library_card.get() else ""

    try:
        cursor.execute("""
            INSERT INTO Memberships 
            (First_Name, Last_Name, Address, Mobile, Membership_Plan, Payment_Plan,
             Extra_Book_Rental, Extra_Private_Area, Extra_Booklet, Extra_Ebook_Rental,
             Has_Library_Card, Library_Card_Number)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            first,
            last,
            entry_address.get(),
            mobile,
            membership_plan.get(),
            payment_plan.get(),
            extra_book_rental,
            extra_private_area,
            extra_booklet,
            extra_ebook_rental,
            has_card,
            card_number
        ))

        conn.commit()
        messagebox.showinfo("Success", "Membership information submitted successfully!")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return

    reset_form()

    # ------------------------------
# Personal Details Frame
# ------------------------------

frame_personal = tk.LabelFrame(window, text="Personal Details", padx=10, pady=10)
frame_personal.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="we")

label_first_name = tk.Label(frame_personal, text="First Name:*")
label_last_name = tk.Label(frame_personal, text="Last Name:*")
label_address = tk.Label(frame_personal, text="Address:*")
label_mobile = tk.Label(frame_personal, text="Mobile:*")

vcmd_name = (window.register(only_letters), "%P")
vcmd_mobile = (window.register(only_numbers), "%P")

entry_first_name = tk.Entry(frame_personal, validate="key", validatecommand=vcmd_name)
entry_last_name = tk.Entry(frame_personal, validate="key", validatecommand=vcmd_name)
entry_address = tk.Entry(frame_personal)
entry_mobile = tk.Entry(frame_personal, validate="key", validatecommand=vcmd_mobile)

label_first_name.grid(row=0, column=0, sticky="w", pady=2)
entry_first_name.grid(row=0, column=1, sticky="we")

label_last_name.grid(row=1, column=0, sticky="w", pady=2)
entry_last_name.grid(row=1, column=1, sticky="we")

label_address.grid(row=2, column=0, sticky="w", pady=2)
entry_address.grid(row=2, column=1, sticky="we")

label_mobile.grid(row=3, column=0, sticky="w", pady=2)
entry_mobile.grid(row=3, column=1, sticky="we")

entry_first_name.bind("<KeyRelease>", update_totals_key)
entry_last_name.bind("<KeyRelease>", update_totals_key)
entry_address.bind("<KeyRelease>", update_totals_key)
entry_mobile.bind("<KeyRelease>", update_totals_key)

# ------------------------------
# Membership Plan Frame
# ------------------------------

frame_membership = tk.LabelFrame(window, text="Membership Plan *", padx=10, pady=10)
frame_membership.grid(row=1, column=0, padx=10, pady=5, sticky="we")

label_membership_type = tk.Label(frame_membership, text="Membership Plan: ")
radio_membership_1 = tk.Radiobutton(frame_membership, text=plan_standard, variable=membership_plan, value=plan_standard)
radio_membership_2 = tk.Radiobutton(frame_membership, text=plan_premium, variable=membership_plan, value=plan_premium)
radio_membership_3 = tk.Radiobutton(frame_membership, text=plan_kids, variable=membership_plan, value=plan_kids)

label_membership_type.grid(row=0, column=0, sticky="w")
radio_membership_1.grid(row=0, column=1, sticky="w")
radio_membership_2.grid(row=1, column=1, sticky="w")
radio_membership_3.grid(row=2, column=1, sticky="w")

# ------------------------------
# Payment Plan Frame
# ------------------------------

frame_payment = tk.LabelFrame(window, text="Payment Plan *️", padx=10, pady=10)
frame_payment.grid(row=1, column=1, padx=10, pady=5, sticky="we")

label_membership_payment_plan = tk.Label(frame_payment, text="Payment Plan:")
radio_payment_plan_1 = tk.Radiobutton(frame_payment, text=plan_monthly, variable=payment_plan, value=plan_monthly)
radio_payment_plan_2 = tk.Radiobutton(frame_payment, text=plan_annual, variable=payment_plan, value=plan_annual)

label_membership_payment_plan.grid(row=0, column=0, sticky="w")
radio_payment_plan_1.grid(row=0, column=1, sticky="w")
radio_payment_plan_2.grid(row=1, column=1, sticky="w")

# ------------------------------
# Optional Extras Frame
# ------------------------------

frame_extras = tk.LabelFrame(window, text="Optional Extras", padx=10, pady=10)
frame_extras.grid(row=2, column=0, padx=10, pady=5, sticky="we")

checkbutton_extra1 = tk.Checkbutton(frame_extras, text=optional_1, variable=extra1)
checkbutton_extra2 = tk.Checkbutton(frame_extras, text=optional_2, variable=extra2)
checkbutton_extra3 = tk.Checkbutton(frame_extras, text=optional_3, variable=extra3)
checkbutton_extra4 = tk.Checkbutton(frame_extras, text=optional_4, variable=extra4)

checkbutton_extra1.grid(row=0, column=0, sticky="w")
checkbutton_extra2.grid(row=1, column=0, sticky="w")
checkbutton_extra3.grid(row=2, column=0, sticky="w")
checkbutton_extra4.grid(row=3, column=0, sticky="w")

# ------------------------------
# Library Card Frame
# ------------------------------

frame_library = tk.LabelFrame(window, text="Library Card", padx=10, pady=10)
frame_library.grid(row=2, column=1, padx=10, pady=5, sticky="we")

label_library_card = tk.Label(frame_library, text="Has Library Card:")
checkbutton_has_library_card = tk.Checkbutton(frame_library, variable=has_library_card)

vcmd = (window.register(only_five_digits), "%P")
label_library_number = tk.Label(frame_library, text="Card Number:")
entry_library_number = tk.Entry(frame_library, validate="key", validatecommand=vcmd)

label_library_card.grid(row=0, column=0, sticky="w")
checkbutton_has_library_card.grid(row=0, column=1, sticky="w")
label_library_number.grid(row=1, column=0, sticky="w")
entry_library_number.grid(row=1, column=1, sticky="we")

entry_library_number.bind("<KeyRelease>", update_totals_key)

# ------------------------------
# Totals Frame
# ------------------------------

frame_totals = tk.LabelFrame(window, text="Totals", padx=10, pady=10)
frame_totals.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

label_total_base = tk.Label(frame_totals, text="Membership Cost:")
label_total_extras = tk.Label(frame_totals, text="Extra Charges:")
label_total_annual = tk.Label(frame_totals, text="Annual Cost:")
label_total_discount = tk.Label(frame_totals, text="Total Discount:")
label_total_final = tk.Label(frame_totals, text="Total Cost:")
label_total_weekly = tk.Label(frame_totals, text="Weekly Cost:")

label_total_cost_base = tk.Label(frame_totals, text="--", width=50, anchor="w")
label_total_cost_extras = tk.Label(frame_totals, text="--", width=50, anchor="w")
label_total_cost_annual = tk.Label(frame_totals, text="--", width=50, anchor="w")
label_total_cost_discount = tk.Label(frame_totals, text="--", width=50, anchor="w")
label_total_cost_total = tk.Label(frame_totals, text="--", width=50, anchor="w")
label_total_cost_weekly = tk.Label(frame_totals, text="--", width=50, anchor="w")

label_total_base.grid(row=0, column=0, sticky="w")
label_total_cost_base.grid(row=0, column=1, sticky="e")

label_total_extras.grid(row=1, column=0, sticky="w")
label_total_cost_extras.grid(row=1, column=1, sticky="e")

label_total_annual.grid(row=2, column=0, sticky="w")
label_total_cost_annual.grid(row=2, column=1, sticky="e")

label_total_discount.grid(row=3, column=0, sticky="w")
label_total_cost_discount.grid(row=3, column=1, sticky="e")

label_total_final.grid(row=4, column=0, sticky="w")
label_total_cost_total.grid(row=4, column=1, sticky="e")

label_total_weekly.grid(row=5, column=0, sticky="w")
label_total_cost_weekly.grid(row=5, column=1, sticky="e")

# ------------------------------
# Buttons
# ------------------------------

button_calculate = Button(window, text="Calculate", command=calculate)
button_calculate.grid(row=18, column=0)

button_submit = Button(window, text="Submit", command=submit)
button_submit.grid(row=18, column=1)

button_reset = Button(window, text="Reset", command=reset_form)
button_reset.grid(row=19, column=0, pady=10)

# ------------------------------
# MAIN MENU 
# ------------------------------

def open_membership_form():
    window.deiconify()

def open_search_form():
    search_window = Toplevel()
    search_window.title("Search Members")
    Label(search_window, text="Search Form Coming Soon").pack(pady=20)
    Button(search_window, text="Back to Menu", command=open_main_menu).pack(pady=10)

def open_statistics_form():
    stats_window = Toplevel()
    stats_window.title("Statistics")
    Label(stats_window, text="Statistics Form Coming Soon").pack(pady=20)
    Button(stats_window, text="Back to Menu", command=open_main_menu).pack(pady=10)

def open_help_screen():
    help_window = Toplevel()
    help_window.title("Help")
    Label(help_window, text="Help Screen Coming Soon").pack(pady=20)
    Button(help_window, text="Back to Menu", command=open_main_menu).pack(pady=10)

def open_main_menu():
    menu_window = Toplevel()
    menu_window.title("Aurora Archive - Main Menu")
    menu_window.geometry("400x400")

    Label(menu_window, text="Main Menu", font=("Arial", 18, "bold")).pack(pady=20)

    Button(menu_window, text="Membership Form", width=25, command=open_membership_form).pack(pady=10)
    Button(menu_window, text="Search Members", width=25, command=open_search_form).pack(pady=10)
    Button(menu_window, text="Statistics", width=25, command=open_statistics_form).pack(pady=10)
    Button(menu_window, text="Help", width=25, command=open_help_screen).pack(pady=10)

    Button(menu_window, text="Exit", width=25, command=menu_window.destroy).pack(pady=20)

# ------------------------------
# Start Program
# ------------------------------

open_main_menu()
window.mainloop()