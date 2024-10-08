from entity.pet import pet
class Cat(pet):
    def __init__(self, name, age, breed, cat_color):
        super().__init__(name, age, breed)
        self.cat_color = cat_color

    def __str__(self):
        return f"{super().__str__()}, CatColor: {self.cat_color}"

    # Getters and setters for cat color
    def get_cat_color(self):
        return self.cat_color
    
    def set_cat_color(self, cat_color):
        self.cat_color = cat_color

