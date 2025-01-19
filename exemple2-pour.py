#méthode1
somme = 0
for b in range (300, 401):
    x = b / 3
    if (int(x) == x):
        somme = somme + b
print("La somme de tous les multiples de 3 entre 300 et 400 est", somme)

#méthode2
somme = 0
for c in range (300, 401, 3):
    somme = somme + c
print("La somme de tous les multiples de 3 entre 300 et 400 est", somme)