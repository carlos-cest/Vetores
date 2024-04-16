#questão 3

tam = 10

vetor = [float] * tam
vetor2 = [float] * tam

def inserir():
    for i in range(len(vetor)):
        num = float(input("digite um número: "))
        vetor[i] = num

def quadrado():
    for l in range(len(vetor)):
        vetor2[l] = vetor[l] ** 2 
    return vetor2

inserir()
quadrado()
print("O quadrado do vetor é: ")

for n in range(len(vetor2)):
    print(vetor2[n])
