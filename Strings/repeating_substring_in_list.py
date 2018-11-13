
def repeatingSub(s):
    n = 3
    patt_dict = {}
    for i in range(0, len(s) - n, 1):
        patt = (''.join(s[i:i+n]))
        if patt not in patt_dict.keys():
            patt_dict[patt] = 1
        else:
            patt_dict[patt] += 1
    for key in patt_dict.keys():
        if patt_dict[key] > 1:
            print('Found ', str(patt_dict[key]), ' repeating instances of ', str(key), '.')

