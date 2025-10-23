senhacorreta = "senhasecreta"
for tentativa in range (1,5):
    entrada= input(f"tentativa{tentativa}:")
    if entrada == senhacorreta:
        print('acesso permitido')
        break
    else:
        print('senha incorreta')
else:
        print('acesso bloqueado por muitas tentativas')