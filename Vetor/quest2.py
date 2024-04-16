#questão 2

vetor = [1,2,4,16,32,64,-128]

soma = 0

for i in range(len(vetor)):
    soma += vetor[i]

for f in range(len(vetor)):
    print(vetor[f])

print("A soma é igual a: ", soma)
