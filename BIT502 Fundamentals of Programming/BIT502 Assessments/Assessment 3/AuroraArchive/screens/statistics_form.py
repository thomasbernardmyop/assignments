#-------------------------------#
#     BIT502 - Assessment 3     #
#         Thomas Bernard        #
#      Student ID 5142644       #
#-------------------------------#

# statistics_form.py
# This file contains the statistics screen for the application.

import tkinter as tk
from tkinter import ttk
from data.database import fetch_all


def open_statistics_form(window, clear_window, open_main_menu):

    clear_window()
    window.geometry("1200x800")   # Wider window for stats table

    tk.Label(window, text="Membership Statistics",
             font=("Arial", 20, "bold")).pack(pady=20)

    # ----------------------------------------------------
    # FETCH ALL MEMBERS
    # ----------------------------------------------------
    members = fetch_all("SELECT * FROM Memberships")

    # ----------------------------------------------------
    # CALCULATE STATISTICS
    # ----------------------------------------------------
    total_members = len(members)

    plan_counts = {
        "Standard - $10": 0,
        "Premium - $15": 0,
        "Kids - $5": 0
    }

    extras_counts = {
        "Book Rental": 0,
        "Private Area": 0,
        "Booklet": 0,
        "Ebook Rental": 0
    }

    monthly_income = 0

    for m in members:
        # m = (MemberID, First, Last, Address, Mobile, Plan, Payment, Book, Private, Booklet, Ebook, HasCard, CardNum)

        plan = m[5]
        payment = m[6]

        # Count plans
        if plan in plan_counts:
            plan_counts[plan] += 1

        # Count extras
        if m[7] == 1: extras_counts["Book Rental"] += 1
        if m[8] == 1: extras_counts["Private Area"] += 1
        if m[9] == 1: extras_counts["Booklet"] += 1
        if m[10] == 1: extras_counts["Ebook Rental"] += 1

        # Estimate monthly income
        base_cost = {
            "Standard - $10": 10,
            "Premium - $15": 15,
            "Kids - $5": 5
        }.get(plan, 0)

        extras_cost = (m[7] * 5) + (m[8] * 15) + (m[9] * 2) + (m[10] * 5)

        if payment == "Monthly":
            monthly_income += base_cost + extras_cost
        else:
            monthly_income += (base_cost * 11 + extras_cost * 12) / 12

    # ----------------------------------------------------
    # DISPLAY STATISTICS
    # ----------------------------------------------------
    stats_frame = tk.Frame(window)
    stats_frame.pack(pady=10)

    tk.Label(stats_frame, text=f"Total Members: {total_members}",
             font=("Arial", 14)).grid(row=0, column=0, sticky="w", pady=5)

    tk.Label(stats_frame, text="Membership Plan Counts:",
             font=("Arial", 14, "bold")).grid(row=1, column=0, sticky="w", pady=5)

    row = 2
    for plan, count in plan_counts.items():
        tk.Label(stats_frame, text=f"{plan}: {count}",
                 font=("Arial", 12)).grid(row=row, column=0, sticky="w")
        row += 1

    tk.Label(stats_frame, text="Optional Extras Selected:",
             font=("Arial", 14, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    row += 1

    for extra, count in extras_counts.items():
        tk.Label(stats_frame, text=f"{extra}: {count}",
                 font=("Arial", 12)).grid(row=row, column=0, sticky="w")
        row += 1

    tk.Label(stats_frame, text=f"Estimated Monthly Income: ${monthly_income:.2f}",
             font=("Arial", 14, "bold")).grid(row=row, column=0, sticky="w", pady=10)

    # ----------------------------------------------------
    # TABLE OF ALL MEMBERS (WITH SCROLLBAR)
    # ----------------------------------------------------
    columns = (
        "MemberID", "First", "Last", "Address", "Mobile",
        "Plan", "Payment", "Book", "Private", "Booklet",
        "Ebook", "HasCard", "CardNum"
    )

    table = ttk.Treeview(window, columns=columns, show="headings", height=10)
    table.pack(fill="both", expand=True, padx=10)

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=120)

    # Insert rows
    for row_data in members:
        table.insert("", tk.END, values=row_data)

    # Horizontal scrollbar
    scroll_x = tk.Scrollbar(window, orient="horizontal", command=table.xview)
    table.configure(xscrollcommand=scroll_x.set)
    scroll_x.pack(fill="x")

    # ----------------------------------------------------
    # BACK BUTTON
    # ----------------------------------------------------
    tk.Button(
        window,
        text="Back to Menu",
        command=lambda: (clear_window(), open_main_menu())
    ).pack(pady=20)

