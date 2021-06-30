d = {i: [0, 0] for i in range(1, 12)}
with open('data.txt', 'r') as f:
    height_data = f.readlines()

for i in height_data:
    class_key = int(i[:i.find('\t')])
    d[class_key][1] += 1
    height = int(i[i.find('\t', 3) + 1:i.find('\n')])
    d[class_key][0] += height

with open('data_answer.txt', 'w') as f:
    for key, value in d.items():
        if value[1] != 0:
            f.write(f'{key} {str(round(value[0] / value[1], 5))}\n')
        else:
            f.write(f'{key} -\n')

print(d)