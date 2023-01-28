import requests

with open('dataset.txt') as inf:
    r = requests.get(inf.readline().strip())
    print(len(r.text.splitlines()))