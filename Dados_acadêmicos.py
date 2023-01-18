print("Se você for estudante digite 1, se for professor digite 2:")

competencia = int(input())

if competencia == 1:
    print("Olá, caro estudante! Digite seu nome, e em seguida o sobrenome.")
    nomealuno = input("Nome:")
    sobrenomealuno = input("Sobrenome:")
    print("Certo,",nomealuno,"! Agora digite seu número de RG:")
    numerorg = input()
    print("Agora precisaremos que digite seu CPF, e em seguida o seu R.A.")
    numerocpf = input("CPF:")
    numerora = input("R.A:")
    print("Perfeito! Agora que já possuímos seus dados, em qual curso você está estudando?")
    curso = input()
    print("O estudante",nomealuno, sobrenomealuno,", portador do RG:",numerorg,"e CPF:",numerocpf,", e cadastrado no RA:",numerora,", está estudando o curso de",curso,"."); 
elif competencia ==2:
    print("Olá, professor! Digite seu nome, e em seguida o sobrenome.")
    nomeprofessor = (input("Nome:"))
    sobrenomeprofessor = input("Sobrenome:")
    print("Certo,",nomeprofessor,"! Agora digite seu número de RG:")
    numerorgp = input()
    print("Agora precisaremos que digite seu CPF e em seguida o seu número de registro:")
    numerocpfp = input("CPF:")
    numeroregistro = input("Número de registro:")
    print("Perfeito! Agora que já possímos seus dados, em qual curso você está lecionando?")
    cursop = input()
    print("O professor",nomeprofessor, sobrenomeprofessor,", portador do RG:",numerorgp,"e CPF:",numerocpfp,", e cadastrado no número de registro:",numeroregistro,", está lecionando o curso de",cursop,".")
else:
    print("Número inválido!")    