from datetime import date

class RecetaError(Exception):
    pass

class Ingrediente:
    def __init__(self,nome,cantidade,unidade):
        self.nome=nome               
        self.__cantidade=cantidade   
        self.unidade=unidade

    def __str__(self):
        return f"{self.nome}: {self.__cantidade} {self.unidade}"

class Plato:
    total_platos=0

    def __init__(self,nome,preparacion):
        self.nome=nome
        self.__preparacion=preparacion 
        self.__ingredientes=[]
        Plato.total_platos+=1

    def engadir_ingrediente(self,ing):
        self.__ingredientes.append(ing)

    @classmethod
    def total_creados(cls):
        return f"Platos totais: {cls.total_platos}"

    def __len__(self):
        return len(self.__ingredientes)

class MenuSemanal:
    def __init__(self,inicio,fin):
        self.data_inicio=inicio
        self.data_fin=fin
        self.__platos=[]

    @staticmethod
    def saudar():
        return "Benvido ao xestor de receitas"

    def engadir_plato(self, plato):
        self.__platos.append(plato)