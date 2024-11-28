from preloaded import MORSE_CODE

def decode_morse(morse_code):
    #removing leading and trailing spaces
    input = morse_code.strip()
    #creating list of morse letters
    letters = input.split(' ')
    #converting morse letters to roman alphabet
    converted_letters = []
    for letter in letters:
        if letter != '':
            converted_letters.append(MORSE_CODE[letter])
        else:
            converted_letters.append(' ')
    #putting decoded message together
    decoded_message_tmp = ''.join(converted_letters)
    decoded_message = decoded_message_tmp.replace('  ',' ')
    return decoded_message
