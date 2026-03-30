import math

from numba.cuda.printimpl import print_item

# num = int(input("Digite um número: "))
# raiz = math.sqrt(num)
# print(f"A raiz de {num} é {raiz:.2f}")

graus = 45
radiano = graus / 180 * math.pi
seno = math.sin(radiano)
print(seno)

import random

numRandom = random.random()
print(numRandom*10)

numRandomInt = random.randint(1,10)
print(numRandomInt)