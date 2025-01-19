#votre nom?
print ("Quel est votre nom?")
nom = input()

while (nom.isdigit() == True):
    print ("Quel est votre nom?")
    nom = input()

#votre âge?
print ("Quel est votre âge?")
age = input()

while (age.isdigit() == False):
    print ("Quel est votre âge?")
    age = input()

#votre ville?
print ("Quel est votre ville?")
ville = input()

while (ville.isdigit() == True):
    print ("Quel est votre ville?")
    ville = input()

#résumé
print ("Vous êtes "+ nom)
print ("Vous avez " + age + " ans")
print ("Vous habitez à " + ville)