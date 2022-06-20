"""normalize url example"""


def normalize_url(url):
    """converts any URLs into https-type

    Args:
        url (str): any URL

    Returns:
        str: https-type URL
    """
    pref = 'https://'
    if url[:4] == 'www.':
        return pref + url[4:]
    if url[:7] == 'http://':
        return pref + url[7:]
    if url[:8] == 'https://':
        return url
    return pref + url


if __name__ == '__main__':
    print('\n{}\n{}\n{}\n{}\n'.format(normalize_url('https://ya.ru'),
                                      normalize_url('http://mail.ru'),
                                      normalize_url('google.com'),
                                      normalize_url('www.youtube.com')))
