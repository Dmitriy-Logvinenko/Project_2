import json
import os

from abc import ABC, abstractmethod


class BaseJSONSaver(ABC):

    @abstractmethod
    def add_aeroplane(self, aeroplanes):
        pass

    @abstractmethod
    def delete_aeroplane(self):
        pass


class JSONSaver(BaseJSONSaver):

    def add_aeroplane(self, aeroplanes):
        base_path = os.path.dirname(os.path.dirname(__file__))
        full_path = os.path.join(base_path, "data", "aeroplanes.json")

        with open(full_path, 'a', encoding="UTF-8") as f:
            json.dump(aeroplanes, f)

    def delete_aeroplane(self):
        base_path = os.path.dirname(os.path.dirname(__file__))
        full_path = os.path.join(base_path, "data", "aeroplanes.json")

        with open(full_path, 'w', encoding="UTF-8") as f:
            if f:
                json.dump([], f)


if __name__ == "__main__":
    api = JSONSaver()
    pi = api.delete_aeroplane()
