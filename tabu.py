num1 = int(input('fale um numero: '))#
for i in range(1,11):#
    resultado= num1 *i#
    print(f"{num1} x {i} = {resultado}")#
    ###tabuada acima e numeros pares abaixo
    num1= int(input('digite um numero: '))
    for i in range(1,num1):
        if i % 2 ==0:
            print(f'os numeros pares que precedem são: {i}')
        elif i % 2 != 0:
            print(f"os numeros impares que precedem são: {i}")