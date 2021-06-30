d = int(input())
l = int(input())
words = set(input().lower().strip() for _ in range(d))
text = tuple(input().lower().strip().split() for _ in range(l))
wrongs = set()
for i in text:
    for j in i:
        if j not in words:
            wrongs.add(j)
print(*wrongs, sep='\n')



'''
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
'''