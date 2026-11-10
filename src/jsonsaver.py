import json
import os

from abc import ABC, abstractmethod

from src.aeroplanes import Aeroplane


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

        data = JSONSaver.format_info(aeroplanes)

        with open(full_path, "w", encoding="UTF-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

    def delete_aeroplane(self):
        base_path = os.path.dirname(os.path.dirname(__file__))
        full_path = os.path.join(base_path, "data", "aeroplanes.json")

        with open(full_path, "w", encoding="UTF-8"):
            pass

    @staticmethod
    def format_info(aeroplanes: list[list[Aeroplane]]) -> list[list[Aeroplane]]:
        str_aeroplanes = []

        for aeroplane in aeroplanes:
            str_aeroplane = {
                "Страна регистрации": aeroplane[0].country_reg,
                "Позывной": aeroplane[0].callsign,
                "Скорость полёта": aeroplane[0].velocity,
                "Высота полёта": aeroplane[0].geo_altitude,
                "Курс": aeroplane[0].true_track,
            }
            str_aeroplanes.append(str_aeroplane)

        return str_aeroplanes
