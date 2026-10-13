

f = open("Getdata/uczniowie.txt","r",encoding="utf-8")
uczniowie = f.read().splitlines()
f.close()
while True:
    print("Menu")
    print("1 Wyswietl liste")
    print("2 Posortuj")
    print("3 usun ucznia")
    print("Zakoncz program")
    wyb = int(input("Wybierz opcje"))


    match wyb:
        case 1:
            numer = 1
            for uczen in uczniowie:
                print(numer,uczen)
                numer= numer + 1
        case 2:
            uczniowie.sort()
        case 3:
            nr = int(input("Wybierz numer ucznia"))
            uczniowie.pop(nr- 1)
        case 4:
            break