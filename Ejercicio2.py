# Programa: término n-ésimo de una progresión geométrica

a1 = float(input("Ingresa el primer término (a1): "))
r = float(input("Ingresa la razón (r): "))
n = int(input("Ingresa el número de término que quieres (n): "))

sn = a1 * (r ** (n - 1))



if r != 1:
    sn = a1 * (r ** (n - 1))/ r - 1
    print("La progresion geometrica es: \t", sn)
else:
    sn = a1 * n
    break