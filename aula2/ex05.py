alunos=[{"nome":"ana","nota":[7,8.5,]},
        {"nome":"jose","nota":[5,5]},
        {"nome":"carlos","nota":[3,4]}
        ]


for alunos in alunos:
    media= sum(alunos["nota"])/len(alunos["nota"])
    if media >= 7:
        situacao= "aprovada"
else:
    situacao= "reprovada"

    print(f"{alunos['nome']}-media:{media:.2f}-{situacao}")