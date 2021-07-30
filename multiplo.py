def multiplo(numero1):
    """
    Função pra multiplicar
    """
    palavra = ""
    if numero1 % 5 == 0 and  numero1 % 7 != 0:
        palavra = "Fizz"
        print("Fizz")
    elif numero1 % 7 == 0 and  numero1 % 5 != 0:
        palavra = "buzz"
        print("buzz")
    elif  numero1 % 5 == 0 and  numero1 % 7 == 0:
        print("Fizzbuzz")
        palavra = "Fizzbuzz"
    return palavra
