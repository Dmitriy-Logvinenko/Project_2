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
    def cast_to_object_list(list_aeroplanes: dict) -> list[Aeroplane]:
        my_list = []
        for i in list_aeroplanes.get('states', []):
            my_list.append(Aeroplane(i[2], i[1], i[9], i[13], i[10]))
        return my_list


if __name__ == "__main__":
    api = AeroplanesAPI()
    ati = api.get_aeroplanes('Canada')

    print(Aeroplane.cast_to_object_list(ati))

# str метод для читаемого вывода
