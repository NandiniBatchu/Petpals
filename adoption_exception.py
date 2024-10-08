class AdoptionException(Exception):
    def __init__(self, message="Error during adoption process"):
        self.message = message
        super().__init__(self.message)
