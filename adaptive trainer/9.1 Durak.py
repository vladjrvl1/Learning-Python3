"""
A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S).
Each card also has a value of either 6 through 10, jack, queen, king, or ace (denoted 6, 7, 8, 9, 10, J, Q, K, A).
For scoring purposes card values are ordered as above, with 6 having the lowest and ace the highest value.

Напишите программу, которая определяет, бьёт ли одна карта другую.
Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
Если карты разных мастей и нет козырных, то никто не побеждает.

Формат ввода:
На первой строке через пробел указываются две карты в формате <значение><масть>,
а на следующей строке указывается козырная масть.

Формат вывода:
Программа должна вывести слово
First, если первая карта бьёт вторую,
Second, если вторая карта бьёт первую,
Error, если ни одна из карт не может побить другую.
"""
# spades (denoted C, D, H, S)
# card value (denoted 6, 7, 8, 9, 10, J, Q, K, A)

d = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
     'J': 11, 'Q': 12, 'K': 13, 'A': 14}


cards = input()
trump = input()

card1 = [cards[:cards.find(' ') - 1], cards[cards.find(' ') - 1: cards.find(' ')]]
card2 = [cards[cards.find(' ') + 1:-1], cards[-1]]

if card1[1] == card2[1]:
    if d[card1[0]] > d[card2[0]]:
        print('First')
    else:
        print('Second')
elif card1[1] == trump:
    print('First')
elif card2[1] == trump:
    print('Second')
elif card1[1] != card2[1]:
    print("Error")
else:
    print('Error')
