from ast import If
from pickle import FALSE
from re import T
from arma import Arma
import random
class Superheroe:
    #constructor
    def __init__(self, nombre, ataque, defensa, etnia):
        self.__nombre = nombre
        self.__salud = 100
        self.__ataque = ataque
        self.__defensa = defensa
        self.__etnia = etnia
        self.__armas = []
        

    #getter y setter
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def salud(self):
        return self.__salud
    
    @salud.setter
    def salud(self, salud):
        self.__salud = salud
    
    @property
    def ataque(self):
        return self.__ataque
    
    @ataque.setter
    def ataque(self, ataque):
        self.__ataque = ataque

    @property
    def superfuerza(self):
        return self.__superfuerza
    
    @superfuerza.setter
    def superfuerza(self, superfuerza):
        self.__superfuerza = superfuerza

    @property
    def defensa(self):
        return self.__defensa
    
    @defensa.setter
    def defensa(self, defensa):
        self.__defensa = defensa

    @property
    def etnia(self):
        return self.__etnia
    
    @etnia.setter
    def etnia(self, etnia):
        self.__etnia = etnia
    
    
    def atacar(self, heroe):
     
        esquiva = self.esquivar(heroe)

        if (esquiva != True):
            if (len(self.__armas) > 0):
                    
                    if (self.__armas[0].resistencia == 0):
                            heroe.salud -= self.__ataque
                            print(f'{heroe.nombre} ha sido atacado, su salud es de {heroe.salud}')
                    else:
                        if (self.__armas[0].resistencia > 0):

                            heroe.salud = heroe.salud - (self.__armas[0].destruccion + self.__ataque)
                            self.__armas[0].resistencia = self.__armas[0].resistencia - 1
                            print(f'{heroe.nombre} ha sido atacado, su salud es de {heroe.salud}')
                            
                            if(self.__armas[0].resistencia == 0):
                                print(f'\n----*{self.__nombre} se le rompio el arma\nProcedera a usar sus puños*----\n')

            elif ((len(self.__armas) < 1)):
                            heroe.salud -= self.__ataque
                            print(f'{heroe.nombre} ha sido atacado, su salud es de {heroe.salud}')


    def esquivar(self, heroe):
        if ( random.randint(0, 2) == 2):
            print(f'{heroe.nombre} ha esquivado el ataque de {self.__nombre}')
            return True

        
        


    def perder(self, heroe):
        if (self.__salud <= 0):
            print(f'{self.__nombre}: llevame pa la casa hmnito')
            print(f'Ganador: {heroe.nombre}')
            self.__salud = 100
            heroe.salud = 100
            return True

    def agregarArma(self, arma):
        self.__armas.append(arma)

    def listaArmas(self):
        if (len(self.__armas) >= 1):
            print("\nArmas\n")
            for i in range(len(self.__armas)):
                print(f'{i+1}. {self.__armas[i].nombre}')
            return True
        else:
            return False

    def aumentarataque(self):
        print(f'\n{self.__nombre} ha aumentado +2 de ataque\n')
        self.__ataque += 2
    
    def recuperarsalud(self):
        print(f'\n{self.__nombre} ha recuperado +20 salud\n')
        self.__salud += 20

    def __str__(self):

        return f'Superheroe: {self.__nombre}\n salud:{self.__salud}\n ataque: {self.__ataque}\n absorberEnergia: {self.__defensa}\nEtnia: {self.__etnia}'
    

