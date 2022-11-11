from time import sleep
from superheroe import Superheroe
from arma import Arma

OjodeHalcon = Superheroe("OjodeHalcon",10,5, "Americana")
Msmarvel = Superheroe("Msmarvel",10,5,"Afroamericana")
CapitanaMarvel = Superheroe("CapitanaMarvel",20,5, "Americana")
PanteraNegra = Superheroe ("PanteraNegra",10,6,"Afroamericana")


Atomo = Superheroe("Atomo",10,5,"Europeo")
Cyborg = Superheroe("Cyborg",5,5,"Europeo")
Hawkgirl= Superheroe("Hawkgirl",5,6,"Americana")
Supergirl= Superheroe("Supergirl",15,6,"Asiatica")

cuchilla = Arma("Cuchilla", 10, 2)
hoz = Arma("Hoz", 20, 2)
palo = Arma("palo", 15, 2)
piedra = Arma("piedra", 5, 3)



#Lista de Superheroes
Superheroes = [OjodeHalcon, Msmarvel, CapitanaMarvel, PanteraNegra, Atomo, Cyborg, Hawkgirl, Supergirl]
#Lista de armas
Armas = [cuchilla, hoz, palo, piedra]

#Menu
def menu():
    print("\n/////////////////MENU DC MARVEL//////////////////// ")
    print ("1.Empezar Duelo\n"
        "2.Listar Heroes\n"
        "3.Ver Heroe\n"
        "4.Salir")
    opcion = input("\nIngrese una opción: ")
    opciones(opcion)
        

#Funcion para gestionar opciones
def opciones(opcion):

    #Pescarse a combos
    if (opcion == "1"):
        print("\nElige los heroes para el duelo\n")
        
        for i in range(len(Superheroes)):
            print(f'{i+1}. {Superheroes[i].nombre}')

        heroe1 = int(input("Elige el primer heroe: "))
        if (Superheroes[heroe1-1].listaArmas() != False):
            print(f'\n{Superheroes[heroe1-1].nombre} usara su arma\n')


        heroe2 = int(input("Elige el segundo heroe: "))
        
        if (Superheroes[heroe2-1].listaArmas() != False):
            print(f'{Superheroes[heroe2-1].nombre} usara su arma')

        print(f'\n{Superheroes[heroe1-1].nombre} VS {Superheroes[heroe2-1].nombre}\n')

        pheroe = Superheroes[heroe1-1]
        sheroe = Superheroes[heroe2-1]

        contround = 0

        estado = False
        while estado != True:
            contround = contround + 1
            print("Round ", contround)

            sleep(0.85)
            if estado != True:
                print("----------------------")
                pheroe.atacar(sheroe)
                estado = sheroe.perder(pheroe)
                print("----------------------")
                
            sleep(0.7)
            if estado != True:
                print("----------------------")
                sheroe.atacar(pheroe)
                estado = pheroe.perder(sheroe)
                print("----------------------")
            
            if contround == 5:
                print("\nBono de 5 rounds")
                pheroe.aumentarataque()
                sheroe.aumentarataque()
                pheroe.recuperarsalud()
                sheroe.recuperarsalud()

            

            elif contround == 10:
                print("\nBono de 10 rounds")
                pheroe.aumentarataque()
                sheroe.aumentarataque()
                pheroe.recuperarsalud()
                sheroe.recuperarsalud()
                

        menu()
    #Aber
    elif (opcion == "2"):
        print("\nLista de Heroes\n")
        for i in range(len(Superheroes)):
            print(f'{i+1}. {Superheroes[i].nombre}')
        menu()
    #Ver heroe
    elif (opcion == "3"):

        for i in range(len(Superheroes)):
            print(f'{i+1}. {Superheroes[i].nombre}')

        heroe = int(input("\nElige el heroe: "))
        Verheroe = Superheroes[heroe-1]
        print(Verheroe.__str__())

        print("\nQuieres agregarle un arma?")
        print("1.Si\n"
            "2.No")
        decision = input("Ingrese una opción: ")

        
        if (Verheroe.listaArmas() != True):
            if (decision == "1"):
                print("\nSolo puedes elegir 1 arma para cada heroe\n")
                for i in range(len(Armas)):
                    print(f'{i+1}. {Armas[i].nombre}')

                arma = int(input("\nElige el arma: "))
                Verheroe.agregarArma(Armas[arma-1])
                print(Verheroe.__str__())
                print(Verheroe.listaArmas())
                menu()
            else:
                menu()
        else:
            print("El heroe ya tiene un arma")
            menu()




    elif (opcion == "4"):
        print("Apagando..")
        quit()




menu()