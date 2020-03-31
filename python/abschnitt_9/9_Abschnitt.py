temps = [22,23,234,234123,-999,122]

new_temp = [temp  / 10 for temp in temps]

print(new_temp)

net_t = [temp if temp != -999 else 0 for temp in temps]



liste= ['1.2','2.3','4.4']

def foo(liste):
    return sum([float(item) for item in liste])

print(foo(liste))


def fo(*args):
    x = [item.upper() for item in args]
    print(x)

fo(liste)