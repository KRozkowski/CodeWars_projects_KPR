roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
def solution(roman : str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
    #convert string into list of symbols
    letter = [l for l in roman]
    arabic = 0
    x = 0

    while x<len(letter):
        if x+1 <len(letter) and roman_dict[letter[x+1]] > roman_dict[letter[x]]:
            #subtract current numeral from following larger one
            arabic += (roman_dict[letter[x+1]]-roman_dict[letter[x]])
            #move by 2 as the next symbol was already used
            x+=2

        else:
            arabic += roman_dict[letter[x]]
            x+=1

    return arabic
