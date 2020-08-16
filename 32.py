"""Do czego w Pythonie służą dekoratory? Napisz
dekorator, który będzie dodawał trzy gwiazdki przed i po
efekcie działania udekorowanej funkcji."""

def my_dec(func):
    def wrap_the_func():
        print('***')
        func()
        print('***')

    return wrap_the_func

@my_dec
def func():
    print("abc")

func()