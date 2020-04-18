def get_user_details(os):
    res = dict(surname='Mipi')

    if os == 'windows':
        res['name'] = 'Makhabane'
    elif os == 'linux':
        res['name'] = 'Christopher'
    else:  # MacOS, Mobile
        res['name'] = 'Chris'
    return res
