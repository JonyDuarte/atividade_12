"""Crie um programa que calcule a área de uma das figuras geométricas abaixo:

- Quadrado
- Triângulo
- Círculo
- Trapézio

O usuário deverá escolher qual figura geométrica deseja calcular a área, e deverá informar as medidas da figura.

Obs: utilize o conceito de lambdas para realizar os cálculos."""
import time
import math
import os


area_quadrado = lambda lado: lado ** 2
area_triangulo = lambda base, altura: base * altura /2
area_circulo = lambda raio: math.pi * raio ** 2
area_trapezio = lambda base1, base2, altura: ((base1 + base2) * altura) / 2 

print("Programa que calcula a área de figuras geométricas")

time.sleep(3.0)

os.system("cls")

print('''Escolha uma das figuras geométricas abaixo:
        [1] Quadrado
        [2] Triângulo  
        [3] Círculo
        [4] Trapézio
        [5] Sair do programa \n''')

time.sleep(1.5)

opcao = int(input("Digite sua opção: "))
os.system("cls")


try:

            if opcao == 1:
                    lado = float(input("Informe o valor do lado do quadrado: ").replace(",","."))
                    area = area_quadrado(lado)
                    print(f"A área do quadrado é: {area}")
                    time.sleep(0.5)
                    
                    
                  
            elif opcao == 2:
                    base = float(input("Informe o valor da base do triângulo: ").replace(",","."))
                    altura = float(input("Informe o valor da altura do trinângulo: ").replace(",","."))
                    area = area_triangulo(base, altura)
                    print(f"A área do triângulo é {area}")
                    time.sleep(0.5)
                    
                    

            elif opcao == 3:
                    raio = float(input("Informe o valor do raio do círculo:  ").replace(",","."))
                    area = area_circulo(raio)
                    print(f"A área do círculo é {area}")
                    time.sleep(0.5)
                    

            elif opcao == 4:
                    base1 = float(input("Informe o valor da primeira base do trapézio: ").replace(",","."))
                    base2 = float(input("Informe o valor da segunda base do trapézio: ").replace(",","."))
                    altura = float(input("Informe o valor da altura do trapézio: ").replace(",","."))
                    area = area_trapezio(base1, base2, altura)
                    print(f"A área do trapézio é: {area}")
                    time.sleep(0.5)
                    

            elif opcao == 5:
                        print("Saindo do programa....")
                        time.sleep(0.5)
                        
                        
            else:
                ...

except Exception as e:
        print("Erro! Tente novamente. {e}.")

time.sleep(0.5)

print("Fim do programa!")

        


        


