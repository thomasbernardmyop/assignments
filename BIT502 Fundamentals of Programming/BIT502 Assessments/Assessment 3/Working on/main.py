#-------------------------------#
#     BIT502 - Assessment 3     #
#         Thomas Bernard        #
#      Student ID 5142644       #
#-------------------------------#

### Main.py
# This is the main entry point for the application. It sets up the main window and provides navigation to the different forms.


import tkinter as tk
from tkinter import messagebox

# Import each form from their respective files

from membership_form import open_membership_form
from search_form import open_search_form
from statistics_form import open_statistics_form
from help_form import open_help_screen


# ------------------------------
# Tkinter Setup
# ------------------------------

window = tk.Tk()
window.title("The Aurora Archive")

# Prevent closing via X button
def block_close():
    messagebox.showinfo("Exit Disabled", "Please exit via the menu of the program only.")

window.protocol("WM_DELETE_WINDOW", block_close)

# Minimum size
window.minsize(550, 500)


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
              command=lambda: open_membership_form(window, clear_window)).pack(pady=10)

    tk.Button(window, text="Search Members", width=25,
              command=lambda: open_search_form(window, clear_window)).pack(pady=10)

    tk.Button(window, text="Statistics", width=25,
              command=lambda: open_statistics_form(window, clear_window)).pack(pady=10)

    tk.Button(window, text="Help", width=25,
              command=lambda: open_help_screen(window, clear_window)).pack(pady=10)

    tk.Button(window, text="Exit", width=25, command=window.destroy).pack(pady=20)


# ------------------------------
# START PROGRAM
# ------------------------------

open_main_menu()
window.mainloop()
