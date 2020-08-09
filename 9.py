"""Dla danego stringa x stwórz słownik przechowujący
informację, ile razy dana litera wystąpiła w stringu."""

x = "myszydokazujągdykotanieczują"
letters = {}

for letter in x:
    if letters.get(letter):
        letters[letter] += 1
    else:
        letters[letter] = 1

print(letters)