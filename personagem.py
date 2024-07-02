

class Personagem():
    
    def __init__(self, id, nome, raca, classe, nivel):
        self.__id = id
        self.__nome = nome
        self.__raca = raca
        self.__classe = classe
        self.__nivel = nivel

    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca

    @property
    def classe(self):
        return self.__classe
    
    @property
    def nivel(self):
        return self.__nivel

    def __str__(self):
        return f'<Personagem {self.__id} | {self.__nome} | {self.__raca} | {self.__classe} | {self.__nivel}>'

