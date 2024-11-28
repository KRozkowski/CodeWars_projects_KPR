def array_diff(a, b):
    result = []
    for i in range(len(a)):
        if a[i] in b:
            continue
        else:
            result.append(a[i])

    return result
