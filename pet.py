class pet:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}"

    # Getters and setters
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def get_breed(self):
        return self.breed
    
    def set_breed(self, breed):
        self.breed = breed
