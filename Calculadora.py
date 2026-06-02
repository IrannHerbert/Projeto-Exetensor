def ler_numeros():
    
    while True:
        
        try:
            n1 = float(input("Digite o primeiro valor: "))
            n2 = float(input("Digite o segundo valor: "))
        
            return n1, n2

        except ValueError:
            print("Apenas números são válidos !")


def dividir():
        
    n1, n2 = ler_numeros ()
        
    if n2 == 0:
        print(" Impossível dividir por 0 !")
        
    else:
        resultado = n1 / n2
      
        print(f" == O resultado da sua divisão será: {resultado} ==")
       
    
    
def multiplicar():
        
   n1, n2 = ler_numeros()

   resultado = n1 * n2
   
   print(f" == O resultado da sua multiplicação será: {resultado} ==")

    
def subtrair():
        
   n1, n2 = ler_numeros()

   resultado = n1 - n2

   print(f" == O resultado da sua subtração será: {resultado} ==")
    

def soma():
   
    n1, n2 = ler_numeros()

    resultado = n1 + n2

    print(f" == O resultado da sua soma será: {resultado} ==")
        

        
def mostrar_menu():
    
    print("\n  == Menu Calculadora ==  ")
    print("\n  1. - Divisão\n  2. - Multiplicação\n  3. - Subtração\n  4. - Soma\n  5. - Compensa álcool ou gasolina\n  6. - Calcular promoções 3 por 1 \n  7. - Calcular IMC \n  8. - Calcular juros compostos\n  9. - Sair")
   


def main():
    
    while True:
        mostrar_menu ()
   
        try: 
            operacao = int(input("Escolha uma operação: "))

            if operacao == 1:
                dividir()

            elif operacao == 2:
                multiplicar()
    
            elif operacao == 3:
                subtrair()

            elif operacao == 4:
                soma()

            elif operacao == 5:
                print("Esta função está em desenvolvimento. Aguarde novidades nas próximas atualizações !")
               
            elif operacao == 6:
                print("Esta função está em desenvolvimento. Aguarde novidades nas próximas atualizações !")

            elif operacao == 7:
                print("Esta função está em desenvolvimento. Aguarde novidades nas próximas atualizações !")

            elif operacao == 8:
                print("Esta função está em desenvolvimento. Aguarde novidades nas próximas atualizações !")
            
            elif operacao == 9:
                print("Até breve !")
                break
    
            else:
                print("Opção inválida, tente novamente !")
        
        except ValueError:
            print("Apenas números são aceitos, tente novamente !")

main()


