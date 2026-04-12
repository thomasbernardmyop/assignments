#-------------------------------#
#     BIT502 - Assessment 3     #
#         Thomas Bernard        #
#      Student ID 5142644       #
#-------------------------------#

# statistics_form.py
# This file contains the statistics form for the application.

import tkinter as tk
from tkinter import ttk
from data.database import fetch_all


def open_statistics_form(window, clear_window):

    clear_window()
    window.geometry("650x650")

    tk.Label(window, text="Membership Statistics",
             font=("Arial", 20, "bold")).pack(pady=15)

    # ------------------------------
    # DATABASE QUERIES
    # ------------------------------

    # Total members
    total_members = fetch_all("SELECT COUNT(*) FROM Memberships")[0][0]

    # Membership plans
    count_standard = fetch_all("SELECT COUNT(*) FROM Memberships WHERE Membership_Plan='Standard - $10'")[0][0]
    count_premium = fetch_all("SELECT COUNT(*) FROM Memberships WHERE Membership_Plan='Premium - $15'")[0][0]
    count_kids = fetch_all("SELECT COUNT(*) FROM Memberships WHERE Membership_Plan='Kids - $5'")[0][0]

    # Payment plans
    count_monthly = fetch_all("SELECT COUNT(*) FROM Memberships WHERE Payment_Plan='Monthly'")[0][0]
    count_annual = fetch_all("SELECT COUNT(*) FROM Memberships WHERE Payment_Plan='Annual'")[0][0]

    # Optional extras
    count_book = fetch_all("SELECT COUNT(*) FROM Memberships WHERE Extra_Book_Rental=1")[0][0]
    count_private = fetch_all("SELECT COUNT(*) FROM Memberships WHERE Extra_Private_Area=1")[0][0]
    count_booklet = fetch_all("SELECT COUNT(*) FROM Memberships WHERE Extra_Booklet=1")[0][0]
    count_ebook = fetch_all("SELECT COUNT(*) FROM Memberships WHERE Extra_Ebook_Rental=1")[0][0]

    # Members with NO extras
    count_no_extras = fetch_all("""
        SELECT COUNT(*) FROM Memberships
        WHERE Extra_Book_Rental=0 AND Extra_Private_Area=0
        AND Extra_Booklet=0 AND Extra_Ebook_Rental=0
    """)[0][0]

    # Library card holders
    count_library_card = fetch_all("SELECT COUNT(*) FROM Memberships WHERE Has_Library_Card=1")[0][0]

    # ------------------------------
    # DISPLAY STATISTICS
    # ------------------------------

    stats_frame = tk.Frame(window)
    stats_frame.pack(pady=10)

    stats_text = (
        f"Total Members: {total_members}\n\n"
        f"Membership Plans:\n"
        f"  • Standard: {count_standard}\n"
        f"  • Premium: {count_premium}\n"
        f"  • Kids: {count_kids}\n\n"
        f"Payment Plans:\n"
        f"  • Monthly: {count_monthly}\n"
        f"  • Annual: {count_annual}\n\n"
        f"Optional Extras:\n"
        f"  • Book Rental: {count_book}\n"
        f"  • Private Area Access: {count_private}\n"
        f"  • Monthly Booklet: {count_booklet}\n"
        f"  • Online Ebook Rental: {count_ebook}\n\n"
        f"Members with NO Extras: {count_no_extras}\n\n"
        f"Members with Library Card: {count_library_card}"
    )

    tk.Label(stats_frame, text=stats_text, justify="left",
             anchor="w", font=("Arial", 11)).pack()

    # ------------------------------
    # INCOME TABLE
    # ------------------------------

    tk.Label(window, text="Estimated Monthly Income",
             font=("Arial", 16, "bold")).pack(pady=10)

    table_frame = tk.Frame(window)
    table_frame.pack(pady=5)

    columns = ("Option", "Cost Per Unit", "Member Amount", "Total Income")

    table = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)
    table.pack()

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=150)

    # Cost per unit (monthly)
    cost_standard = 10
    cost_premium = 15
    cost_kids = 5
    cost_book = 5
    cost_private = 15
    cost_booklet = 2
    cost_ebook = 5

    # Insert rows
    income_rows = [
        ("Standard Plan", cost_standard, count_standard, cost_standard * count_standard),
        ("Premium Plan", cost_premium, count_premium, cost_premium * count_premium),
        ("Kids Plan", cost_kids, count_kids, cost_kids * count_kids),
        ("Book Rental", cost_book, count_book, cost_book * count_book),
        ("Private Area Access", cost_private, count_private, cost_private * count_private),
        ("Monthly Booklet", cost_booklet, count_booklet, cost_booklet * count_booklet),
        ("Online eBook Rental", cost_ebook, count_ebook, cost_ebook * count_ebook),
    ]

    for row in income_rows:
        table.insert("", tk.END, values=row)

    # ------------------------------
    # BACK BUTTON
    # ------------------------------

    tk.Button(window, text="Back to Menu",
              command=lambda: clear_window() or window.after(10, window.master.open_main_menu)
              ).pack(pady=20)