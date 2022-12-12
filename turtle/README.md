# Arquivos - /turtle
Pasta criada com o intuito de alocar os exercícios utilizando a biblioteca Python Turtle.
Nesta pasta é possível executar os códigos e visualizar os resultados dos exercícios

Ressalvas - Os exercícios podem ser acessados pelos links abaixo:
- [Plotting Fibonacci spiral fractal](https://www.geeksforgeeks.org/python-plotting-fibonacci-spiral-fractal-using-turtle/)
- [Y Fractal tree](https://www.geeksforgeeks.org/y-fractal-tree-in-python-using-turtle/)
- [How to make Triangles](https://www.geeksforgeeks.org/how-to-make-triangle-in-python-turtle-using-onscreenclick/)


## Requisitos

É necessário possuir instalado Python 3.8 ou maior em sua máquina, você pode instalar [aqui](https://www.python.org/downloads/).

```bash
# Mac/Linux/Windows 
python --version
```

Com Python3 configurado, configure suas variáveis de git:

```bash
# Git config (https)
git config --global user.email [seu e-mail] 
git config --global user.name [seu nickname] 
```

Clone o repositório em uma pasta vazia (recomendado) e acesse a pasta do repo


## Exercício 1 - Sequência de Fibonacci
Cada número na série representa o comprimento dos lados de um quadrado. O quadrado de lado 0 não existe. Então começamos do quadrado de lado 1. O próximo quadrado também tem lado 1. 
 
- Primeiro constrói-se dois quadrados de dimensão 1 lado a lado.
- Então, tomando o comprimento da junta dos dois quadrados, construímos um terceiro quadrado abaixo dos dois quadrados de dimensão 1.
- Novamente tomando os 2 quadrados de dimensão 1, 2 respectivamente construímos o quarto quadrado de dimensão 3.
Embora tenhamos continuado esse processo por um pequeno número de iterações, esse processo continua até o infinito.
 
Depois de concluirmos o desenho dos quadrados, começamos com o menor quadrado interno. Em seguida, desenhamos quadrantes contínuos dentro dos quadrados com o lado de cada quadrado como o raio.

**Resultado**

<img src="https://user-images.githubusercontent.com/65917017/206950101-db56d685-394f-4e3e-8ed4-310cc8fa666e.png" width="480px;">


## Exercício 2 - Árvore fractal
Um fractal é um padrão sem fim. Fractais são padrões infinitamente complexos que são autossimilares em diferentes escalas. Eles são criados repetindo um processo simples repetidamente em um ciclo de feedback contínuo. Impulsionados pela recursão, os fractais são imagens de sistemas dinâmicos

- Inicia-se desenhando uma única forma 'Y' para a árvore base (nível 1). Então, ambos os ramos do 'Y' servem como base para outros dois 'Y's (nível 2).
- Esse processo é repetido recursivamente e o tamanho do Y diminui à medida que o nível aumenta.
- A coloração da árvore é feita em nível: mais escuro no nível de base para mais claro no topo.

**Resultado**

<img src="https://user-images.githubusercontent.com/65917017/206950693-a09c091a-3f38-46f2-867f-ffd893d0c1e1.png" width="480px;">

## Exercício 3 - Criar triângulos
Ao clicar em qualquer ponto da tela exibida pela biblioteca turtle, é possível interagir com a mesma graças à função _onscreenclick(functionname,1)_. Para testar isso, define-se uma função que cria triângulos com apenas um clique.

**Resultado**

<img src="https://user-images.githubusercontent.com/65917017/206952665-bfbc8764-a530-4325-b2ab-f7a086319792.png" width="480px;">


## Exercício 4 - Corrida de tartarugas
Como forma de finalizar o estudo envolvendo as funções comuns da biblioteca turtle, foi desenvolvido um jogo simples para duas pessoas.

Objetivo: O jogador cuja tartaruga chegar primeiro a sua casa ganha o jogo.
Como jogar:

- Cada jogador lança um dado para obter um número.
- O jogador então move sua tartaruga por tantos passos.
- Os jogadores alternam turnos até que um deles vença.

A estrutura:

- Cada jogador tinha uma tartaruga indicada por uma cor diferente. Você pode ter mais de dois jogadores, mas para este tutorial, você criará um jogo para dois jogadores.
- Cada tartaruga tem uma posição inicial que deve alcançar.
- Cada jogador usa um dado para escolher um valor aleatoriamente para seu turno. Em seu programa, o dado é representado por uma lista de números de 1 a 6.

**Resultado**

![Design sem nome](https://user-images.githubusercontent.com/65917017/206960866-0e6abe0b-ae4d-4b53-ae95-9451c0475d3f.gif)







