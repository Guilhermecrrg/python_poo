from funcionario import *

g = Gerente('Guilherme','123',123)
print(g.autenticar('123',123))
print(g.cancelar_operacao())
print(g)

op = Operador_Caixa('Pedro','1234',1234,1)
print(op.autenticar(1,1234))
print(op.registrar_produto())
print(op)

s = Seguranca('Rafael','321',321,4)
print(s.autenticar(4,321))
print(s.acionar_alarme())
print(s)