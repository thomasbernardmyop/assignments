#-------------------------------#
#     BIT502 - Assessment 2     #
#         Thomas Bernard        #
#      Student ID 5142644       #
#-------------------------------#

# ------------------------------
# Imports
# ------------------------------

import tkinter


# ------------------------------
# Tkinter setup
# ------------------------------

window = tkinter.Tk()
window.title("The Aurora Archive")


# ------------------------------
# Variables
# ------------------------------

# Store text in the variables so we can change it later if we need to

plan_standard = "Standard"
plan_premium = "Premium"
plan_kids = "Kids"

plan_monthly = "Monthly"
plan_annual = "Annual"

optional_1 = "Book Rental"
optional_2 = "Private Area Access"
optional_3 = "Monthly Booklet"
optional_4 = "Online ebook Rental"

# Variables that store the results of the elements


membership_plan = tkinter.StringVar(window, plan_standard)      # Selected membership type
payment_plan = tkinter.StringVar(window, plan_monthly)          # Duration of payment
extra1 = tkinter.BooleanVar(window, False)                      # Optional extra 1
extra2 = tkinter.BooleanVar(window, False)                      # Optional extra 2
extra3 = tkinter.BooleanVar(window, False)                      # Optional extra 3
extra4 = tkinter.BooleanVar(window, False)                      # Optional extra 4
has_library_card = tkinter.BooleanVar(window, False)            # Library Card




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
# Widget definitions
# ------------------------------
# The widget definitions are found in this section, no positioning has been done here, just declaration


#### Labels ####

label_first_name = tkinter.Label(window, text = "First Name:")
label_last_name = tkinter.Label(window, text = "Last Name:")
label_address = tkinter.Label(window, text = "Address:")
label_mobile = tkinter.Label(window, text = "Mobile:")

label_membership_type = tkinter.Label(window, text = "Membership Plan:")
label_membership_payment_plan = tkinter.Label(window, text = "Payment Plan:")
label_library_card = tkinter.Label(window, text = "Library Card:")
label_library_number = tkinter.Label(window, text = "Card Number:")

label_optional_extras = tkinter.Label(window, text = "Optional Extras:")

label_total_header = tkinter.Label(window, text = "Totals")
label_total_base = tkinter.Label(window, text = "Membership Cost:")
label_total_extras = tkinter.Label(window, text = "Extra Charges:")
label_total_annual = tkinter.Label(window, text = "Annual Cost:")
label_total_discount = tkinter.Label(window, text = "Total Discount:")
label_total_final = tkinter.Label(window, text = "Total Cost:")


label_total_cost_base = tkinter.Label(window, text = "--")
label_total_cost_extras = tkinter.Label(window, text = "--")
label_total_cost_annual = tkinter.Label(window, text = "--")
label_total_cost_discount = tkinter.Label(window, text = "--")
label_total_cost_total = tkinter.Label(window, text = "--")


#### Entry text boxes ####

entry_first_name = tkinter.Entry(window)
entry_last_name = tkinter.Entry(window)
entry_address = tkinter.Entry(window)
entry_mobile = tkinter.Entry(window)

entry_library_number = tkinter.Entry(window)

#### Radio buttons ####

radio_membership_1 = tkinter.Radiobutton(window, text = plan_standard, variable = membership_plan, value = plan_standard)
radio_membership_2 = tkinter.Radiobutton(window, text = plan_premium, variable = membership_plan, value = plan_premium)
radio_membership_3 = tkinter.Radiobutton(window, text = plan_kids, variable = membership_plan, value = plan_kids)

radio_payment_plan_1 = tkinter.Radiobutton(window, text = plan_monthly, variable = payment_plan, value = plan_monthly)
radio_payment_plan_2 = tkinter.Radiobutton(window, text = plan_annual, variable = payment_plan, value = plan_annual)

#### Checkbuttons ####

checkbutton_has_library_card = tkinter.Checkbutton(window, text = "", variable = has_library_card, onvalue = True, offvalue = False)

checkbutton_extra1 = tkinter.Checkbutton(window, text = optional_1, variable = extra1, onvalue = True, offvalue = False)
checkbutton_extra2 = tkinter.Checkbutton(window, text = optional_2, variable = extra2, onvalue = True, offvalue = False)
checkbutton_extra3 = tkinter.Checkbutton(window, text = optional_3, variable = extra3, onvalue = True, offvalue = False)
checkbutton_extra4 = tkinter.Checkbutton(window, text = optional_4, variable = extra4, onvalue = True, offvalue = False)


#### Buttons ####

button_calculate = tkinter.Button(window, text = "Calculate", command = calculate)
button_submit = tkinter.Button(window, text = "Submit", command = submit)


# ------------------------------
# Widget positioning
# ------------------------------
# All of the widget positioning is found here
# Another method of positioning widgets can be used if you comment this code out and use your own design

label_first_name.grid(row = 0, column = 0, sticky = "w")
label_last_name.grid(row = 1, column = 0, sticky = "w")
label_address.grid(row = 2, column = 0, sticky = "w")
label_mobile.grid(row = 3, column = 0, sticky = "w")

label_membership_type.grid(row = 4, column = 0, sticky = "w")
label_membership_payment_plan.grid(row = 7, column = 0, sticky = "w")
label_library_card.grid(row = 14, column = 0, sticky = "w")

entry_first_name.grid(row = 0, column = 1, sticky = "w")
entry_last_name.grid(row = 1, column = 1, sticky = "w")
entry_address.grid(row = 2, column = 1, sticky = "w")
entry_mobile.grid(row = 3, column = 1, sticky = "w")

radio_membership_1.grid(row = 4, column = 1, sticky = "w")
radio_membership_2.grid(row = 5, column = 1, sticky = "w")
radio_membership_3.grid(row = 6, column = 1, sticky = "w")

radio_payment_plan_1.grid(row = 7, column = 1, sticky = "w")
radio_payment_plan_2.grid(row = 8, column = 1, sticky = "w")

label_optional_extras.grid(row = 10, column = 0, sticky = "w")
checkbutton_extra1.grid(row = 10, column = 1, sticky = "w")
checkbutton_extra2.grid(row = 11, column = 1, sticky = "w")
checkbutton_extra3.grid(row = 12, column = 1, sticky = "w")
checkbutton_extra4.grid(row = 13, column = 1, sticky = "w")

label_library_number.grid(row = 15, column = 0, sticky = "w")
checkbutton_has_library_card.grid(row = 14, column = 1, sticky = "w")
entry_library_number.grid(row = 15, column = 1, sticky = "w")

label_total_header.grid(row = 19, column = 0, sticky = "w")
label_total_base.grid(row = 20, column = 0, sticky = "w")
label_total_extras.grid(row = 21, column = 0, sticky = "w")
label_total_annual.grid(row = 22, column = 0, sticky = "w")
label_total_discount.grid(row = 23, column = 0, sticky = "w")
label_total_final.grid(row = 24, column = 0, sticky = "w")

label_total_cost_base.grid(row = 20, column = 1, sticky = "w")
label_total_cost_extras.grid(row = 21, column = 1, sticky = "w")
label_total_cost_annual.grid(row = 22, column = 1, sticky = "w")
label_total_cost_discount.grid(row = 23, column = 1, sticky = "w")
label_total_cost_total.grid(row = 24, column = 1, sticky = "w")

button_calculate.grid(row = 25, column = 0)
button_submit.grid(row = 25, column = 1)

# ----------------------------------
# Tkinter mainloop
window.mainloop()