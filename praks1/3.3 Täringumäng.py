täringud = int(input("Täringute arv: "))
from random import randint
i = 0
while i < täringud:
    r = randint(1, 6)
    i += 1
    print(str(r))
    