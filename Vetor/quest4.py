#Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e
#Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá escrever a
#soma dos valores encontrados nas respectivas posições X e Y .

tam = 8

vetor = [int] * tam

for i in range(len(vetor)):
    vetor[i] = int(input("Digite um número: "))

x = int(input("Escola uma posição(0, 7): "))
y = int(input("Escola outra posição(o, 7): "))

soma = 0

for t in range(len(vetor)):
    if t == x:
        x_valor = vetor[t]
        soma += vetor[t]
    if t == y:
        y_valor = vetor[t]
        soma += vetor[t]

print("")
print(f"A soma entre X e Y é: {soma}")
print("")
print(f"Valor de x: {x_valor} valor de y: {y_valor}")