import student_class3 as c

def fil_val():
    val = input("Vad heter filen med alla studenter? ")
    return f"{val}"

def se_studenter():
    while True:
        try:
            fil = fil_val()
            filen = open(fil, "r", encoding="utf-8")
            break
        except FileNotFoundError:
            print("Den filen fanns inte!")

    print("\nHär är alla studenter i KTH:\n")
    personnr = filen.readline().strip()
    while personnr != "":
        efternamn = filen.readline().strip()
        förnamn = filen.readline().strip()
        print(c.Student(förnamn, efternamn, personnr)) #skriver in fil, får ut studenter med strängen från Student klassen
        personnr = filen.readline().strip()
    filen.close()


#def skriv_till_fil(u_lista):
#    fil = fil_val()
#    with open(fil, 'w', encoding= 'utf-8') as f:
#        for student in u_lista:
#            f.write(f"{student.personnummer}\n{student.efternamn}\n{student.förnamn}\n")