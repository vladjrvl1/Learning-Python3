import requests

with open('data.txt') as f:
    url_from_file = f.read().strip()
cont = requests.get(url_from_file)

cnt = 0
while True:
    cnt += 1
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + cont.text
    cont = requests.get(url)
    if cont.text.startswith('We'):
        with open('data_answer.txt', 'w') as f:
            f.write(cont.text)
        print(cnt, 'get requests')
        break
    print(cont.text)

