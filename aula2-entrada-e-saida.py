print("usando o print")
print("usando o print\n uso o barra n para quebrar a linha")
print("usando o print\t uso o barra t para simular o tab")

nome = 'Gabriela'

print(nome)
tipo_nome = type(nome)
idade = 1
tipo_idade = type(idade)
decimal = 1.4
tipo_decimal = type(decimal)
print(tipo_nome)
print(tipo_idade)
print(tipo_decimal)

print(idade, decimal, nome)
print(idade, "sem", decimal)

#convertendo inteiros para string
print(nome + str(idade))

#usando input - formulário
#viram objetos string
campo = input('escreva seu nome: ')
qnos = input('sua idade:')
print(type(campo), type(qnos))


numero1 = 27
numero2 = 53

resultado = numero1 + numero2
print(resultado)

quadrado = 10 ** 2
raiz = 16 **(1/2)
print(quadrado, raiz)