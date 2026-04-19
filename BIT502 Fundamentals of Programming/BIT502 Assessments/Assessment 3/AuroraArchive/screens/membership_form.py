#-------------------------------#
#     BIT502 - Assessment 3     #
#         Thomas Bernard        #
#      Student ID 5142644       #
#-------------------------------#

import tkinter as tk
from tkinter import messagebox
from data.database import insert_member


# ------------------------------
# Validation Helpers
# ------------------------------

def only_letters(value):
    return all(c.isalpha() or c == " " for c in value) or value == ""

def only_numbers(value):
    return value.isdigit() or value == ""

def only_five_digits(value):
    return (value.isdigit() and len(value) <= 5) or value == ""


# ------------------------------
# MEMBERSHIP FORM
# ------------------------------

def open_membership_form(window, clear_window, open_main_menu):

    clear_window()
    window.geometry("550x700")

    # Tkinter variables
    membership_plan = tk.StringVar(value="Standard - $10")
    payment_plan = tk.StringVar(value="Monthly")

    extra1 = tk.BooleanVar(value=False)
    extra2 = tk.BooleanVar(value=False)
    extra3 = tk.BooleanVar(value=False)
    extra4 = tk.BooleanVar(value=False)

    has_library_card = tk.BooleanVar(value=False)

    # ------------------------------
    # CALCULATE FUNCTION
    # ------------------------------

    def calculate():
        # Reset colours
        for entry in [entry_first, entry_last, entry_address, entry_mobile, entry_card]:
            entry.config(bg="white")

        # Validate
        errors = False

        if entry_first.get().strip() == "":
            entry_first.config(bg="misty rose")
            errors = True

        if entry_last.get().strip() == "":
            entry_last.config(bg="misty rose")
            errors = True

        if entry_address.get().strip() == "":
            entry_address.config(bg="misty rose")
            errors = True

        mobile = entry_mobile.get().strip()
        if mobile == "" or not mobile.isdigit():
            entry_mobile.config(bg="misty rose")
            errors = True

        if has_library_card.get():
            card = entry_card.get().strip()
            if not (card.isdigit() and len(card) == 5):
                entry_card.config(bg="misty rose")
                errors = True

        # Base membership cost
        plan = membership_plan.get()
        if plan == "Standard - $10":
            base = 10
        elif plan == "Premium - $15":
            base = 15
        else:
            base = 5

        # Extras
        extras = 0
        if extra1.get(): extras += 5
        if extra2.get(): extras += 15
        if extra3.get(): extras += 2
        if extra4.get(): extras += 5

        # Monthly vs Annual
        if payment_plan.get() == "Monthly":
            membership_cost = base
            extras_cost = extras
        else:
            membership_cost = base * 11
            extras_cost = extras * 12

        # Discount
        discount = 0
        if has_library_card.get() and entry_card.get().isdigit() and len(entry_card.get()) == 5:
            discount = (membership_cost + extras_cost) * 0.10

        total = membership_cost + extras_cost - discount

        # Weekly cost
        if payment_plan.get() == "Monthly":
            weekly = total / 4
        else:
            weekly = total / 52

        # Update labels
        lbl_base.config(text=f"${membership_cost:.2f}")
        lbl_extras.config(text=f"${extras_cost:.2f}")
        lbl_discount.config(text=f"${discount:.2f}")
        lbl_total.config(text=f"${total:.2f}")
        lbl_weekly.config(text=f"${weekly:.2f}")

   

    def update_totals_key(event):
        calculate()

    def update_totals(*args):
        calculate()

    # ------------------------------
    # RESET FUNCTION
    # ------------------------------

    def reset_form():
        entry_first.delete(0, tk.END)
        entry_last.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_mobile.delete(0, tk.END)
        entry_card.delete(0, tk.END)

        membership_plan.set("Standard - $10")
        payment_plan.set("Monthly")

        extra1.set(False)
        extra2.set(False)
        extra3.set(False)
        extra4.set(False)

        has_library_card.set(False)

        lbl_base.config(text="--")
        lbl_extras.config(text="--")
        lbl_discount.config(text="--")
        lbl_total.config(text="--")
        lbl_weekly.config(text="--")


    # ------------------------------
    # SUBMIT FUNCTION
    # ------------------------------

    def submit():
        first = entry_first.get().strip()
        last = entry_last.get().strip()
        address = entry_address.get().strip()
        mobile = entry_mobile.get().strip()
        card = entry_card.get().strip()

        # Reset colours
        for entry in [entry_first, entry_last, entry_address, entry_mobile, entry_card]:
            entry.config(bg="white")

        errors = False
        missing = []

        if first == "":
            entry_first.config(bg="red")
            missing.append("First Name")
            errors = True

        if last == "":
            entry_last.config(bg="red")
            missing.append("Last Name")
            errors = True

        if address == "":
            entry_address.config(bg="red")
            missing.append("Address")
            errors = True

        if mobile == "" or not mobile.isdigit():
            entry_mobile.config(bg="red")
            missing.append("Mobile")
            errors = True

        if has_library_card.get():
            if not (card.isdigit() and len(card) == 5):
                entry_card.config(bg="red")
                missing.append("Library Card Number")
                errors = True

        if errors:
            messagebox.showwarning("Error", "Invalid or missing fields:\n" + "\n".join(missing))
            return

        # Insert into DB
        insert_member((
            first, last, address, mobile,
            membership_plan.get(), payment_plan.get(),
            int(extra1.get()), int(extra2.get()), int(extra3.get()), int(extra4.get()),
            int(has_library_card.get()), card if has_library_card.get() else ""
        ))

        messagebox.showinfo("Success", "Membership submitted!")
        reset_form()


    # ------------------------------
    # UI LAYOUT
    # ------------------------------

    # Personal Details
    frame_personal = tk.LabelFrame(window, text="Personal Details", padx=10, pady=10)
    frame_personal.grid(row=0, column=0, padx=10, pady=5, sticky="nw")
    frame_personal.grid_columnconfigure(1, weight=1)

    v_letters = (window.register(only_letters), "%P")
    v_numbers = (window.register(only_numbers), "%P")
    v_card = (window.register(only_five_digits), "%P")

    tk.Label(frame_personal, text="First Name:*").grid(row=0, column=0, sticky="w")
    entry_first = tk.Entry(frame_personal, validate="key", validatecommand=v_letters)
    entry_first.grid(row=0, column=1, sticky="we")
    entry_first.bind("<KeyRelease>", update_totals_key)

    tk.Label(frame_personal, text="Last Name:*").grid(row=1, column=0, sticky="w")
    entry_last = tk.Entry(frame_personal, validate="key", validatecommand=v_letters)
    entry_last.grid(row=1, column=1, sticky="we")
    entry_last.bind("<KeyRelease>", update_totals_key)

    tk.Label(frame_personal, text="Address:*").grid(row=2, column=0, sticky="w")
    entry_address = tk.Entry(frame_personal)
    entry_address.grid(row=2, column=1, sticky="we")
    entry_address.bind("<KeyRelease>", update_totals_key)

    tk.Label(frame_personal, text="Mobile:*").grid(row=3, column=0, sticky="w")
    entry_mobile = tk.Entry(frame_personal, validate="key", validatecommand=v_numbers)
    entry_mobile.grid(row=3, column=1, sticky="we")
    entry_mobile.bind("<KeyRelease>", update_totals_key)

    # Membership Plan
    frame_membership = tk.LabelFrame(window, text="Membership Plan", padx=10, pady=10)
    frame_membership.grid(row=1, column=0, padx=10, pady=5, sticky="nw")

    tk.Radiobutton(frame_membership, text="Standard - $10", variable=membership_plan,
                   value="Standard - $10").grid(row=0, column=0, sticky="w")
    tk.Radiobutton(frame_membership, text="Premium - $15", variable=membership_plan,
                   value="Premium - $15").grid(row=1, column=0, sticky="w")
    tk.Radiobutton(frame_membership, text="Kids - $5", variable=membership_plan,
                   value="Kids - $5").grid(row=2, column=0, sticky="w")

    # Optional Extras
    frame_extras = tk.LabelFrame(window, text="Optional Extras", padx=10, pady=10)
    frame_extras.grid(row=2, column=0, padx=10, pady=5, sticky="nw")

    tk.Checkbutton(frame_extras, text="Book Rental", variable=extra1).grid(row=0, column=0, sticky="w")
    tk.Checkbutton(frame_extras, text="Private Area Access", variable=extra2).grid(row=1, column=0, sticky="w")
    tk.Checkbutton(frame_extras, text="Monthly Booklet", variable=extra3).grid(row=2, column=0, sticky="w")
    tk.Checkbutton(frame_extras, text="Online Ebook Rental", variable=extra4).grid(row=3, column=0, sticky="w")

    # Payment Plan
    frame_payment = tk.LabelFrame(window, text="Payment Plan", padx=10, pady=10)
    frame_payment.grid(row=0, column=1, padx=10, pady=5, sticky="ne")

    tk.Radiobutton(frame_payment, text="Monthly", variable=payment_plan,
                   value="Monthly").grid(row=0, column=0, sticky="w")
    tk.Radiobutton(frame_payment, text="Annual", variable=payment_plan,
                   value="Annual").grid(row=1, column=0, sticky="w")

    # Library Card
    frame_library = tk.LabelFrame(window, text="Library Card", padx=10, pady=10)
    frame_library.grid(row=1, column=1, padx=10, pady=5, sticky="ne")
    frame_library.grid_columnconfigure(1, weight=1)

    tk.Checkbutton(frame_library, text="Has Library Card",
                   variable=has_library_card).grid(row=0, column=0, sticky="w")

    tk.Label(frame_library, text="Card Number:").grid(row=1, column=0, sticky="w")
    entry_card = tk.Entry(frame_library, validate="key", validatecommand=v_card)
    entry_card.grid(row=1, column=1, sticky="we")
    entry_card.bind("<KeyRelease>", update_totals_key)

    # Bind auto‑update to variables
    membership_plan.trace_add("write", update_totals)
    payment_plan.trace_add("write", update_totals)
    extra1.trace_add("write", update_totals)
    extra2.trace_add("write", update_totals)
    extra3.trace_add("write", update_totals)
    extra4.trace_add("write", update_totals)
    has_library_card.trace_add("write", update_totals)

    # Totals
    frame_totals = tk.LabelFrame(window, text="Totals", padx=10, pady=10)
    frame_totals.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")
    frame_totals.grid_columnconfigure(1, weight=1)

    tk.Label(frame_totals, text="Membership Cost:").grid(row=0, column=0, sticky="w")
    lbl_base = tk.Label(frame_totals, text="--")
    lbl_base.grid(row=0, column=1, sticky="e")

    tk.Label(frame_totals, text="Extras Cost:").grid(row=1, column=0, sticky="w")
    lbl_extras = tk.Label(frame_totals, text="--")
    lbl_extras.grid(row=1, column=1, sticky="e")

    tk.Label(frame_totals, text="Discount:").grid(row=2, column=0, sticky="w")
    lbl_discount = tk.Label(frame_totals, text="--")
    lbl_discount.grid(row=2, column=1, sticky="e")

    tk.Label(frame_totals, text="Total Cost:").grid(row=3, column=0, sticky="w")
    lbl_total = tk.Label(frame_totals, text="--")
    lbl_total.grid(row=3, column=1, sticky="e")

    tk.Label(frame_totals, text="Weekly Cost:").grid(row=4, column=0, sticky="w")
    lbl_weekly = tk.Label(frame_totals, text="--")
    lbl_weekly.grid(row=4, column=1, sticky="e")

    # Buttons
    tk.Button(window, text="Calculate", command=calculate).grid(row=4, column=0, pady=10)
    tk.Button(window, text="Submit", command=submit).grid(row=4, column=1, pady=10)
    tk.Button(window, text="Reset", command=reset_form).grid(row=5, column=0, pady=10)

    # Back Button
    tk.Button(
        window,
        text="Back to Menu",
        command=lambda: (clear_window(), open_main_menu())
    ).grid(row=5, column=1, pady=10)
