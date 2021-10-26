'''
Tarefa

Complete o código no editor abaixo. As variáveis i, d , e s já estão declarados e inicializados para você. Você deve:

1. Declarar 3 variáveis: uma do tipo int , uma do tipo double e uma do tipo String .
2. Leitura 3 linhas de entrada de stdin (de acordo com a sequência fornecida na seção Formato de entrada abaixo) e inicialize seu 3 variáveis.
3. Use o + operador para realizar as seguintes operações:
    1. Imprima a soma i de  mais sua variável int em uma nova linha.
    2. Imprima a soma d de  mais sua variável dupla em uma escala de uma casa decimal em uma nova linha.
    3. Concatenar s com a string que você lê como entrada e imprime o resultado em uma nova linha.

Nota: Se você estiver usando um idioma que não suporta o usopara concatenação de strings (por exemplo: C),
você pode apenas imprimir uma variável imediatamente após a outra na mesma linha.
A string fornecida em seu editor deve ser impressa primeiro, seguida imediatamente pela string que você leu como entrada.

Formato de entrada

A primeira linha contém um inteiro que você deve somar i.
A segunda linha contém um duplo que você deve somar d.
A terceira linha contém uma string que você deve concatenar com s.

Formato de saída

Imprime a soma de ambos os inteiros na primeira linha, a soma de ambos os pares (dimensionado para 1 casa decimal)
na segunda linha e, em seguida, as duas strings concatenadas na terceira linha.

Amostra de entrada

12
4.0
is the best place to learn and practice coding!

Saida de amostra

16
8.0
HackerRank is the best place to learn and practice coding!

Explicação

Quando somamos os inteiros 4 e 12 , obtemos o inteiro 16.
Quando somamos os números de ponto flutuante 4.0 e 4.0, Nós temos 8.0.
Quando concatenamos HackerRank com is the best place to learn and practice coding!,
obtemos HackerRank is the best place to learn and practice coding!.

Você não passará neste desafio se tentar atribuir os valores do Caso de Amostra às suas variáveis,
​​em vez de seguir as instruções acima e ler a entrada de stdin.

'''
i = 4
d = 4.0
s = 'HackerRank '

a = 12
b = 4.0
c = 'is the best place to learn and practice coding!'

print(i + a)
print(d + b)
print(s + c)
