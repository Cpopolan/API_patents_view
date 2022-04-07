from time import sleep
def stergere():
    ask = input("Ce tip de fisier doresti sa creezi? ( txt sau csv ):\n")
    while True:
        global text
        text = input("Tasta 'd' pentru a STERGERE continutul fisierului,\nTasta 's' pentru scriere: ")
        if text.lower() == "d":
            a_file = open("patentTitles.txt", "w")
            a_file.truncate()
            a_file.close()
            print("Fisierul este gol.")
            break
        elif text.lower() == "s":
            print("Scrierea a fost efectuata.")
            break
        else:
            print("Mai incearca odata. Introdu caractere valide!")
            sleep(3)



