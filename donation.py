# donation.py

from abc import ABC, abstractmethod
from datetime import datetime

class Donation(ABC):
    def __init__(self, donor_name: str, amount: float):
        self.donor_name = donor_name
        self.amount = amount

    @abstractmethod
    def record_donation(self):
        """Abstract method to record the donation."""
        pass


# entity/donation.py
# entity/donation.py

from datetime import datetime

class CashDonation:
    def __init__(self, donor_name: str, amount: float, donation_date: str):
        self.donor_name = donor_name
        self.amount = amount
        # Assuming donation_date is a string in the format 'YYYY-MM-DD'
        self.donation_date = datetime.strptime(donation_date, '%Y-%m-%d')

    def __str__(self):
        return f"Cash Donation - Donor: {self.donor_name}, Amount: {self.amount}, Date: {self.donation_date.strftime('%Y-%m-%d')}"

class ItemDonation:
    def __init__(self, donor_name: str, item_value: float, donation_date: str):
        self.donor_name = donor_name
        self.item_value = item_value
        # Assuming donation_date is a string in the format 'YYYY-MM-DD'
        self.donation_date = datetime.strptime(donation_date, '%Y-%m-%d')

    def __str__(self):
        return f"Item Donation - Donor: {self.donor_name}, Item Value: {self.item_value}, Date: {self.donation_date.strftime('%Y-%m-%d')}"
