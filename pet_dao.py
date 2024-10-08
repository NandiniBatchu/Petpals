import sqlite3
from entity.pet import pet

class PetDAO:
    def __init__(self, db_connection):
        self.conn = db_connection
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS pets
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT,
                           age INTEGER,
                           breed TEXT)''')
        self.conn.commit()

    def add_pet(self, pet):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO pets (name, age, breed) VALUES (?, ?, ?)", (pet.name, pet.age, pet.breed))
        self.conn.commit()

    def get_available_pets(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM pets")
        return cursor.fetchall()

    def delete_pet(self, pet_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM pets WHERE id = ?", (pet_id,))
        self.conn.commit()
