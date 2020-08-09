"""Jakiej struktury danych użyłbyś do zapisania numerów
telefonów wszystkich klientów firmy
– i odpowiadających im nazwisk? Wybierz strukturę tak,
aby sprawdzenie właściciela numeru telefonu nie
zajmowało wiele czasu.
Następnie stwórz przykładową strukturę przechowującą
poniższe informacje:
123456789 – Jan Kot
999888777 – Anna Lis
111222333 – Jan Kot
Odczytaj nazwisko właściciela numeru 123456789."""

phone_numbers = {
    123456789: "Jan Kot",
    999888777: "Anna Lis",
    111222333: "Jan Kot"
}

print(phone_numbers.get(123456789))