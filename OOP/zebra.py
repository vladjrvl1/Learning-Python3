class Zebra:
    def __init__(self, cnt=0):
        self.cnt = cnt

    def which_stripe(self):
        self.cnt += 1
        if self.cnt % 2 == 1:
            print("Полоска белая")
        else:
            print("Полоска черная")


z1 = Zebra()
z1.which_stripe()  # печатает "Полоска белая"
z1.which_stripe()  # печатает "Полоска черная"
z1.which_stripe()  # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe()  # печатает "Полоска белая"
