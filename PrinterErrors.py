import string
def printer_error(s):
    total = len(s)
    e = []
    for i in s:
        if string.ascii_lowercase.index(i)>string.ascii_lowercase.index('m'):
            e.append(i)
        else:
            e.append("")
    e_str = str("".join(e))
    rate = f'{len(e_str)}/{len(s)}'
    return rate
