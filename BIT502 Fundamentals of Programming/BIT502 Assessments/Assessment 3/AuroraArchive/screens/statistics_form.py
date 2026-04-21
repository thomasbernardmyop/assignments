#-------------------------------#
#     BIT502 - Assessment 3     #
#         Thomas Bernard        #
#      Student ID 5142644       #
#-------------------------------#

# statistics_form.py

import tkinter as tk
from tkinter import ttk
from data.database import fetch_all


def open_statistics_form(window, clear_window, open_main_menu):

    clear_window()

    # ----------------------------------------------------
    # MAKE ONLY THIS SCREEN FULL SCREEN
    # ----------------------------------------------------
    window.state("zoomed")   # Maximized window

    # ----------------------------------------------------
    # SCROLLABLE WINDOW SETUP (SAFE + STABLE)
    # ----------------------------------------------------
    outer_frame = tk.Frame(window)
    outer_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(outer_frame)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar_y = tk.Scrollbar(outer_frame, orient="vertical", command=canvas.yview)
    scrollbar_y.pack(side="right", fill="y")

    scrollable_frame = tk.Frame(canvas)

    # Update scroll region
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Make scrollable frame match canvas width
    def resize_canvas(event):
        canvas.itemconfig(canvas_window, width=event.width)

    canvas.bind("<Configure>", resize_canvas)
    canvas.configure(yscrollcommand=scrollbar_y.set)

    # ----------------------------------------------------
    # ENABLE MOUSE WHEEL SCROLLING
    # ----------------------------------------------------
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # ----------------------------------------------------
    # TITLE
    # ----------------------------------------------------
    tk.Label(scrollable_frame, text="Membership Statistics",
             font=("Arial", 26, "bold")).pack(pady=20)

    # ----------------------------------------------------
    # FETCH MEMBERS
    # ----------------------------------------------------
    members = fetch_all("SELECT * FROM Memberships")

    # ----------------------------------------------------
    # CALCULATE STATISTICS
    # ----------------------------------------------------
    total_members = len(members)

    plan_counts = {"Standard - $10": 0, "Premium - $15": 0, "Kids - $5": 0}
    extras_counts = {"Book Rental": 0, "Private Area": 0, "Booklet": 0, "Ebook Rental": 0}

    monthly_income = 0

    for m in members:
        plan = m[5]
        payment = m[6]

        if plan in plan_counts:
            plan_counts[plan] += 1

        if m[7] == 1: extras_counts["Book Rental"] += 1
        if m[8] == 1: extras_counts["Private Area"] += 1
        if m[9] == 1: extras_counts["Booklet"] += 1
        if m[10] == 1: extras_counts["Ebook Rental"] += 1

        base_cost = {"Standard - $10": 10, "Premium - $15": 15, "Kids - $5": 5}.get(plan, 0)
        extras_cost = (m[7] * 5) + (m[8] * 15) + (m[9] * 2) + (m[10] * 5)

        if payment == "Monthly":
            monthly_income += base_cost + extras_cost
        else:
            monthly_income += (base_cost * 11 + extras_cost * 12) / 12

    # ----------------------------------------------------
    # SUMMARY BOX
    # ----------------------------------------------------
    stats_box = tk.LabelFrame(scrollable_frame, text="Summary Statistics",
                              padx=10, pady=10, font=("Arial", 16, "bold"))
    stats_box.pack(pady=10, fill="x")

    row = 0
    tk.Label(stats_box, text=f"Total Members: {total_members}",
             font=("Arial", 14)).grid(row=row, column=0, sticky="w")
    row += 1

    tk.Label(stats_box, text="Membership Plans:",
             font=("Arial", 14, "bold")).grid(row=row, column=0, sticky="w", pady=(10, 0))
    row += 1

    for plan, count in plan_counts.items():
        tk.Label(stats_box, text=f"{plan}: {count}",
                 font=("Arial", 12)).grid(row=row, column=0, sticky="w")
        row += 1

    tk.Label(stats_box, text="Optional Extras:",
             font=("Arial", 14, "bold")).grid(row=row, column=0, sticky="w", pady=(10, 0))
    row += 1

    for extra, count in extras_counts.items():
        tk.Label(stats_box, text=f"{extra}: {count}",
                 font=("Arial", 12)).grid(row=row, column=0, sticky="w")
        row += 1

    tk.Label(stats_box, text=f"Estimated Monthly Income: ${monthly_income:.2f}",
             font=("Arial", 16, "bold")).grid(row=row, column=0, sticky="w", pady=10)

    # ----------------------------------------------------
    # EXPECTED MONTHLY INCOME TABLE
    # ----------------------------------------------------
    tk.Label(scrollable_frame, text="Expected Monthly Income (No Discounts Applied)",
             font=("Arial", 20, "bold")).pack(pady=10)

    income_columns = ("Option", "Cost Per Unit", "Member Amount", "Total Income")

    income_table = ttk.Treeview(scrollable_frame, columns=income_columns, show="headings", height=8)
    income_table.pack(fill="x", padx=10)

    for col in income_columns:
        income_table.heading(col, text=col)
        income_table.column(col, width=200)

    income_data = [
        ("Standard Plan", 10, plan_counts["Standard - $10"]),
        ("Premium Plan", 15, plan_counts["Premium - $15"]),
        ("Kids Plan", 5, plan_counts["Kids - $5"]),
        ("Book Rental", 5, extras_counts["Book Rental"]),
        ("Private Area Access", 15, extras_counts["Private Area"]),
        ("Monthly Booklet", 2, extras_counts["Booklet"]),
        ("Online eBook Rental", 5, extras_counts["Ebook Rental"])
    ]

    for option, cost, amount in income_data:
        total_income = cost * amount
        income_table.insert("", tk.END, values=(option, f"${cost}", amount, f"${total_income}"))

    # ----------------------------------------------------
    # FULL MEMBER LIST TABLE
    # ----------------------------------------------------
    tk.Label(scrollable_frame, text="All Members",
             font=("Arial", 20, "bold")).pack(pady=10)

    columns = (
        "MemberID", "First", "Last", "Address", "Mobile",
        "Plan", "Payment", "Book", "Private", "Booklet",
        "Ebook", "HasCard", "CardNum"
    )

    table = ttk.Treeview(scrollable_frame, columns=columns, show="headings", height=15)
    table.pack(fill="both", expand=True, padx=10)

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=140)

    for row_data in members:
        table.insert("", tk.END, values=row_data)

    scroll_x = tk.Scrollbar(scrollable_frame, orient="horizontal", command=table.xview)
    table.configure(xscrollcommand=scroll_x.set)
    scroll_x.pack(fill="x")

    # ----------------------------------------------------
    # BACK BUTTON
    # ----------------------------------------------------
    def go_back():
        window.state("normal")
        window.geometry("550x500")
        clear_window()
        open_main_menu()

    tk.Button(
        scrollable_frame,
        text="Back to Menu",
        font=("Arial", 14),
        command=go_back
    ).pack(pady=20)
