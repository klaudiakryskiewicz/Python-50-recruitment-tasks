"""Co stanie się w wyniku wykonania poniższego kodu?"""

x = 10


def f():
    global x
    x = 111
    y = 12
    print(x, y)


f()
print(x)
