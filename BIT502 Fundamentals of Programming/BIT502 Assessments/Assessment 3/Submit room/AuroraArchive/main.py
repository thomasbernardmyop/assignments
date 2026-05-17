#-------------------------------#
#     BIT502 - Assessment 3     #
#         Thomas Bernard        #
#      Student ID 5142644       #
#-------------------------------#

# Main.py

import tkinter as tk
from tkinter import messagebox

# Import screens(forms)
from screens.membership_form import open_membership_form
from screens.search_form import open_search_form
from screens.statistics_form import open_statistics_form
from screens.help_form import open_help_screen


# ------------------------------
# Tkinter Setup
# ------------------------------

window = tk.Tk()
window.title("The Aurora Archive")
window.minsize(550, 500)

# Disable closing via X
def block_close():
    messagebox.showinfo("Exit Disabled", "Please exit via the menu of the program only.")

window.protocol("WM_DELETE_WINDOW", block_close)


# ------------------------------
# Clear Window
# ------------------------------

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()


# ------------------------------
# MAIN MENU
# ------------------------------

def open_main_menu():
    clear_window()
    window.geometry("550x500")

    tk.Label(window, text="Main Menu", font=("Arial", 20, "bold")).pack(pady=20)

    tk.Button(window, text="Membership Form", width=25,
              command=lambda: open_membership_form(window, clear_window, open_main_menu)).pack(pady=10)

    tk.Button(window, text="Search Members", width=25,
              command=lambda: open_search_form(window, clear_window, open_main_menu)).pack(pady=10)

    tk.Button(window, text="Statistics", width=25,
              command=lambda: open_statistics_form(window, clear_window, open_main_menu)).pack(pady=10)

    tk.Button(window, text="Help", width=25,
              command=lambda: open_help_screen(window, clear_window, open_main_menu)).pack(pady=10)

    tk.Button(window, text="Exit", width=25, command=window.destroy).pack(pady=20)


# ------------------------------
# START PROGRAM
# ------------------------------

open_main_menu()
window.mainloop()
