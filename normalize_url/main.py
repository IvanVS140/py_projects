"""normalize url example"""


def normalize_url(address):
    """
normalize url
    :param address:
    :return:
    """
    if address[:4] == 'www.':
        return 'https://' + address[4:]
    if address[:7] == 'http://':
        return 'https://' + address[7:]
    if address[:8] == 'https://':
        return address
    return 'https://' + address


print('{}\n{}\n{}\n{}\n\n {}'.format(normalize_url('https://ya.ru'),
                                     normalize_url('http://mail.ru'),
                                     normalize_url('google.com'),
                                     normalize_url('www.youtube.com'),
                                     'Have. a. nice. day.'))
