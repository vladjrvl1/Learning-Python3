def razvertka(string):
    num = ''
    ss = ''
    for i in s[::-1]:
        if i.isdigit():
            num += i
        else:
            ss += i * int(num[::-1])
            num = ''
    return ss[::-1]

with open(r'C:\Users\Vlad_\Desktop\Chrome Downloads\dataset_3363_2 (3).txt') as f:
    s = f.read().strip()

with open(r'C:\Users\Vlad_\Desktop\Chrome Downloads\dataset_3363_2 (3).txt', 'w') as f:
    f.write(razvertka(s))
