import sqlite3
from entity.adoption_event import AdoptionEvent

class AdoptionEventDAO:
    def __init__(self):
        self.conn = sqlite3.connect("petpals.db")
        self.cursor = self.conn.cursor()

    def add_adoption_event(self, event: AdoptionEvent):
        self.cursor.execute("""
            INSERT INTO adoption_events (event_name, participants) 
            VALUES (?, ?)
        """, (event.event_name, len(event.participants)))
        self.conn.commit()

    def get_all_adoption_events(self):
        self.cursor.execute("SELECT * FROM adoption_events")
        events = self.cursor.fetchall()
        return events

    def register_participant(self, event_id, participant_name):
        self.cursor.execute("""
            INSERT INTO participants (event_id, participant_name)
            VALUES (?, ?)
        """, (event_id, participant_name))
        self.conn.commit()

    def get_event_participants(self, event_id):
        self.cursor.execute("SELECT * FROM participants WHERE event_id = ?", (event_id,))
        participants = self.cursor.fetchall()
        return participants

    def close(self):
        self.conn.close()
