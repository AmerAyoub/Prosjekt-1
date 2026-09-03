
def addisjon(a, b):
    print(a + b)

addisjon(10, 5)

def subtraksjon(a, b):
    print(a - b)

subtraksjon(7, 12)

def multi(a, b):
    print(a * b)

multi(2, 7)

def divi(a, b):
    print(a / b)

divi(10, 3)


def kalku(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)

kalku(19, 6)

# hente to tall fra brukeren
n1 = int(input("skriv inn num1 "))
n2 = int(input("skriv inn num2 "))

# legge sammen to tall 
def kal(c, d):
    print(c + d)
    print(c - d)
    print(c * d)
    print(c / d)

kal(n1, n2)


def regn():
    numb1 = int(input("skriv inn første tall "))
    numb2 = int(input("skriv inn andre tall "))
    print(numb1 + numb2)
    print(numb1 - numb2)
    print(numb1 * numb2)
    print(numb1 / numb2)

regn()


def add(a, b):
    return(a + b)
resultat = add(1, 3)

print(resultat)


def sub(a, b):
    return(a - b)
svar = sub(5, 3)

print(svar)
