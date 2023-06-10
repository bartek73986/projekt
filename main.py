class ProgramSelector:
    def __init__(self):
        self.program = None

    def select_program(self):
        choice = input("Wybierz program (1 - animal.py, 2 - human.py): ")

        if choice == "1":
            import animal
            self.program = animal
        elif choice == "2":
            import human
            self.program = human
        else:
            print("Nieprawidłowy wybór.")

    def run_program(self):
        if self.program:
            self.program.run()
        else:
            print("Nie wybrano żadnego programu.")


if __name__ == "__main__":
    selector = ProgramSelector()
    selector.select_program()
    selector.run_program()
