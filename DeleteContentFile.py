def stergere(s):
    if text == "d":
        a_file = open("file_3.txt", "w")
        a_file.truncate()
        a_file.close()
        print("Fisierul este gol.")
    elif text == "c":
        print("Stergerea a fost anulata.")
    return s

text =input("Apasa tasta 'd' pentru a STERGERE continutul fisierului \nSau 'c' pentru CANCEL : ")