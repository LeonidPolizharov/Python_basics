import re


# def mail_parsing(mail):
#     parsed_mail = re.compile(r'^([0-9a-z._\-]+)\@((([0-9a-z\-]+\.)+)+[a-z]{2,})$', re.IGNORECASE).findall(mail)
#     try:
#         doc = {'username': parsed_mail[0][0], 'domain': parsed_mail[0][1]}
#         return doc
#     except IndexError as err:
#         msg = 'wrong email: ' + mail
#         raise ValueError(msg)


def mail_parsing(mail):
    try:
        parsed_mail = re.match(r'^(?P<username>[\w._\-]+)\@(?P<domain>(([0-9a-z\-]+\.)+)+[a-z]{2,})$', mail).groupdict()
        return parsed_mail
    except AttributeError as err:
        msg = 'wrong email: ' + mail
        raise ValueError(msg)


if __name__ == '__main__':
    print(mail_parsing('spp_a9.ad-Ded@ma-3il.ab-5n.com.info'))
    # print(mail_parsing('sp%p_a9.ad-Ded@ma-3il.ab-5n.com.info'))  # некорректный email




