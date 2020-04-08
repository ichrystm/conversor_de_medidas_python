import sys
import conversor

def menu():
    print(" ")
    print(":::: Conversor de medidas ::::")
    print (" ")
    print("1. Pés para metros.")
    print("2. Polegadas para centímetros.")
    print("3. Jardas para metros.")
    print("4. Milhas para quilômetros.")
    print("5. Sair do programa.")
    print(" ")

    entry = input("Digite a opção desejada: ")
    print(" ")

    if entry == '1':
        print(" ")
        measure = float(input("Digite o valor da medida: "))
        print("Medida em metros: ", conversor.pe2metro(measure))

    elif entry == '2':
        print(" ")
        measure = float(input("Digite o valor da medida: "))
        print("Medida em centímetros: ", conversor.pol2cent(measure))
    
    elif entry == '3':
        print(" ")
        measure = float(input("Digite o valor da medida: "))
        print("Medida em metros: ", conversor.jarda2metro(measure))
    
    elif entry == '4':
        print(" ")
        measure = float(input("Digite o valor da medida: "))
        print("Medida em quilômetros: ", conversor.milhas2km(measure))

    elif entry == '5':
        sys.exit()

    else:
        print(" ")
        print("Digite uma opção válida.")
        print(" ")
        menu()
    menu()

menu()



