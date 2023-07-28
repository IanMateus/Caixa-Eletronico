from conta_notas import conta_notas
def saque():
    notas_disponiveis = {100:0, 50:0, 10:0, 5:0, 1:0}
    val_min = 10
    val_max = 600

    val_solicitado = int(input("Digite o valor desejado (entre R$10 e R$600):"))
    if ((val_solicitado > val_max) or (val_solicitado < val_min)):
        print("Valor inválido")
    else:
        notas_devolvidas = conta_notas(val_solicitado, notas_disponiveis)
        notas = []
        for nota in notas_devolvidas.keys():
            if nota != 0:
                print("{} nota(s) de R${}".format(notas_devolvidas[nota], nota))