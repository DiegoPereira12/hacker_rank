'''
Dado um número inteiro,, execute as seguintes ações condicionais:

Se  n é estranho imprimir Weird
Se  n é uniforme e está na faixa inclusiva de 2 para 5, imprimir Not Weird
Se  n é uniforme e está na faixa inclusiva de 6 para 20, imprimir Weird
Se  n é igual e maior do que 20, imprimir Not Weird
Complete o código stub fornecido em seu editor para imprimir ou não  é estranho.

Formato de entrada

Uma única linha contendo um número inteiro positivo, n.

Formato de saída

Imprima Weirdse o número for estranho; caso contrário, imprima Not Weird.

Amostra de entrada 0

3

Sample Output 0

Weird

Amostra de entrada 1

24

Saída de amostra 1

Not Weird

'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N == 1:
        print('Weird')
    elif N >= 2 and N <=5:
        print('Not Weird')
    elif N >= 6 and N <= 20:
        print('Weird')
    elif N > 20:
        print('Not Weird')