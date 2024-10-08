# main.py

from dao.donation_dao import DonationDAO
from entity.donation import CashDonation, ItemDonation
import sqlite3

def main():
    db_connection = sqlite3.connect('donations.db')  # Change the path as necessary
    donation_dao = DonationDAO(db_connection)
    
    while True:
        print("1. Add Cash Donation")
        print("2. Add Item Donation")
        print("3. View All Donations")
        print("4. Add Adoption Event")
        print("5. Register Participant to Event")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            donor_name = input("Enter donor name: ")
            amount = float(input("Enter donation amount: "))
            donation_date = input("Enter donation date (YYYY-MM-DD): ")
            cash_donation = CashDonation(donor_name, amount, donation_date)
            donation_dao.add_cash_donation(cash_donation)

        elif choice == '2':
            donor_name = input("Enter donor name: ")
            item_value = float(input("Enter item value: "))
            donation_date = input("Enter donation date (YYYY-MM-DD): ")
            item_donation = ItemDonation(donor_name, item_value, donation_date)
            donation_dao.add_item_donation(item_donation)

        elif choice == '3':
            donations = donation_dao.get_all_donations()
            for donation in donations:
                print(donation)

        elif choice == '6':
            break

if __name__ == "__main__":
    main()
