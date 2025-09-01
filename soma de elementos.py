numeros = []
for i in range(5):
    numb = float(input(f"digite o número{i+1}: "))
    numeros.append (numb)

total = sum(numeros)

print (f"A soma de todos os números é: {total}")