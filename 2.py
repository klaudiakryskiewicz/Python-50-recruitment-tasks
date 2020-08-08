"""Co się stanie po wykonaniu poniższego kodu?"""

a = 'abcdefg'

list_ = list(a)

list_[1] = 'X'
a = "".join(list_)
print(a)
