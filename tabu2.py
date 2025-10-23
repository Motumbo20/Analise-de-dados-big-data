num1= int(input('digite um numero: '))
for i in range(1,num1):
    if i % 2 ==0:
        print(f'os numeros pares que precedem são: {i}')
    elif i % 2 != 0:
        print(f"os numeros impares que precedem são: {i}")