#-------------------------------#
#     BIT502 - Assessment 3     #
#         Thomas Bernard        #
#      Student ID 5142644       #
#-------------------------------#

# help_form.py
# This file contains the help screen for the application.



import tkinter as tk


def open_help_screen(window, clear_window):

    clear_window()
    window.geometry("550x500")

    # Title
    tk.Label(window, text="The Aurora Archive - Help",
             font=("Arial", 20, "bold")).pack(pady=20)

    # Help text
    help_text = (
        "Welcome to The Aurora Archive Membership System.\n\n"
        "This application allows staff to register new members, search for existing\n"
        "members, and view useful statistics about the membership database.\n\n"
        "---------------------------------------------\n"
        "MEMBERSHIP FORM\n"
        "---------------------------------------------\n"
        "- Enter the member's personal details.\n"
        "- Choose a membership plan and payment plan.\n"
        "- Select optional extras if required.\n"
        "- If the member has a library card, enter the 5‑digit card number.\n"
        "- Click 'Calculate' to update totals.\n"
        "- Click 'Submit' to save the member to the database.\n\n"
        "---------------------------------------------\n"
        "SEARCH MEMBERS\n"
        "---------------------------------------------\n"
        "- Search by ID, last name, membership plan, or payment plan.\n"
        "- You can combine multiple filters.\n"
        "- Partial last name searches are allowed.\n"
        "- Results will appear in the table below the search options.\n\n"
        "---------------------------------------------\n"
        "STATISTICS\n"
        "---------------------------------------------\n"
        "- View total members and counts for each membership plan.\n"
        "- See how many members selected each optional extra.\n"
        "- View monthly income estimates based on membership choices.\n\n"
        "---------------------------------------------\n"
        "NAVIGATION\n"
        "---------------------------------------------\n"
        "- Use the 'Back to Menu' button to return to the main screen.\n"
        "- The window close button (X) is disabled. Please exit via the menu.\n"
    )

    label = tk.Label(window, text=help_text, justify="left", anchor="w")
    label.pack(padx=20, pady=10, fill="both")

    # Back button
    tk.Button(window, text="Back to Menu",
              command=lambda: clear_window() or window.after(10, window.master.open_main_menu)
              ).pack(pady=20)