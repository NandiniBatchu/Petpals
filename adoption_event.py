# entity/adoption_event.py

from abc import ABC, abstractmethod
from typing import List

class IAdoptable(ABC):
    @abstractmethod
    def adopt(self):
        """Abstract method to handle the adoption process."""
        pass


class AdoptionEvent:
    def __init__(self):
        self.participants: List[IAdoptable] = []

    def host_event(self):
        """Hosts the adoption event and displays the participants."""
        print("Hosting the adoption event with the following participants:")
        for participant in self.participants:
            print(participant)  # You may want to implement __str__ in IAdoptable or its subclasses

    def register_participant(self, participant: IAdoptable):
        """Registers a participant for the event."""
        self.participants.append(participant)
        print(f"Registered participant: {participant}")

