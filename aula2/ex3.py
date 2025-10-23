senha= 'porco'
for vezes in range (1,4):
    tentativa= input('digite a senha: ')
    if tentativa == senha:
        print('acesso permitido')
        break
    else:
        print('tente novamente')
else:
    print('acesso negado')