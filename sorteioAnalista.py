import random

analista = ["Nikolas","Alexandre","Ketlyn","Priscila"]

def sorteio_pipoca(q):

    sorteio = random.sample(analista,q)

    return sorteio

print(sorteio_pipoca(1))






