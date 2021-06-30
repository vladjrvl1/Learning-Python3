alphabet = [i for i in input().strip()]
cipher = [i for i in input().strip()]
encryption = input().strip()
decryption = input().strip()


def cryption(symbols, cipher, to_encription='', to_decryption=''):
    d = dict(zip(symbols, cipher))
    encryption_res = ''
    for i in to_encription:
        if i in d.keys():
            encryption_res += d[i]
        else:
            encryption_res += i
    d = dict(zip(cipher, symbols))
    decryption_res = ''
    for i in to_decryption:
        if i in d.keys():
            decryption_res += d[i]
        else:
            decryption_res += i
    return [encryption_res, decryption_res]


print(*cryption(alphabet, cipher, encryption, decryption), sep='\n')
