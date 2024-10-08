class InsufficientFundsException(Exception):
    def __init__(self, message="Donation amount is insufficient"):
        self.message = message
        super().__init__(self.message)
