from entity.pet import pet
class Dog(pet):
    def __init__(self, name, age, breed, dog_breed):
        super().__init__(name, age, breed)
        self.dog_breed = dog_breed

    def __str__(self):
        return f"{super().__str__()}, DogBreed: {self.dog_breed}"

    # Getters and setters for dog breed
    def get_dog_breed(self):
        return self.dog_breed
    
    def set_dog_breed(self, dog_breed):
        self.dog_breed = dog_breed
   
