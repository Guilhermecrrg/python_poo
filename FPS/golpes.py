from abc import ABC, abstractmethod 
from jogador import Jogador

class Golpe(ABC):

    @abstractmethod
    def golpear(self, j: Jogador):
        pass

class Soco(Golpe):

    def golpear(self, j: Jogador):
        j.energia -= 1

class Chute(Golpe):

    def golpear(self, j: Jogador):
        j.energia -= 2