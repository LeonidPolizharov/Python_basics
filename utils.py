def currency_rates(inp_arg):
    import requests
    from datetime import datetime
    from decimal import Decimal
    cbr_request = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encode = requests.utils.get_encoding_from_headers(cbr_request.headers)
    cbr_content = cbr_request.content.decode(encoding=encode)
    parsed_cont = cbr_content.replace('>', ' ').replace('<', ' ').split()
    # date = datetime.date(datetime.strptime(cbr_request.headers['Date'], "%a, %d %b %Y %H:%M:%S %Z"))
    date = ''
    for i in parsed_cont:
        if i[0:4] == 'Date':
            date = datetime.date(datetime.strptime(i[6:16], "%d.%m.%Y"))

    if inp_arg.upper() in parsed_cont and not inp_arg.isdigit():
        inp_arg = inp_arg.upper()
        rate = None
        nom = None
        for i, val in enumerate(parsed_cont):
            if val == inp_arg:
                for j, sec_val in enumerate(parsed_cont[i:]):
                    if sec_val == 'Nominal' and parsed_cont[i + j + 1][0].isdigit():
                        nom = parsed_cont[i + j + 1]
                    if sec_val == 'Value' and parsed_cont[i + j + 1][0].isdigit():
                        rate = parsed_cont[i + j + 1].replace(',', '.')
                        break
    else:
        return None
    return Decimal(rate), nom, date
