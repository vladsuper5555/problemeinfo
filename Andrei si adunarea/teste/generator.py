from random import randint 

for i in range (1,11):
    nume_test = 'test' + str(i)
    nr1, nr2 = '1', '1'
    car1, car2 = randint(1, 29), randint(1, 29)
    for j in range (car1):
        cifra = randint(0, 1)
        nr1 += str(cifra)
    for j in range (car2):
        cifra = randint(0, 1)
        nr2 += str(cifra)
    with open (nume_test + '.in', 'w') as f:
        f.write(nr1 + ' ' + nr2)