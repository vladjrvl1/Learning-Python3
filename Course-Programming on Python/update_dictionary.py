def update_dictionary(d, key, value):
    if key in d.keys():
        d.get(key).append(value)
    elif key * 2 in d.keys():
        d.get(key*2).append(value)
    else:
        d.update({key*2: [value]})

