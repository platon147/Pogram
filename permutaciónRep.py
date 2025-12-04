def permutacion_repeticiones(n, k):
    return n ** k

n = int(input("Ingresa n total de elementos: "))
k = int(input("Ingresa k elementos a elegir: "))

if n < 0 or k < 0:
    print("n y k deben ser números no negativos.")
else:
    p = permutacion_repeticion(n, k)
    print("P(", n, ",", k, ") =", P)