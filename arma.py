class Arma:
    def __init__(self, nombre, destruccion, resistencia):
        self.__nombre = nombre
        self.__destruccion = destruccion
        self.__resistencia = resistencia
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def destruccion(self):
        return self.__destruccion
    
    @destruccion.setter
    def destruccion(self, destruccion):
        self.__destruccion = destruccion
    
    @property
    def resistencia(self):
        return self.__resistencia
    
    @resistencia.setter
    def resistencia(self, resistencia):
        self.__resistencia = resistencia

    def __str__(self):
        return f'arma: {self.__nombre} destruccion: {self.__destruccion} resistencia:{self.__resistencia}'

    