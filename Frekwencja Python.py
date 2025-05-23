from datetime import datetime

def main():
    courses = {}

    while True:
        print("\n1. Dodaj kurs\n2. Dodaj studenta na kurs\n3. Dodaj ocenę\n4. Dodaj frekwencję\n5. Pokaż raporty\n6. Koniec")
        choice = input("Wybierz: ")

        if choice == "1":
            name = input("Nazwa kursu: ").strip()
            if name and name not in courses:
                courses[name] = {"students": {}}
                print("Dodano kurs.")
        elif choice == "2":
            name = input("Nazwa kursu: ").strip()
            if name in courses:
                sname = input("Imię i nazwisko studenta: ").strip()
                if sname:
                    courses[name]["students"][sname] = {"grades": [], "attendance": []}
                    print("Dodano studenta.")
        elif choice == "3":
            name = input("Nazwa kursu: ").strip()
            if name in courses:
                sname = input("Imię studenta: ").strip()
                if sname in courses[name]["students"]:
                    try:
                        grade = float(input("Ocena: "))
                        courses[name]["students"][sname]["grades"].append(grade)
                        print("Dodano ocenę.")
                    except ValueError:
                        print("Niepoprawna ocena.")
        elif choice == "4":
            name = input("Nazwa kursu: ").strip()
            if name in courses:
                sname = input("Imię studenta: ").strip()
                if sname in courses[name]["students"]:
                    present = input("Obecny? (t/n): ").strip().lower() == 't'
                    courses[name]["students"][sname]["attendance"].append((present, datetime.now()))
                    print("Dodano frekwencję.")
        elif choice == "5":
            name = input("Nazwa kursu: ").strip()
            if name in courses:
                print(f"Oceny dla {name}:")
                for s, data in courses[name]["students"].items():
                    grades = data["grades"]
                    if grades:
                        avg = sum(grades)/len(grades)
                        print(f"{s}: {grades} (Śr: {avg:.2f})")
                    else:
                        print(f"{s}: brak ocen")
                print(f"Frekwencja dla {name}:")
                for s, data in courses[name]["students"].items():
                    total = len(data["attendance"])
                    present = sum(1 for a, _ in data["attendance"] if a)
                    print(f"{s}: {present}/{total} obecności")
        elif choice == "6":
            print("Koniec programu.")
            break
        else:
            print("Nieznana opcja.")

if __name__ == "__main__":
    main()
