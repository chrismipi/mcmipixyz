from ...main.modules import utils


def test_mac_os():
    os = 'mac_os'
    res = utils.get_user_details(os)

    assert res['name'] == 'Chris'
    assert res['surname'] == 'Mipi'


def test_windows():
    os = 'windows'
    res = utils.get_user_details(os)

    assert res['name'] == 'Makhabane'
    assert res['surname'] == 'Mipi'


def test_linux():
    os = 'linux'
    res = utils.get_user_details(os)

    assert res['name'] == 'Christopher'
    assert res['surname'] == 'Mipi'
