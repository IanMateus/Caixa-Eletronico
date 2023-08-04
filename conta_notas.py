def conta_notas(val_solicitado, notas_disponiveis):
    while (val_solicitado != 0):
        for nota in notas_disponiveis:
            while (val_solicitado - nota >= 0):
                notas_disponiveis[nota] += 1
                val_solicitado -= nota
    return notas_disponiveis