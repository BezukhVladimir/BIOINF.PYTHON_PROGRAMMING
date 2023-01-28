l = [(str(i).lower()) for i in input().split()]
d = {}
while len(l) > 0:
	if l[0] not in d:
		d[l[0]] = 1
		l.remove(l[0])
	else:
		d[l[0]] += 1
		l.remove(l[0])
for key, value in d.items():
	print(key, value)