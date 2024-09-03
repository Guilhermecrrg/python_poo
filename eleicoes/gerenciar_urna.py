from common import *
from eleicao import Urna

def menu_urna():
    print("1- Iniciar urna")
    print("2- Contabilizar voto")
    print("3- Exibir infos urna e finalizar")
    print("4- Sair")
    op = int(input("Digite uma opção entre [1,2,3,4]:"))
    return op

def iniciar_urna(eleitores, candidatos):
    print("Iniciando Urna")
    print("==============")
    secao = int(input("Número da secao: "))
    zona = int(input("Número da zona: "))

    nome_mes = input("Nome do Mesario: ")
    rg_mes = input("RG do Mesario: ")
    cpf_mes = input("CPF do Mesario: ")

    mesario = Pessoa(nome_mes, rg_mes, cpf_mes)

    return Urna(mesario, secao, zona, candidatos, eleitores)

def votar(urna : Urna):
    titulo_eleitor = int(input("Digite o titulo do eleitor: "))
    eleitor = urna.get_eleitor(titulo_eleitor)

    if not eleitor:
        raise Exception("Eleitor não é desta Urna")

    print(eleitor)
    print("Pode votar!")
    print("===========")
    voto = int(input("Digite o numero do candidato: "))
    urna.registrar_voto(eleitor, voto)