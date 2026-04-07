#-------------------------------#
#     BIT502 - Assessment 2     #
#         Thomas Bernard        #
#      Student ID 5142644       #
#-------------------------------#

import tkinter as tk

# ------------------------------
# Tkinter setup
# ------------------------------

window = tk.Tk()
window.title("The Aurora Archive")
window.geometry("300x630")


# ------------------------------
# Variables
# ------------------------------

plan_standard = "Standard"
plan_premium = "Premium"
plan_kids = "Kids"

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
# Functions
# ------------------------------

def calculate():
    # TODO: Build the calculation system, error checking and other tasks
    pass

def submit():
    # TODO: Finish the code for submission
    pass


# ------------------------------
# Widgets
# ------------------------------

# Labels
label_first_name = tk.Label(window, text="First Name:")
label_last_name = tk.Label(window, text="Last Name:")
label_address = tk.Label(window, text="Address:")
label_mobile = tk.Label(window, text="Mobile:")

label_membership_type = tk.Label(window, text="Membership Plan:")
label_membership_payment_plan = tk.Label(window, text="Payment Plan:")
label_library_card = tk.Label(window, text="Library Card:")
label_library_number = tk.Label(window, text="Card Number:")

label_optional_extras = tk.Label(window, text="Optional Extras:")

label_total_header = tk.Label(window, text="Totals", font=("Arial", 12, "bold"))
label_total_base = tk.Label(window, text="Membership Cost:")
label_total_extras = tk.Label(window, text="Extra Charges:")
label_total_annual = tk.Label(window, text="Annual Cost:")
label_total_discount = tk.Label(window, text="Total Discount:")
label_total_final = tk.Label(window, text="Total Cost:")

label_total_cost_base = tk.Label(window, text="--")
label_total_cost_extras = tk.Label(window, text="--")
label_total_cost_annual = tk.Label(window, text="--")
label_total_cost_discount = tk.Label(window, text="--")
label_total_cost_total = tk.Label(window, text="--")

# Entry fields
entry_first_name = tk.Entry(window)
entry_last_name = tk.Entry(window)
entry_address = tk.Entry(window)
entry_mobile = tk.Entry(window)
entry_library_number = tk.Entry(window)

# Radio buttons
radio_membership_1 = tk.Radiobutton(window, text=plan_standard, variable=membership_plan, value=plan_standard)
radio_membership_2 = tk.Radiobutton(window, text=plan_premium, variable=membership_plan, value=plan_premium)
radio_membership_3 = tk.Radiobutton(window, text=plan_kids, variable=membership_plan, value=plan_kids)

radio_payment_plan_1 = tk.Radiobutton(window, text=plan_monthly, variable=payment_plan, value=plan_monthly)
radio_payment_plan_2 = tk.Radiobutton(window, text=plan_annual, variable=payment_plan, value=plan_annual)

# Checkbuttons
checkbutton_has_library_card = tk.Checkbutton(window, variable=has_library_card)

checkbutton_extra1 = tk.Checkbutton(window, text=optional_1, variable=extra1)
checkbutton_extra2 = tk.Checkbutton(window, text=optional_2, variable=extra2)
checkbutton_extra3 = tk.Checkbutton(window, text=optional_3, variable=extra3)
checkbutton_extra4 = tk.Checkbutton(window, text=optional_4, variable=extra4)

# Buttons
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_submit = tk.Button(window, text="Submit", command=submit)


# ------------------------------
# Widget Positioning
# ------------------------------

label_first_name.grid(row=0, column=0, sticky="w", pady=2)
label_last_name.grid(row=1, column=0, sticky="w", pady=2)
label_address.grid(row=2, column=0, sticky="w", pady=2)
label_mobile.grid(row=3, column=0, sticky="w", pady=2)

entry_first_name.grid(row=0, column=1, sticky="w")
entry_last_name.grid(row=1, column=1, sticky="w")
entry_address.grid(row=2, column=1, sticky="w")
entry_mobile.grid(row=3, column=1, sticky="w")

label_membership_type.grid(row=4, column=0, sticky="w", pady=(10, 2))
radio_membership_1.grid(row=4, column=1, sticky="w")
radio_membership_2.grid(row=5, column=1, sticky="w")
radio_membership_3.grid(row=6, column=1, sticky="w")

label_membership_payment_plan.grid(row=7, column=0, sticky="w", pady=(10, 2))
radio_payment_plan_1.grid(row=7, column=1, sticky="w")
radio_payment_plan_2.grid(row=8, column=1, sticky="w")

label_optional_extras.grid(row=10, column=0, sticky="w", pady=(10, 2))
checkbutton_extra1.grid(row=10, column=1, sticky="w")
checkbutton_extra2.grid(row=11, column=1, sticky="w")
checkbutton_extra3.grid(row=12, column=1, sticky="w")
checkbutton_extra4.grid(row=13, column=1, sticky="w")

label_library_card.grid(row=14, column=0, sticky="w", pady=(10, 2))
checkbutton_has_library_card.grid(row=14, column=1, sticky="w")

label_library_number.grid(row=15, column=0, sticky="w")
entry_library_number.grid(row=15, column=1, sticky="w")

label_total_header.grid(row=19, column=0, sticky="w", pady=(20, 5))
label_total_base.grid(row=20, column=0, sticky="w")
label_total_extras.grid(row=21, column=0, sticky="w")
label_total_annual.grid(row=22, column=0, sticky="w")
label_total_discount.grid(row=23, column=0, sticky="w")
label_total_final.grid(row=24, column=0, sticky="w")

label_total_cost_base.grid(row=20, column=1, sticky="w")
label_total_cost_extras.grid(row=21, column=1, sticky="w")
label_total_cost_annual.grid(row=22, column=1, sticky="w")
label_total_cost_discount.grid(row=23, column=1, sticky="w")
label_total_cost_total.grid(row=24, column=1, sticky="w")

button_calculate.grid(row=25, column=0, pady=20)
button_submit.grid(row=25, column=1)


# ------------------------------
# Mainloop
# ------------------------------

window.mainloop()