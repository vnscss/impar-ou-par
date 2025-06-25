boleano = False
file = 'impar-ou-par.py'

def read_line(intLine):
    with open("impar-ou-par.py") as fp:
        linha = fp.readlines()[intLine]
        return linha

def raise_error():
    raise Exception("O arquivo impar-ou-par.py especificado é inválido... :(")

def validate_file():

    headerString = read_line(1).strip()
    footerString = read_line(-2).strip()

    if 'numero = int(input("Digite um número: "))' in headerString and \
       'print(f"Não é possivel determinar se {numero} é um número ímpar ou par. :(  ")''' in footerString:
            try:
                string = read_line(1).strip()
                exec(string ,  globals())
                return True
            except Exception as e:
                print(e)
                return False
    else:
        raise_error()


if validate_file():
    fp = open(file)
    for i, line in enumerate(fp):
        if f'{numero}' in line:
            string = read_line(i+1).strip()
            exec(string)
            exit(0)
    fp.close()

    string = read_line(-2).strip()
    exec(string)



