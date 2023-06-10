class Zwierze:
    def __init__(self, rodzaj, rasa, wiek, imie):
        self.rodzaj = rodzaj
        self.rasa = rasa
        self.wiek = wiek
        self.imie = imie

    def przedstaw_sie(self):
        print(f"Nazywa się {self.imie} i jest to {self.rodzaj} {self.rasa}")
        print(f"Jest w wieku {self.wiek} lat.")


def sprawdz_czy_liczba(wartosc):
    try:
        int(wartosc)
        return True
    except ValueError:
        return False


rodzaj = input("Podaj rodzaj zwierzęcia: ")
while sprawdz_czy_liczba(rodzaj):
    rodzaj = input("Podaj poprawny rodzaj zwierzęcia (nie może być liczba): ")

rasa = input("Podaj rasę zwierzęcia: ")
while sprawdz_czy_liczba(rasa):
    rasa = input("Podaj poprawną rasę zwierzęcia (nie może być liczba): ")

imie = input("Podaj imię zwierzaka: ")
while sprawdz_czy_liczba(imie):
    imie = input("Podaj poprawne imię zwierzaka (nie może być liczba): ")

wiek = input("Podaj wiek zwierzęcia: ")

zwierze = Zwierze(rodzaj, rasa, wiek, imie)
zwierze.przedstaw_sie()
