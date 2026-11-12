from src.aeroplanes import Aeroplane


def test_aeroplane_init(aeroplane):
    assert aeroplane.country_reg == 'Spain'
    assert aeroplane.callsign == 'SCP-173'
    assert aeroplane.velocity == 100.0
    assert aeroplane.geo_altitude == 10000.0
    assert aeroplane.true_track == 10.0


def test_aeroplane_str(aeroplane, capsys):
    assert str(aeroplane) == 'Spain, SCP-173, 100.0, 10000.0, 10.0'


def test_aeroplane_cast_to_object_list(aeroplanes_dict):
    assert Aeroplane.cast_to_object_list(aeroplanes_dict).__repr__() == (
        '[[Spain, SCP-173, 350.0, 10000.0, 10.0], '
        '[Canada, SCP-003, 100.0, 17895.0, 34.0], '
        '[China, SCP-143, 200.0, 11234.0, 21.0]]'
    )


def test_aeroplanes_geo_altitude_comparison(aeroplanes):
    assert Aeroplane.geo_altitude_comparison(aeroplanes).__repr__() == (
        '[[Canada, SCP-003, 100.0, 17895.0, 34.0], '
        '[China, SCP-143, 200.0, 11234.0, 21.0], '
        '[Spain, SCP-173, 350.0, 10000.0, 10.0]]'
    )


def test_aeroplane_speed_comparison(aeroplanes):
    assert Aeroplane.speed_comparison(aeroplanes).__repr__() == (
        '[[Spain, SCP-173, 350.0, 10000.0, 10.0], '
        '[China, SCP-143, 200.0, 11234.0, 21.0], '
        '[Canada, SCP-003, 100.0, 17895.0, 34.0]]'
    )


def test_aeroplane_filter(aeroplanes):
    assert Aeroplane.filter_aeroplanes(aeroplanes, 'Spain').__repr__() == (
        '[[Spain, SCP-173, 350.0, 10000.0, 10.0]]'
    )


def test_aeroplane_top_n(aeroplanes):
    assert Aeroplane.get_top_aeroplanes(aeroplanes, 2).__repr__() == (
        '[[Spain, SCP-173, 350.0, 10000.0, 10.0], '
        '[Canada, SCP-003, 100.0, 17895.0, 34.0]]'
    )
