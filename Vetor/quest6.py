#questão 6

tam = 5

vetor = [int] * tam

soma = 0
mult = 0

for i in range(len(vetor)):
    vetor[i] = int(input("digite um número: "))
    if i == 0:
        mult = vetor[i]
    soma += vetor[i] 
    mult *= vetor[i]

print('A soma dos numeros é: ', soma)
print('A multiplicação dos numeros é: ', mult)

print("---Vetor---")
for l in range(len(vetor)):
    print(vetor[l])