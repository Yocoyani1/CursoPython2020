while True:
    print("\n------------------------------------------")
    print("\tMenú")
    print("1)Suma")
    print("2)Resta")
    print("3)Multiplicar")
    print("4)Dividir")
    print("5)Salir")

    decision = int(input("-> "))

    if decision == 5:
        break

    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))

    if decision == 1:
        print("Resultado: "+str(num1+num2))
    elif decision == 2:
        print("Resultado: "+str(num1-num2))
    elif decision == 3:
        print("Resultado: "+str(num1*num2))
    elif decision == 4:        
        while True:
            if num2 == 0:
                print("Número 2 debe ser diferente de 0\n Intenta de nuevo")
                num2 = int(input("Número 2: "))
                continue
            break
        print("Resultado: "+str(num1/num2))
 		
print("Adiós.........")