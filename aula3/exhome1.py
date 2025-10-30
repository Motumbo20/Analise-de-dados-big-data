nome = input('digite seu nome:')
salario = float(input("digite seu salario:"))
if salario >= 3000:
    desconto = (salario*0.11)
elif salario >= 2000:
    desconto = (salario*0.09)
elif salario <= 2000:
    desconto = (salario*0.08)


if salario >= 2000:
    trans = (salario*0.08)
else:
    trans = (salario*0.05)


if salario >= 3000:
    bonus = 300
else:
    bonus  = 200


if salario >= 3000:
    cargo = ("Acionista")
elif salario >= 2000:
    cargo = ("Gerente")
elif salario <= 2000:
    cargo = ("Vendedor")

salarioliq = salario - (desconto + trans) + bonus

print("================================================================================================")
print (f"{nome}, seu salario bruto informado foi de {salario} e seu salario liquido é de {salarioliq}")
print("=================================================================================================")
print(f"os descontos aplicados foram de  {desconto} referente ao INSS, {trans} referente ao VT")
print("=================================================================================================")
print(f"também recebeu um bonus de {bonus}, e seu cargo atual é de {cargo}")
print("=================================================================================================")