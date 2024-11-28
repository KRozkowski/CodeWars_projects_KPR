def solution(s):
    result =[]
    for i in range(0,len(s)):
        if s[i].isupper():
            result.append(" "+s[i])
        else:
            result.append(s[i])
    return str("".join(result))
