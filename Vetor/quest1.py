#questão 1

vetor = [1,2,4,16,32,64,-128]

maior = 0
menor = 0

for i in range(len(vetor)):
    if i == 0:
        maior = vetor[i]
        menor = vetor[i]
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]

for f in range(len(vetor)):
    print(vetor[f])

print("O maior número é: ", maior)
print("O menor número é: ", menor)
