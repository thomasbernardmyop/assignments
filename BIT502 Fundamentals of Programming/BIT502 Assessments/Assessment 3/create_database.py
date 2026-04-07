import os
import sqlite3

# Always create DB in the same folder as this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "theauroraarchive_database.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Memberships (
    MemberID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_Name TEXT NOT NULL,
    Last_Name TEXT NOT NULL,
    Address TEXT NOT NULL,
    Mobile TEXT NOT NULL,
    Membership_Plan TEXT NOT NULL,
    Payment_Plan TEXT NOT NULL,
    Extra_Book_Rental INTEGER NOT NULL,
    Extra_Private_Area INTEGER NOT NULL,
    Extra_Booklet INTEGER NOT NULL,
    Extra_Ebook_Rental INTEGER NOT NULL,
    Has_Library_Card INTEGER NOT NULL,
    Library_Card_Number TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully.")