#VALUES example: VALUES = { "EUR": [5, 10, 20, 50, 100, 200, 500], "USD": [ 1, 2, 5, 10, 20, 50, 100, 200] }

from preloaded import VALUES
def atm(value):
    val = ""
    curr = ""
    #putting customer entry in managable format splitting currency and amount
    for i in range(len(value)):
        if value[i].isdigit():
            val += value[i]
        elif value[i].isalpha():
            curr += value[i]
        else:
            continue
    val_int = int(val)
    curr_up = curr.upper()

    #checking if ATM handles the currency
    if curr_up not in VALUES:
        return f"Sorry, have no {curr_up}."

    else:
        bnotes = VALUES[curr_up]

        #processing customer request
        result = ""
        i = -1
        orig_val = val_int
        #additional test added
        if val_int % bnotes[0] != 0:
            return f"Can't do {orig_val} {curr_up}. Value must be divisible by {bnotes[0]}!"
        #building a string
        while i*-1<=len(bnotes):
            note, rest = divmod(val_int,bnotes[i])
            if note ==0 and rest!=0 and rest<bnotes[0]:
                result = str(f'Can\'t do {orig_val} {curr_up}. Value must be divisible by {bnotes[0]}!')

            if note != 0:
                result+=(f'{note} * {bnotes[i]} {curr_up}, ')
                val_int -=(bnotes[i]*note)
                i-=1

            elif note ==0:
                i-=1


        return result.rstrip(", ")
