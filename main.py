from src.aeroplanes import Aeroplane
from src.api import AeroplanesAPI
from src.jsonsaver import JSONSaver


# Функция для взаимодействия с пользователем
def user_interaction():
    country = input("Введите название страны: ")
    try:
        top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    except ValueError:
        top_n = 0
    filter_words = input("Введите названия стран, для фильтрации по стране регистрации, через запятую: ")

    api = AeroplanesAPI()

    # try:
    info_aeroplanes = api.get_aeroplanes(country)
    # except KeyError:
    #     "Страна не найдена"

    aeroplanes = Aeroplane.cast_to_object_list(info_aeroplanes)
    aero_of_fw = Aeroplane.filter_aeroplanes(aeroplanes, filter_words)
    sorted_geo_altitude = Aeroplane.geo_altitude_comparison(aero_of_fw)
    top_aeroplanes = Aeroplane.get_top_aeroplanes(sorted_geo_altitude, top_n)

    json_saver = JSONSaver()
    json_saver.add_aeroplane(top_aeroplanes)
    print(JSONSaver.format_info(top_aeroplanes))

    return top_aeroplanes


if __name__ == "__main__":
    user_interaction()
