from golpes import *
from armas import * 
from typing import List

class Jogador:

    energia : float
    arma: List[Arma]

    def __init__(self):
        self.energia = 150
        self.arma: List[Arma] = []

    def atirar(self, d: Disparavel, j):
        d.disparar(j)

    def municiar(self, d: Disparavel):
        d.recarregar()

    def bater(self, j, golpe: Golpe = None, arma: Arma = None):
        if (golpe != None and arma == None):
            golpe.golpear(j)
        elif (golpe == None and arma != None):
            arma.agredir(j)

    def __str__(self):
        info = f'Vida do jodador = {self.energia}'
        return info
    

    

