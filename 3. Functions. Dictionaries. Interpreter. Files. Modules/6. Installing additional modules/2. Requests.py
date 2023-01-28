import requests


url, name = 'https://stepic.org/media/attachments/course67/3.6.3/', '_.txt'
while name[:2] != 'We':
    name = requests.get(url + name).text
print(name)