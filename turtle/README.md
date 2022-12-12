# Arquivos - /turtle
Pasta criada com o intuito de alocar os exercícios utilizando a biblioteca Python Turtle.

Nesta pasta é possível executar os códigos e visualizar os resultados dos exercícios


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


### Exercício 1 - Sequência de Fibonacci
Cada número na série representa o comprimento dos lados de um quadrado. O quadrado de lado 0 não existe. Então começamos do quadrado de lado 1. O próximo quadrado também tem lado 1. 
 
- Primeiro constrói-se dois quadrados de dimensão 1 lado a lado.
- Então, tomando o comprimento da junta dos dois quadrados, construímos um terceiro quadrado abaixo dos dois quadrados de dimensão 1.
- Novamente tomando os 2 quadrados de dimensão 1, 2 respectivamente construímos o quarto quadrado de dimensão 3.
Embora tenhamos continuado esse processo por um pequeno número de iterações, esse processo continua até o infinito.
 
![alt text](https://media.geeksforgeeks.org/wp-content/uploads/Fibo-Fractal-1-1.png)

Depois de concluirmos o desenho dos quadrados, começamos com o menor quadrado interno. Em seguida, desenhamos quadrantes contínuos dentro dos quadrados com o lado de cada quadrado como o raio.

* Resultado

