import pytest

from src.aeroplanes import Aeroplane


@pytest.fixture
def aeroplane():
    return Aeroplane('Spain', 'SCP-173', 100.0, 10000.0, 10.0)


@pytest.fixture
def aeroplanes_dict():
    return {'states': [[
        0,
        'SCP-173', # i[1] = country_reg
        'Spain',   # i[2] = callsign
        3,
        4,
        5,         # пустые значения (для заполнения шаблона)
        6,
        7,
        8,
        350.0,     # i[9] = velocity
        10.0,      # i[10] = true_track
        11,
        12,
        10000.0    # i[13] = geo_altitude
    ], [
        0,
        'SCP-003',
        'Canada',
        3,
        4,
        5,
        6,
        7,
        8,
        100.0,
        34.0,
        11,
        12,
        17895.0
    ], [
        0,
        'SCP-143',
        'China',
        3,
        4,
        5,
        6,
        7,
        8,
        200.0,
        21.0,
        11,
        12,
        11234.0
    ]

    ]}


@pytest.fixture
def aeroplanes(aeroplanes_dict):
    aero = Aeroplane.cast_to_object_list(aeroplanes_dict)
    return aero
