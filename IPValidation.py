def is_valid_IP(strng):
    x= strng.split(".")
    test=0
    if len(x) < 4 or len(x) >4 : test+=1
    for i in x:
        if not i.isnumeric():
            test+=1
        elif int(i) < 0 or int(i) > 255:
            test+=1
        elif i[0]=="0" and len(i) is not 1:
            test+=1
        else:
            test+=0
    return True if test==0 else False
