'''
Tarefa
Dado o preço da refeição (custo base de uma refeição),
a porcentagem da gorjeta (a porcentagem do preço da refeição sendo adicionada como gorjeta),
e a porcentagem do imposto (a porcentagem do preço da refeição sendo adicionada como imposto),
para uma refeição, localize e imprima o custo total da refeição . Arredonde o resultado para o número inteiro mais próximo.

Example

meal_cost = 100
tip_percent = 15
tax_percent = 8

Uma gorjeta de 15% * 100 = 15 e os impostos são 8% * 100 = 8. Imprima o valor 123 e retornar da função.

Descrição da funcão

Complete a função resolver no editor abaixo.


resolve tem os seguintes parâmetros:

    int meal_cost: o custo da comida antes da gorjeta e impostos
    int tip_percent: a porcentagem da gorjeta
    int tax_percent: a porcentagem de imposto
Retorna A função não retorna nada. Imprime o valor calculado, arredondado para o número inteiro mais próximo.

Nota: Certifique-se de usar valores precisos para seus cálculos, ou você pode acabar com um resultado arredondado incorretamente.

Formato de entrada

Existem 3 linhas de entrada numérica:
a primeira linha tem um duplo, meal_cost(o custo da refeição antes de impostos e gorjeta).
A segunda linha tem um número inteiro, tip_percent(a porcentagem de sendo adicionado como dica).
A terceira linha tem um número inteiro, tax_percent(a porcentagem de  sendo adicionado como imposto).

Amostra de entrada

12.00
20
8

Saida de amostra

15

'''
import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):

    total_cost = meal_cost + meal_cost * tip_percent/100 + meal_cost * tax_percent/100
    print(round(total_cost))

   
    if __name__ == '__main__':
        meal_cost = float(input())

        tip_percent = int(input())

        tax_percent = int(input())

        solve(meal_cost, tip_percent, tax_percent)

solve(12.00,20,8)        

            

