"""
Seguindo o PEP8
Link: https://www.python.org/dev/peps/pep-0008/

Tentativa de fazer resumo do PEP8

Objetivo:
Deixar o code mais legivel e facil de enteder

Sao regras sobre legibilidade do code, porem nao precisam ser siguidas
a risca, somente o que for possivel implementar 
"""

"""
Um guia de estilo é sobre consistência.
A consistência com este guia de estilo é importante.
A consistência dentro de um projeto é mais importante.
A consistência dentro de um módulo ou função é a mais importante.

Caso for modificar a forma atual, padronize ou nao mexa no estilo.
"""

#Identacao -> 4 espacos sao o padrao -> Regra opcional 

"""
Ex de identacao com .... como 4 espacos 
teste = [
....1,2,3,4,5,
....3,4,5,6,6,
....1,3,4,5,6
....]
"""

"""
#Evite quebrar os valores de forma imprecisa
teste = [1,2,3,4,5,3,4,5,
    6,6,
    1,3,4,5,6
    ]

#Deixe dessa forma
teste = [
    1,2,3,4,5,
    3,4,5,6,6,
    1,3,4,5,6
    ]
"""

"""
Esse a identacao abaixo para [], () e {}
Pelo menos a forma 
"""
teste = [
    1,2,3,4,5,
    3,4,5,6,6,
    1,3,4,5,6
    ]
print(teste)

"""
Quando for identar alguma coisa, uso espacos em vez de Tab
Configuracao de tab pode modificar de maquina para maquina
espacos nao
"""

"""
Limite o tamanho de suas linhas ate os possiveis 79 a 72
colunas isso facilita a abertura de varios arquivos de uma
vez sem atrapalhar a visualizacao de demais arquivos ja
abertos ou que estao sendo trabalhados naquele momento

Esta e uma regra opcional, mas que facilita a organizacao
e vizualicao dos arquivos

Formar de fazer isso e utilizando / ou [], {} e () nos locais
necessarios
"""

"""
Comentarios devem seguir de 
    * Frase completa e explicatica
    * Se muito grande ou mais de um paragrafo, quebreo em partes
    * Ao fim do comentario,  dois espacos em branco apos o comando
    * Primeira letra sempre em maiscula
    * Se possivel escreva em ingles(universal), caso tenha certeza que
    de um certo grupo na passe o code, escreve na lingua de preferencia
    
Lembre-se, comentarios que nao batem com o code sao os piores

Use comentarios com moderacao no caso de sintaxe

Quando escrever um comentario na mesma linha de code, de dois espacos
para comecar a escrever o comentario
"""

"""
Forma mais recomendada de mostrar equacoes longas,
Antes a quebra era apos o operador, dificultando a leitura,
com isso foi trocado que se quebra antes do operador,
isso facilita a visualiuzacao, pois sabemos os valores a se
trabalhar
"""

t1=1
t2=2
t3=3
t4=4
t5=5
t6=6
t7=7
valor = (t1
         +t2
         +t3
         +t4
         +t5
         +t6
         +t7
)
print(valor)

"""
Use linhas em branco de forma moderada para dividir
secoes do code.
    *Quando iniciada uma nova funcao ou objeto, de duas
    linhas de espaco em branco do code para a nova funcao
"""

"""
Use:
ASCII -> Python 2
UTF-8 -> Python 3

Use sempre que possivel, ingles para descrever areas do code,
caso os termos usados nao possam ser escritos em ingles,
utilize a linguagem local para fazer a discricao
"""

"""
Imports devem estar em linhas separadas

Sim ->
import os
import sys

Nao ->
import os, sys

Modelo absoluto de chamada -> 
So traz o que esta sendo importado da lib ->
from teste import pastel

Importacoes absolutas sao preferiveis por so trazer
o que necessita sem nada alem disso

Evite coringas nos imports
"""

"""
Dunders devem ser colocados apos a documentacao
, isso e, apos os comentarios, a unica excessao e o
__future__ que deve ser colocado antes de qualquer
outra coisa alem da documentacao

Ex:

From __future__ import barry_as_FLUFL 

__all__ = ['a', 'b', 'c'] 
__version__ = '0.1' 
__author__ = 'Cardinal Biggles' 

import os 
import sys

"""

"""
PEP nao faz recomendacoes de como arrumar array
e tuplas, essa fica por escolha do programador
"""

"""
Evite espacos em branco dentro de instrucoes

Ex:

teste[ 1 ] -> Errado
teste[1] -> Certo

Ou

teste=[1, 3, 5, 5, 4, 5, 4] -> Errado
teste=[1,2,3,4,5,6,7] -> Certo

O mesmo vale para operacoes matematicas
Ex:
(1 + 1) -> Errado
(1+1) -> Certo
"""

"""
Docstrings -> Documentacao de strings

Para todas as funcoes, metodos e classes -> Escreva comentarios para
explicar o que esta acontecendo em determinado trecho de code

Use """ ''''" para estes trechos
"""

"""
Nomenclatura

Variaveis e funcoes -> Evite o uso de I, L, O, podem ser confundidas com
outros caracteres alem de valores numericos

Use somente nomes que respeitem o ASCII e o UTF-8

CapWords -> Palavra composta

Nomes de classes devem usar CapWords

Variaveis devem ser escrita com o divisor sendo _ entre as palavras

Para a criacao de variaveis globais, so respeitar tudo acima e use
mixedCase casa necessario so para manter a compatibilidade

Para nomear uma funcao use -> Letra minuscula, _ para divisao de palavras

Use _ para nome de metodos e variaveis nao publicos

Use __  para evitar conflito de subsclasses e chamar funcoes de manipulacao
do python, o uso e para encapsulamento e para evitar conflito entre elementos
de sub-classes

contantes sao definidas em escrito em maiusculo
"""

"""
Heranca

Definida no projeto se um metodo ou variavel vai ser publico o nao
em caso de duvida, deixeo privado, e mais facil torna-lo publio que privado
dentro do projeto que o contrario

nenhuma variavel e realmente privada no python, so e mais dificil de acessar
a mesma mais que o normal
"""

"""
Interfaces publicas e internas

Insterfaces publicas devem possuir retro-compatibilidade entre determinadas
versoes, caso nao tenha, deve ser comentado que tal recurso e necessario
ou o que necessita para funcionar

Tambem deve ser comentado se esta utilizando uma API ou nao nos
determinados trechos
"""

"""
Recomendacao de programacao

Codes devem ser escritos de forma que nao prejudiquem outras implementacoes

Sempre use um def para fazer uma operacao

Use Exception quando puder para evitar problemas de continuacao

Projete uma hierarquia de acesso e controle

Use encadeamento para indicar substituicao sem perder o retorno original

Tenha tratamento para todas as excessoes

Evite returns None 
"""
