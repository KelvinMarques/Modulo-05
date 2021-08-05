from multiplo import multiplo

AUX = 1
while AUX == 1:
    """
    Entrada dos dados e execução do main
    """
    numero = int(input("Digite um numero natural: "))

    if numero < 0:
        print("Numero negativo não é permitido")
    else:
        SAIDA = multiplo(numero)
        AUX = int(input("\n0 para sair | 1 para novo numero"))

print("\nUltima palavra que foi chamada: ", SAIDA)
print("\nPrograma Multiplo finalizado")
