hauteur = 1000  #cm
rebonds = 0

while (hauteur > 1):
    rebonds = rebonds + 1
    hauteur = hauteur * 0.9
    print(rebonds, hauteur)

print ("La balle aura rebondit", rebonds, "fois")