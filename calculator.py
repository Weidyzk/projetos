print ("=== Calculadora Simples ===")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print ("Escolha a operação: ")
print ("1 - soma(+)")
print ("2 - subtração(-)")
print ("3 - multiplicação(*)")
print ("4 - divisão(/)")
opcao = input("Digite o número da operação: ")

if opcao == "1":
    resultado = numero1 + numero2
elif opcao == "2": 
    resultado = numero1 - numero2
elif opcao == "3":
    resultado = numero1 * numero2
elif opcao == "4": 
    resultado = numero1 / numero2
else:
    resultado ("opcão inválida!")

print ("Resultado: ", resultado)
