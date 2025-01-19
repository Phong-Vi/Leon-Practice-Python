population = 7.72   #milliard
années = 2022

while (population < 10):
    années = années + 1
    population = population * 1.0106
    print(années, population)

print("La population dépassera 10 milliards en l'an", années)