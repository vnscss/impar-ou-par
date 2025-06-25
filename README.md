# Exercício: Ímpar ou Par

Apenas um exercício para calcular se um número é ímpar ou par.
Número máximo até hoje: 71236

🥸


Este repo é uma brincadeira que resolvi fazer rapidinho e postar.

Me inspirei após ver o video do `@ThePrime`, que é um react do código do `@jekyll`:  


- Vídeo: https://www.youtube.com/watch?v=nlFjL0B43-w
- Artigo: https://andreasjhkarlsson.github.io/jekyll/update/2023/12/27/4-billion-if-statements.html


## Como rodar

Por conta do `impar-ou-par.py` ser um arquivo muito grande, o python retorna:
> MemoryError: Parser stack overflowed - Python source too complex to parse


Então para rodar o código, execute o `run.py`


#### Como funciona o run.py

O `run.py` basicamente verifica se o arquivo `impar-ou-par.py` é válido e depois executa a primeira linha dele:

```python
#impar-ou-par.py
numero = int(input("Digite um número: "))
```

Então percorre o `impar-ou-par.py` até encontrar o bloco `elif` respectivo ao número que o usuário informou e o executa.

```python
#Numero informado pelo user == 65971
#run.py percorre o arquivo até encontrar o bloco correto e o executa.

...

elif numero == 65971: 
    print("O número 65971 é ímpar.")

...
```

Caso o número informado pelo user não esteja presente em nenhum bloco `elif`, o código executa o `else` no final do arquivo `impar-ou-par.py`

## Como gerar o arquivo impar-ou-par.py

Para gerar um arquivo `impar-ou-par.py` execute o script `create.py`.

Existem dois modos de geração:

- Breakpoint: Informe até que número inteiro o script `impar-ou-par.py` irá verificar.
- Tamanho esperado: Informe em bytes o tamanho esperado que o arquivo `impar-ou-par.py` deverá ter.


```bash

Digite o modo de geração:
1 - Breakpoint
2 - Tamanho esperado (em bytes)

```

Após escolher o modo, o script pedirá o input do tamanho esperado ou do breakpoint.


```bash

Digite o modo de geração:
1 - Breakpoint
2 - Tamanho esperado (em bytes)

: 1 #user escolheu o modo 1 

Digite o breakpoint: 9999999 #breakpoint escolhido pelo user
```

Pronto! O arquivo `impar-ou-par.py` estará disponível para ser apreciado 🥸 .