#-------------------------------#
#     BIT502 - Assessment 3     #
#         Thomas Bernard        #
#      Student ID 5142644       #
#-------------------------------#

# database.py
# This file contains the database functions for the application.

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "theauroraarchive_database.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Ensure table exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS Memberships (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_Name TEXT,
    Last_Name TEXT,
    Address TEXT,
    Mobile TEXT,
    Membership_Plan TEXT,
    Payment_Plan TEXT,
    Extra_Book_Rental INTEGER,
    Extra_Private_Area INTEGER,
    Extra_Booklet INTEGER,
    Extra_Ebook_Rental INTEGER,
    Has_Library_Card INTEGER,
    Library_Card_Number TEXT
)
""")
conn.commit()


def insert_member(values):
    cursor.execute("""
        INSERT INTO Memberships
        (First_Name, Last_Name, Address, Mobile, Membership_Plan, Payment_Plan,
         Extra_Book_Rental, Extra_Private_Area, Extra_Booklet, Extra_Ebook_Rental,
         Has_Library_Card, Library_Card_Number)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, values)
    conn.commit()


def fetch_all(query, params=()):
    cursor.execute(query, params)
    return cursor.fetchall()