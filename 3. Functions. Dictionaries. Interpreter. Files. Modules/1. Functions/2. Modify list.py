def modify_list(l):
    length = len(l) - 1
    while length != -1:
        if l[length] % 2:
            del l[length]
        else:
            l[length] = l[length] // 2
        length -= 1