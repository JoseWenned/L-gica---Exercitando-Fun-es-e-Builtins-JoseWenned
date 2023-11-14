import math
# Função delta


def calculo_delta(valorA, valorB, valorC):
    return (valorB * valorB) - 4 * (valorA) * (valorC)


delta = calculo_delta(4, 6, 2)
print(delta)

# Função bhaskara


def calculo_bhaskara(delta):

    if delta < 0:
        return "Delta Negativo"
    else:
        raiz1 = (-delta.valorB + math.sqrt(delta) / 2 * delta.valorA)
        raiz2 = (-delta.valorB - math.sqrt(delta) / 2 * delta.valorA)

    raiz1 = round(raiz1, 2)
    raiz2 = round(raiz2, 2)

    return raiz1, raiz2


print(calculo_bhaskara())
