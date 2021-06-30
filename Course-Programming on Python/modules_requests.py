import requests

f_path = 'data.txt'
with open(f_path, 'r') as f:
    url_from_f = f.read().strip()
content = requests.get(url_from_f)
print(len(content.text.splitlines()))
print(content.text.splitlines())

