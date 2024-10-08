# dao/donation_dao.py

import sqlite3
from entity.donation import CashDonation, ItemDonation  # Ensure to import the classes
from datetime import datetime

class DonationDAO:
    def __init__(self, db_connection):
        self.conn = db_connection
        self.cursor = self.conn.cursor()
        # Ensure your table is created
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS donations (
                id INTEGER PRIMARY KEY,
                donor_name TEXT,
                amount REAL,
                donation_type TEXT,
                donation_date TEXT
            )
        """)
        self.conn.commit()

    def add_cash_donation(self, cash_donation: CashDonation):
        self.cursor.execute("""
            INSERT INTO donations (donor_name, amount, donation_type, donation_date) 
            VALUES (?, ?, 'cash', ?)
        """, (cash_donation.donor_name, cash_donation.amount, cash_donation.donation_date.strftime('%Y-%m-%d')))
        self.conn.commit()

    def add_item_donation(self, item_donation: ItemDonation):
        self.cursor.execute("""
            INSERT INTO donations (donor_name, amount, donation_type, donation_date) 
            VALUES (?, ?, 'item', ?)
        """, (item_donation.donor_name, item_donation.item_value, item_donation.donation_date.strftime('%Y-%m-%d')))
        self.conn.commit()
    
    def get_all_donations(self):
        self.cursor.execute("SELECT * FROM donations")
        rows = self.cursor.fetchall()
        donations = []
        for row in rows:
            donation_type = row[3]
            if donation_type == 'cash':
                donations.append(CashDonation(row[1], row[2], row[4]))  # donor_name, amount, donation_date
            elif donation_type == 'item':
                donations.append(ItemDonation(row[1], row[2], row[4]))  # donor_name, item_value, donation_date
        return donations
