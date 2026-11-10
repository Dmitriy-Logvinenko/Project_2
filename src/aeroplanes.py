from src.api import AeroplanesAPI


class Aeroplane:
    aeroplanes: dict

    # Разберись с тем, чтобы Aeroplane(aeroplanes) запускался без обозначения всех параметров
    def __init__(self, country_reg, callsign, velocity, geo_altitude, true_track):
        self.country_reg = self.__validation_country_reg(country_reg)
        self.callsign = self.__validation_callsign(callsign)
        self.velocity = self.__validation_velocity(velocity)
        self.geo_altitude = self.__validation_geo_altitude(geo_altitude)
        self.true_track = self.__validation_true_track(true_track)

    @staticmethod
    def __validation_country_reg(country_reg: str) -> str | None:
        if type(country_reg) is str:
            return country_reg
        return "Самолёт не найден."

    @staticmethod
    def __validation_callsign(callsign: str) -> str | None:
        if type(callsign) is str and callsign != "":
            return callsign
        return "Позывной отсутствует"

    @staticmethod
    def __validation_velocity(velocity: float) -> float:
        if type(velocity) is float:
            return velocity
        return 0

    @staticmethod
    def __validation_geo_altitude(geo_altitude: float) -> float:
        if type(geo_altitude) is float:
            return geo_altitude
        return 0

    @staticmethod
    def __validation_true_track(true_track: float | int) -> float | int:
        if type(true_track) is float or type(true_track) is int:
            return true_track
        return 0

    def __repr__(self):
        str_info_aeroplane = (f"{self.country_reg}, "
                              f"{self.callsign}, {self.velocity}, {self.geo_altitude}, {self.true_track}")
        return str_info_aeroplane

    def __str__(self):
        str_aeroplanes = f"{self.country_reg}, {self.callsign}, {self.velocity}, {self.geo_altitude}, {self.true_track}"
        return str_aeroplanes

    @staticmethod
    def cast_to_object_list(dict_aeroplanes: dict) -> list[list[Aeroplane]]:
        list_aeroplanes = []

        for i in dict_aeroplanes.get("states", []):
            list_aeroplane = []
            list_aeroplane.append(Aeroplane(i[2], i[1].strip(), i[9], i[13], i[10]))
            list_aeroplanes.append(list_aeroplane)

        return list_aeroplanes

    @staticmethod
    def geo_altitude_comparison(aeroplanes: list[list[Aeroplane]]) -> list[list[Aeroplane]]:
        sorted_aeroplanes = sorted(aeroplanes, key=lambda k: k[0].geo_altitude, reverse=True)
        return sorted_aeroplanes

    @staticmethod
    def speed_comparison(aeroplanes: list[list[Aeroplane]]) -> list[list[Aeroplane]]:
        sorted_aeroplanes = sorted(aeroplanes, key=lambda k: k[0].velocity, reverse=True)
        return sorted_aeroplanes

    @staticmethod
    def filter_aeroplanes(aeroplanes: list[list[Aeroplane]], filter_words: str) -> list[list[Aeroplane]]:
        """Функция для фильтрации самолётов по стране регистрации"""
        filter_list = list()
        filter_words = filter_words.title().split(", ")

        for aeroplane in aeroplanes:
            for word in filter_words:
                if aeroplane[0].country_reg == word.title():
                        filter_list.append(aeroplane)

        return filter_list

    @staticmethod
    def get_top_aeroplanes(aeroplanes: list[list[Aeroplane]], top_n: int) -> list[list[Aeroplane]]:
        if top_n != 0:
            top_n_aeroplanes = aeroplanes[:top_n]
            return top_n_aeroplanes
        else:
            print("Не удалось обработать данные. Будет выведен полный список.")
            return aeroplanes


if __name__ == "__main__":
    api = AeroplanesAPI()
    ati = api.get_aeroplanes("Spain")

    pi = Aeroplane.cast_to_object_list(ati)

    print(pi)
    print(Aeroplane.filter_aeroplanes(pi, "Spain, China"))
    print(Aeroplane.geo_altitude_comparison(pi))
    print(Aeroplane.speed_comparison(pi))
    print(Aeroplane.get_top_aeroplanes(pi, 3))
    print(str(Aeroplane.get_top_aeroplanes(pi, 3)))
