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
        

def fag():
    
    preco_etanol = float(input("Digite o preço do Etanol: "))
    preco_gasolina = float(input("Digite o preço da Gasolina: "))
    
    
    
    km_gasolina = float(input("Digite o consumo do seu carro com Gasolina (Km/l): "))
    km_etanol = float(input("Digite o consumo do seu carro com Etanol (Km/l): "))

    custo_gasolina = preco_gasolina / km_gasolina
    custo_etanol = preco_etanol / km_etanol


    formula = preco_etanol / preco_gasolina 

    print(f"O custo por Km rodado com  Gasolina será:{custo_gasolina:.3f}.")
    print(f"O custo por KM rodado com Etanol será:{custo_etanol:.3f}.") 
    
    print(f"O Etanol corresponde a {formula:.2f}% do preço da Gasolina.")

    if custo_etanol < custo_gasolina:
        print ("Etanol é a melhor opção!")

    elif custo_gasolina < custo_etanol:
        print ("Gasolina é a melhor opção!")
   
    else:
        print ("Os dois combustíveis tem o mesmo custo!")
       



def promocao_3_por_1():
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade de produtos: "))

    grupos = quantidade // 3
    restantes = quantidade % 3

    total_sem_promocao = quantidade * preco
    total_com_promocao = (grupos * preco) + (restantes * preco)

    economia = total_sem_promocao - total_com_promocao

    print(f"\nQuantidade de produtos: {quantidade}")
    print(f"Valor unitário: R$ {preco:.2f}")
    print(f"Total sem promoção: R$ {total_sem_promocao:.2f}")
    print(f"Total a pagar: R$ {total_com_promocao:.2f}")
    print(f"Você economizou R$ {economia:.2f}!")


def imc():
    
    altura = float(input("Digite sua altura (m): "))
    peso = float(input("Digite seu peso (kg): "))

    resultado = peso / (altura ** 2)

    print(f"\nSeu IMC é {resultado:.2f}")

    if resultado < 18.5:
        print("Classificação: Abaixo do peso")
    
    elif resultado <= 24.9:
        print("Classificação: Peso normal")
    
    elif resultado <= 29.9:
        print("Classificação: Sobrepeso")
    
    elif resultado <= 34.9:
        print("Classificação: Obesidade grau I")
    
    elif resultado <= 39.9:
        print("Classificação: Obesidade grau II")
    
    else:
        print("Classificação: Obesidade grau III (mórbida)")



def mostrar_menu():
    
    print("\n  == Menu Calculadora ==  ")
    print("\n  1. - Divisão\n  2. - Multiplicação\n  3. - Subtração\n  4. - Soma\n  5. - Compensa etanol ou gasolina\n  6. - Calcular promoções 3 por 1 \n  7. - Calcular IMC \n  8. - Sair")
   


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
                fag()
               
            elif operacao == 6:
                promocao_3_por_1()

            elif operacao == 7:
                imc()

            
            elif operacao == 8:
                print("Até breve !")
                break
    
            else:
                print("Opção inválida, tente novamente !")
        
        except ValueError:
            print("Apenas números são aceitos, tente novamente !")

main()


