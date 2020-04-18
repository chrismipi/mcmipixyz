from ..main import utils


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


def test_ip_localhost():
    assert utils.valid_ip_address('127.0.0.1') == False
    assert utils.valid_ip_address('0.0.0.0') == False


def test_ip_valid_ip():
    assert utils.valid_ip_address('41.144.74.153') == True
