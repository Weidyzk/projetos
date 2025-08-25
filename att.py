# Atividade de permissão de acesso.

idade = int (input("Digite sua idade "))
ingresso = input("Do you have ticket? ").upper()
if idade >= 18 and ingresso == "SIM": 
    print ("you have a pass.")
    
else: print ("you dont have acess.")

if idade <18: print ("Você não tem Idade!")
if ingresso != ("SIM"): print("Você não possui o acesso.")
