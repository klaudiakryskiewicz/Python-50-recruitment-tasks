"""Do czego w Pythonie służy słowo kluczowe yield ?
Napisz przykładowy kod wykorzystujący yield."""

def generator(n):
    for i in range(n):
        yield i


for item in generator(5):
    print(item)

gen = generator(5)

print(gen)  # <generator object generator_function at xxxxxxx>
print(next(gen))  # 0
print(gen.__next__())  # 1

