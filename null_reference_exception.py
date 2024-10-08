class NullReferenceException(Exception):
    def __init__(self, message="Null reference encountered"):
        self.message = message
        super().__init__(self.message)
