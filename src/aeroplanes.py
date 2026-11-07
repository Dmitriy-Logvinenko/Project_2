from src.api import AeroplanesAPI


class Aeroplane:
    aeroplanes: dict

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
        return 'Самолёт не найден.'

    @staticmethod
    def __validation_callsign(callsign: str) -> str | None:
        if type(callsign) is str:
            return callsign
        return 'Самолёт не найден'

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
        str_info_aeroplane = (f'{self.country_reg}, '
                              f'{self.callsign}, {self.velocity}, {self.geo_altitude}, {self.true_track}')
        return str_info_aeroplane

    @staticmethod
    def cast_to_object_list(dict_aeroplanes: dict) -> list[list[Aeroplane]]:
        list_aeroplanes = []

        for i in dict_aeroplanes.get('states', []):
            list_aeroplane = []
            list_aeroplane.append(Aeroplane(i[2], i[1].strip(), i[9], i[13], i[10]))
            list_aeroplanes.append(list_aeroplane)

        return list_aeroplanes

    def geo_altitude_comparison(self, other):
        if self.geo_altitude < other.geo_altitude:
            return True
        return False

    def speed_comparison(self, other):
        if self.velocity > other.velocity:
            return True
        return False

    @staticmethod
    def filter_aeroplanes(aeroplanes: list[list[Aeroplane]], country_reg: str) -> list[list[Aeroplane]]:
        """Функция для фильтрации самолётов по стране регистрации"""
        filter_list = list()

        for aeroplane in aeroplanes:
            if aeroplane[0] == country_reg:
                filter_list.append(aeroplane)

        return filter_list


if __name__ == "__main__":
    api = AeroplanesAPI()
    ati = api.get_aeroplanes('Canada')

    pi = Aeroplane.cast_to_object_list(ati)
    print(pi)
    print(Aeroplane.filter_aeroplanes(pi, 'Canada'))

# str метод для читаемого вывода
