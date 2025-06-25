import os
import sys


def generate(r1 , r2):
    for i in range(r1 , r2):
        sys.stdout.write(f"\rIterations: {i}    Bytes: {os.path.getsize('./impar-ou-par.py')}    ")
        sys.stdout.flush()
        string = ''
        if i % 2 == 0:
            string = 'par'
        else:
            string = 'ímpar'

        innerString = ''

        if i == 0:
            innerString = 'if'
        elif i != 0:
            innerString = 'elif'


        text = '''
{innerString} numero == {i}: 
    print("O número {i} é {string}.")
        '''.format(i=i, string=string , innerString=innerString)


        with open("impar-ou-par.py", "a") as myfile:
            myfile.write(text)


with open("impar-ou-par.py", "a") as myfile:
    myfile.write('''
numero = int(input("Digite um número: "))
    ''')


mode = int(input("1 para breakpoint, 2 para tamanho em esperado: "))

if mode == 1:
    breakpoint = int(input("Digite o breakpoint: "))
    generate(0 ,breakpoint)
    
elif mode == 2:
    targetBytes = int(input("Digite o tamanho esperado: "))

    atualBytes = os.path.getsize('./impar-ou-par.py')

    i = 0

    while atualBytes < targetBytes:
        generate(i , i +1 )
        i += 1
        atualBytes = os.path.getsize('./impar-ou-par.py')


with open("impar-ou-par.py", "a") as myfile:
    myfile.write('''
else:
    print(f"Não é possivel determinar se {numero} é um número ímpar ou par. :(  ")
    ''')

