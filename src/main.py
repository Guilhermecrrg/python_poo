from frota import *

def simular_carro(carro : Carro):
    op = 0
    print("1- Ligar o motor")
    print("2- Desligar o motor")
    print("3- Acelerar")
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)
    print("\n")

if __name__ == "__main__":
    print('Cadastre o primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    print("\n")

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, motor = False)

    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    print("\n")

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, motor=False)

    '''
    Controlando 2 carros até um deles atingir 300 Km
    '''
    while carro1.odometro < 300 and carro2.odometro < 300:
        try:
            op_carro=0
            while op_carro not in (1,2):
                op_carro = int(input("Qual carro simular 1 ou 2?"))
                print("\n")

            if op_carro == 1:
                simular_carro(carro1)

            else:
                simular_carro(carro2)

        except Exception as e:
            print("Erro!")
            print(f"{e}\n")
    try:
        carro1.desligar()
        carro2.desligar()
    except Exception as e:
        print("Erro!")
        print(f"{e}\n")

    print(carro1)
    print("\n")
    print(carro2)
    print("\n")

    if carro1.odometro > 300:
        print("o Carro 1 chegou em primeiro")

    else:
        print("o Carro 2 chegou em primeiro")
