"""Napisz funkcję sprawdzającą, czy podane słowo jest
palindromem.
Uruchom funkcję, aby sprawdzić, czy palindromami są
słowa "kajak" i "anakonda"."""

def check_palindrome(word):
    return word == word[::-1]


print(check_palindrome("kajak"))
print(check_palindrome("anakonda"))