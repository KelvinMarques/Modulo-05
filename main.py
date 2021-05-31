
import multiplo

aux = 1
while(aux == 1):

    numero = int(input("Digite um numero natural: "))

    if numero < 0:
        print("Numero negativo não é permitido")
    else:
        saida = multiplo(numero)
        aux = int(input("\n0 para sair | 1 para novo numero"))

print("\nUltima palavra que foi chamada: ", saida)
print("\nPrograma Multiplo finalizado")