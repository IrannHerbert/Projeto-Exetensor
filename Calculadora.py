           
def dividir():
        
    n1 = float(input("Informe o valor que será dividido: "))
    n2 = float(input("Informe o valor pelo qual o número será dividido: "))
        
    if n2 == 0:
        print("Impossivel dividir por 0")
        
    else:
        resultado_divisao = n1 / n2
        print(f"O resultado da sua divisão será: {n1 / n2}")
    
    
def multiplicar():
        
    n1 = float(input("Informe o valor que será dividido: "))
    n2 = float(input("Informe o valor pelo qual o núro será multiplicado: "))

    print(f"O resultado da sua multiplicação será: {n1 * n2}")

    
def subtrair():
        
    n1 = float(input("Informe o valor do qual será subtraido: "))
    n2 = float(input("Informe o valor que será subtraido: "))
       
    print(f"O resultado da sua subtração será: {n1 - n2}")
    
def soma():
        
    n1 = float(input(f"Informe um valor para soma:  "))
    n2 = float(input(f"Informe o segundo valor para a soma: "))

    print(f"O resultado da sua soma será: {n1 + n2}")
        

        
def mostrar_menu():
    
    print("\n  == Menu Calculadora ==  ")
    print("\n  1.Divisão\n  2.Multiplicação\n  3.Subtração\n  4.Soma\n  5.Sair")
   


    
while True:
    mostrar_menu ()
   
    operaçao = int(input("Escolha uma operação: "))

    if operaçao == 1:
        dividir()

    elif operaçao == 2:
        multiplicar()
    
    elif operaçao == 3:
        subtrair()

    elif operaçao == 4:
        soma()

    elif operaçao == 5:
        print("Até breve !")
        break
    
    else:
        print("Opção invalida, tente novamente outra opção !")


