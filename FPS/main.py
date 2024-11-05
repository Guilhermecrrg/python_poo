from jogador import Jogador
from golpes import *
from armas import *

if __name__ == '__main__':
    j1 = Jogador()
    j2 = Jogador()
    soco = Soco()
    chute = Chute()
    faca = Faca()
    socoIngles = Soco_Ingles()
    revolvi = Revolver()
    lancaChamas = Lanca_Chamas()
    
    j1.arma.append(revolvi)
    j1.atirar(j1.arma[0],j2)
    print(j2)