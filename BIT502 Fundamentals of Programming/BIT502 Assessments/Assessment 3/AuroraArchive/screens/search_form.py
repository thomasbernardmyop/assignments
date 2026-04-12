#-------------------------------#
#     BIT502 - Assessment 3     #
#         Thomas Bernard        #
#      Student ID 5142644       #
#-------------------------------#

# search_form.py
# This file contains the search form for the application.

import tkinter as tk
from tkinter import ttk, messagebox
from data.database import fetch_all


def open_search_form(window, clear_window):

    clear_window()
    window.geometry("650x550")

    # ------------------------------
    # Search Variables
    # ------------------------------

    var_id = tk.StringVar()
    var_last = tk.StringVar()
    var_plan = tk.StringVar(value="Any")
    var_payment = tk.StringVar(value="Any")

    # ------------------------------
    # RUN SEARCH
    # ------------------------------

    def run_search():
        query = "SELECT * FROM Memberships WHERE 1=1"
        params = []

        # ID search
        if var_id.get().strip() != "":
            if not var_id.get().isdigit():
                messagebox.showwarning("Invalid ID", "ID must be a number.")
                return
            query += " AND ID = ?"
            params.append(var_id.get())

        # Last name search (partial, case-insensitive)
        if var_last.get().strip() != "":
            query += " AND LOWER(Last_Name) LIKE ?"
            params.append("%" + var_last.get().lower() + "%")

        # Membership plan
        if var_plan.get() != "Any":
            query += " AND Membership_Plan = ?"
            params.append(var_plan.get())

        # Payment plan
        if var_payment.get() != "Any":
            query += " AND Payment_Plan = ?"
            params.append(var_payment.get())

        results = fetch_all(query, params)

        # Clear table
        for row in table.get_children():
            table.delete(row)

        if not results:
            messagebox.showinfo("No Results", "No members found matching your criteria.")
            return

        # Insert results
        for row in results:
            table.insert("", tk.END, values=row)

    # ------------------------------
    # UI LAYOUT
    # ------------------------------

    tk.Label(window, text="Search Members", font=("Arial", 18, "bold")).pack(pady=10)

    frame = tk.Frame(window)
    frame.pack(pady=10)

    # ID
    tk.Label(frame, text="Search by ID:").grid(row=0, column=0, sticky="w")
    tk.Entry(frame, textvariable=var_id).grid(row=0, column=1, padx=5)

    # Last Name
    tk.Label(frame, text="Search by Last Name:").grid(row=1, column=0, sticky="w")
    tk.Entry(frame, textvariable=var_last).grid(row=1, column=1, padx=5)

    # Membership Plan
    tk.Label(frame, text="Membership Plan:").grid(row=2, column=0, sticky="w")
    ttk.Combobox(frame, textvariable=var_plan, values=[
        "Any", "Standard - $10", "Premium - $15", "Kids - $5"
    ], state="readonly").grid(row=2, column=1, padx=5)

    # Payment Plan
    tk.Label(frame, text="Payment Plan:").grid(row=3, column=0, sticky="w")
    ttk.Combobox(frame, textvariable=var_payment, values=[
        "Any", "Monthly", "Annual"
    ], state="readonly").grid(row=3, column=1, padx=5)

    # Search Button
    tk.Button(window, text="Search", width=20, command=run_search).pack(pady=10)

    # Results Table
    columns = (
        "ID", "First", "Last", "Address", "Mobile",
        "Plan", "Payment", "Book", "Private", "Booklet",
        "Ebook", "HasCard", "CardNum"
    )

    table = ttk.Treeview(window, columns=columns, show="headings", height=12)
    table.pack(fill="both", expand=True, padx=10)

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100)

    # Back Button
    tk.Button(window, text="Back to Menu",
              command=lambda: clear_window() or window.after(10, window.master.open_main_menu)
              ).pack(pady=10)