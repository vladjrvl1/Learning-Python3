words = tuple(input().lower().split())
for word in set(words):
    print(word, words.count((word)))




