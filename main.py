from student_class3 import Student as s
from student_class3 import *
from Lab5_2 import *
from Lab6 import*

#gör felhantering en definiion som rerturnerar break


def main():
    nummer_lista = {"n": 0} #id nummer räknaren, där 
    nyckel = "n" #konstanten
    sko = Skolor()
    
    while True:
        print("\x1bc")
        val0 = meny()
        if val0 == 1:
            person = skapa_student()
            s.lista_införing(person, sko.id_lista, nummer_lista, nyckel)
            
            while True:
                val1 = input("Vill du lägga till en student (ja/nej) ")
                if val1 == "ja":
                    person2 = skapa_student()
                    s.lista_införing(person2, sko.id_lista, nummer_lista, nyckel)
                elif val1 == "nej":
                    break
                else:
                    print("Svara med ja eller nej")
            
            val2 = tillbaka()
            if val2 == True:
                continue
            else:
                break
        
        elif val0 == 2:
            söka_elev(sko.id_lista)
            
            val3 = tillbaka()
            if val3 == True:
                continue
            else:
                break
            
        elif val0 == 3:
            #visa_studenter(sko.id_lista)
            se_studenter()
            
            val4 = tillbaka()
            if val4 == True:
                continue
            else:
                break

        elif val0 == 4:
            ta_bort_student(sko.id_lista)
            
            val5 = tillbaka()
            if val5 == True:
                continue
            else:
                break
            
        elif val0 == 5:
            person_id = int(input("Skriv ID till den student du vill ändra: "))
            person = sko.id_lista[person_id]
            s.ändra_student(person, person_id, sko.id_lista)
            
            val6 = tillbaka()
            if val6 == True:
                continue
            else:
                break
    
    
        #elif val0 == 10: #test för att se vilka om allt sparas på rätt sätt, vilket det för tillfället inte gör
        #    studenter(id_lista)
            
        else:
            print("svara med siffror mellan 0 och 4")

    print(f"-[{nummer_lista[nyckel]}]-") #lite info för programmeraren hur långt id_nummer räkningen har gått om det går bra

main()