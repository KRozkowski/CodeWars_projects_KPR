import math
def subs_offset_apply(st, offset):
    offset_h = math.floor(offset/3600000)
    offset_min = math.floor((offset-offset_h*3600000)/60000)
    offset_sec = math.floor((offset-offset_h*3600000-offset_min*60000)/1000)
    offset_ms = offset-offset_h*3600000-offset_min*60000-offset_sec*1000

    s = [n for n in st]

    new_start_h = int(s[0])*10+int(s[1])+offset_h
    new_start_min = int(s[3])*10+int(s[4])+offset_min
    new_start_sec = int(s[6])*10+int(s[7])+offset_sec
    new_start_ms = int(s[9])*100+int(s[10])*10+int(s[11])+offset_ms

    if new_start_ms >999:
        new_start_ms-=1000
        new_start_sec+=1
    else:
        new_start_ms
    if new_start_sec >59:
        new_start_sec-=60
        new_start_min+=1
    else:
        new_start_sec
    if new_start_min >59:
        new_start_min-=60
        new_start_h+=1
    else:
        new_start_min
    if new_start_h>99 or new_start_h<0:
        return "Invalid offset"
    else:
        new_start_h

    #finish time
    new_stop_h = int(s[17])*10+int(s[18])+offset_h
    new_stop_min = int(s[20])*10+int(s[21])+offset_min
    new_stop_sec = int(s[23])*10+int(s[24])+offset_sec
    new_stop_ms = int(s[26])*100+int(s[27])*10+int(s[28])+offset_ms

    if new_stop_ms >999:
        new_stop_ms-=1000
        new_stop_sec+=1
    else:
        new_stop_ms
    if new_stop_sec >59:
        new_stop_sec-=60
        new_stop_min+=1
    else:
        new_stop_sec
    if new_stop_min >59:
        new_stop_min-=60
        new_stop_h+=1
    else:
        new_stop_min
    if new_stop_h>99 or new_stop_h<0:
        return "Invalid offset"
    else:
        new_stop_h

    #print(str("".join((str(s[30:-1])+(str(s[-1]))))))
    text =("".join(s[30:-1])+str(s[-1]))


    new_str = f"{new_start_h :02d}"+":"+f"{new_start_min :02d}"+":"+f"{new_start_sec:02d}"+","+f"{new_start_ms:03d}"+" --> "+f"{new_stop_h :02d}"+":"+f"{new_stop_min :02d}"+":"+f"{new_stop_sec:02d}"+","+f"{new_stop_ms:03d} "+text
    return(new_str)
