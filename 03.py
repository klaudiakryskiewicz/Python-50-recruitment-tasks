"""Napisz kod, który zaprezentuje najważniejsze różnice
między listą a tuplą (krotką)."""

list_ = [1, 2, 3, 4]
print(list_)

tuple_ = 1, 2, 3, 4
print(tuple_)

list_.append(5)
# tuple_.append(5) - AtributeError

list_[1] = 0
# tuple_[1] = 0 - AtributeError
