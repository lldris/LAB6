#klassen---------------------------------------------------------------------------
class Student:

    def __init__(self, namn, efternamn, personnr):
        self.förnamn = namn
        self.efternamn = efternamn
        self.personnr = personnr
        
    def __str__(self):
        return f"Namn: {self.förnamn} {self.efternamn} Personnr: {self.personnr}"

    def lista_införing(self, u_lista, n_lista, konstant): #inför information om den nya studenten både till listan och filen
        n_lista[konstant] += 1  #uppdaterar ID nummer räkningen
        nytt_tal = int(n_lista[konstant]) 
        
        print(f"Studenten har ID: {nytt_tal}")
        u_lista[nytt_tal] = Student(self.förnamn, self.efternamn, self.personnr) #tilldelar en unik ID (nytt_tal) till nya elever och sparar dem
        
        #fil införing
        fil = open("students.txt", "a", encoding="utf-8") #skriver i students.txt by default, har därför inte med en parameter
        fil.write(f"\n{self.personnr}\n{self.efternamn}\n{self.förnamn}") 
        fil.close()

    def ändra_student(self, val0, u_lista):
        print(f"Här är studenten som ska ändras, {u_lista[val0]}")
        print("Vad vill du ändra?")
        print("1. förnamn\n2. efternamn\n3. personnummer")
        val = int(input("skriv valet här: "))
        if val == 1:
            ny_namn = input("ändra till: ")
            u_lista[val0] = Student(ny_namn, self.efternamn, self.personnr)
        elif val == 2:
            ny_efternamn = input("ändra till: ")
            u_lista[val0] = Student(self.förnamn, ny_efternamn, self.personnr)
        elif val == 3:
            ny_personnr = personnr_hanteraren() #kallar på funktionen som tar input för personnr samt hanterar felhantering
            u_lista[val0] = Student(self.förnamn, self.efternamn, ny_personnr)
        else:
            print("välj en siffra från 1-3")
        print("Student ändrad!")
     
#hantering av studenter och listor------------------------------------------------
def skapa_student(): 
    förnamn = input("Vad är studentens förnamn? ")
    efternamn = input("Vad är personens efternamn? ")
    personnr = personnr_hanteraren() 
    
    print("Student skapad!")
    return  Student(förnamn, efternamn, personnr)

def personnr_hanteraren():
    while True:
        try:
            personnr = int(input("Vad är studentens personnummer? "))
            if len(str(personnr)) != 12:
                print("Personnr ska vara 12 siffror")
            else: 
                return personnr
                #break
        except ValueError:
            print("Fel datatyp, använd endast siffror i heltal")
            
#kommenterad kod nedan funkar ej
'''    
def id_felhantering(prompt: int):
    while True:
        try:
            prompt
            break
        except KeyError:
            print(f"Student med ID-nummer {prompt} finns inte")
        except ValueError:
            print("Fel datatyp, använd endast siffror i heltal")

def söka_elev(u_lista): 
    prompt = int(input("Skriv in studentens ID-nummer: "))
    id_felhantering(prompt)
    print(u_lista[prompt])

def ta_bort_student(u_lista):
    prompt = int(input("Skriv ID-nummer för den student du vill ta bort: "))
    print(f"Studenten, {u_lista[prompt]}, togs bort")
    u_lista.pop(prompt)

'''
def söka_elev(u_lista): #funkar
    while True:
        try:
            välj_elev = int(input("Skriv in studentens ID-nummer: "))
            print(u_lista[välj_elev])
            break
        except KeyError:
            print(f"Student med ID-nummer {välj_elev} finns inte")
        except ValueError:
            print("Fel datatyp, använd endast siffror i heltal")
            
def ta_bort_student(u_lista): #används inte än
    while True:
        try:
            skriv_nummer = int(input("Skriv ID-nummer för den student du vill ta bort: "))
            print(f"Studenten, {u_lista[skriv_nummer]}, togs bort")
            u_lista.pop(skriv_nummer)
            
            break
        except KeyError:
            print(f"Student med ID-nummer {skriv_nummer} finns inte")
        except ValueError:
            print("Fel datatyp, använd endast siffror i heltal")

def visa_studenter(u_lista):
    print("Här är alla studenter:")
    for id in u_lista:
        print(f"[ID: {id}] {u_lista[id]}")
    pass

def antalet_elever(n_lista):
    print(f"Den här skolan har {n_lista.keys}")

def tillbaka():
    while True:
        val = input("Tillbaka till huvudmenyn? (ja/nej) ")
        if val == "ja":
            return True #ger upphov till continue i main()
        elif val == "nej": #behöver nästan 2 break efter varandra, för att koden ger samma sak som ja
            print("Tack, vi ses nästa gång.")
            return False #ger upphov till break i main()
        else:
            print("svara med ja eller nej") 

def meny():
        print("\nVälkommen till skolans databas\n")
        print("1. Skapa en ny student")
        #print("2. Sök efter en student") #går inte nu när vi hanterar filer
        print("3. Se alla studenter")
        #print("4. Ta bort en student")
        #print("5. Ändra en student") 
        while True:
            try:
                val = float(input("\nVad vill du göra? "))
                return val
            except ValueError:
                print("Fel datatyp, skriv ett av siffrorna i menyn")
                
