class FileHandlingException(Exception):
    def __init__(self, message="An error occurred while handling the file"):
        self.message = message
        super().__init__(self.message)