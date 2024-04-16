#questao 5

tam = 6

vetor= [int] * tam
inverso = [int] * tam

for i in range(len(vetor)):
    num = int(input("Digite um número: "))
    vetor[i] = num

for l in range(len(inverso)):
    inverso[l] = vetor[i]
    i = i - 1

print("A ordem inversa é:")
for p in range(len(inverso)):
    print(inverso[p])