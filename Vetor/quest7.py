#Faça um procedimento que peça a idade e a altura de 5 pessoas, armazene cada informação no
#seu respectivo vetor. Imprima a media das idades, a media das alturas, o mais novo, o mais velho,
#o mais alto e mais baixo.

tam = 2

vetor_idade = [int] * tam
vetor_altura = [float] * tam


def maior_idade(vetor_idade):
    maior_idade = vetor_idade[0]
    for i in range(1, len(vetor_idade)):
        if vetor_idade[i] > maior_idade:
            maior_idade = vetor_idade[i]
    return maior_idade

def menor_idade(vetor_idade):
    menor_idade = vetor_idade[0]
    for i in range(1, len(vetor_idade)):
        if vetor_idade[i] < menor_idade:
            menor_idade = vetor_idade[i]
    return menor_idade

def media_vetor(vetor):
    soma = 0
    tamanho = len(vetor)
    for i in range(tamanho):
        soma += vetor[i]
    media = soma / tamanho
    return media

for i in range(len(vetor_idade)):
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    vetor_idade[i] = idade
    vetor_altura[i] = altura

print(f'A maior idade obtida foi: {maior_idade(vetor_idade)}')
print(f'A menor idade foi: {menor_idade(vetor_idade)}')
print(f'A média das idades é: {media_vetor(vetor_idade)}')
print(f'A média das alturas é: {media_vetor(vetor_altura)}')