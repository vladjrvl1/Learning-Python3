class Solution:
    def __init__(self, alphabet: str, cipher: str, encryption: str, decryption: str):
        self.alphabet = alphabet
        self.cipher = cipher
        self.encryption = encryption
        self.decryption = decryption

    def cryption(self, symbols, cipher, to_encription='', to_decryption='') -> list:
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

