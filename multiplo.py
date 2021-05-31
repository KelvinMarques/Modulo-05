

def multiplo(n1):
    palavra = ""
    if n1 % 5 == 0 and  n1 % 7 != 0:
        palavra = "Fizz"
        print("Fizz")
    elif n1 % 7 == 0 and  n1 % 5 != 0:
        palavra = "buzz"
        print("buzz")
    elif  n1 % 5 == 0 and  n1 % 7 == 0:
        print("Fizzbuzz")
        palavra = "Fizzbuzz"
    return palavra

