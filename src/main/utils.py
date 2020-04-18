__IP_ADDRESSES = ['127.0.0.1', '0.0.0.0']


def get_user_details(os):
    res = dict(surname='Mipi')

    if os == 'windows':
        res['name'] = 'Makhabane'
    elif os == 'linux':
        res['name'] = 'Christopher'
    else:  # MacOS, Mobile and any other platform out there
        res['name'] = 'Chris'
    return res


def valid_ip_address(ip_address):
    return not __IP_ADDRESSES.__contains__(ip_address)
