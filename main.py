import importlib

while True:
    wybor = input("Jeśli chcesz stworzyć czlowieka wpisz 'human', a jeśli chcesz stworzyć zwierzaka to wpisz 'animal'\n")

    if wybor == "animal":
        try:
            module = importlib.import_module('animal')
            module.animal()
        except ModuleNotFoundError:
            print("Wpisz jeszcze raz 'b'.")
    elif wybor == "human":
        try:
            module = importlib.import_module('human')
            module.human()
        except ModuleNotFoundError:
            print("Wpisz jeszcze raz 'b'.")
        
    wybor = input("Czy chcesz stworzyć nowego? (t/n): ")
    if wybor.lower() != "t":
        break
    