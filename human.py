class Osoba:
    def __init__(self, plec, imie, wiek, kraj, zawod):
        self.plec = plec
        self.imie = imie
        self.wiek = wiek
        self.kraj = kraj
        self.zawod = zawod

    def przedstaw_sie(self):
        print(f"Cześć! Jestem {self.imie}. Mam {self.wiek} lat.")
        print(f"Jestem {self.plec} i pochodzę z {self.kraj}.")
        print(f"Aktualnie pracuję jako {self.zawod}.")


def sprawdz_czy_liczba(wartosc):
    try:
        int(wartosc)
        return True
    except ValueError:
        return False


plec = input("Podaj swoją płeć: ")
while sprawdz_czy_liczba(plec):
    plec = input("Podaj poprawną płeć (nie może być liczba): ")

imie = input("Podaj swoje imię: ")
while sprawdz_czy_liczba(imie):
    imie = input("Podaj poprawne imię (nie może być liczba): ")

wiek = input("Podaj swój wiek: ")
while not sprawdz_czy_liczba(wiek):
    wiek = input("Podaj poprawny wiek (musi być liczbą): ")

kraj = input("Podaj aktualny kraj zamieszkania: ")
while sprawdz_czy_liczba(kraj):
    kraj = input("Podaj poprawny kraj zamieszkania (nie może być liczba): ")

zawod = input("Podaj swój zawód: ")
while sprawdz_czy_liczba(zawod):
    zawod = input("Podaj poprawny zawód (nie może być liczba): ")

osoba = Osoba(plec, imie, wiek, kraj, zawod)
osoba.przedstaw_sie()
