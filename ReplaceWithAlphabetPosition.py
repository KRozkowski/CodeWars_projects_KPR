import string

def alphabet_position(text):
    result = []
    text_lower = text.lower()
    for i in range(len(text_lower)):
        if text_lower[i].isalpha():
            result.append(string.ascii_lowercase.find(text_lower[i])+1)
        else:
            continue

    return str(" ".join(map(str,result)))
