# Nivel 1

# 1
print("Iteración con for:")
for i in range(11):
    print(i)

i = 0
print("Iteración con while:")
while i <= 10:
    print(i)
    i += 1

#2
print("Iteración inversa con for:")
for i in range(10, -1, -1):
    print(i)

i = 10
print("Iteración inversa con while:")
while i >= 0:
    print(i)
    i -= 1

# 3
for i in range(1, 8):
    print("#" * i)

# 4
for _ in range(8):
    print("# # # # # # # #")

# 5
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6
fruits = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for fruit in fruits:
    print(fruit)

# 7
print("Números pares:")
for i in range(0, 101, 2):
    print(i)

# 8
print("Números impares:")
for i in range(1, 101, 2):
    print(i)

# Nivel 2

# 1
suma_total = sum(range(101))
print(f"La suma de todos los números es {suma_total}.")

# 2
suma_pares = sum(i for i in range(101) if i % 2 == 0)
suma_impares = sum(i for i in range(101) if i % 2 != 0)
print(f"La suma de todos los pares es {suma_pares}. Y la suma de todos los impares es {suma_impares}.")

# Nivel 3

# 1
countries = ['Argentina', 'Australia', 'Bolivia', 'Colombia', 'Tierra del Fuego', 'Finlandia', 'Groenlandia']
countries_with_land = [country for country in countries if 'tierra' in country.lower()]
print("Países con 'tierra':", countries_with_land)

# 2
fruits = ['plátano', 'naranja', 'mango', 'limón']
fruits.reverse()
print("Lista de frutas invertida:", fruits)

# 3
languages = ['Inglés', 'Español', 'Francés', 'Inglés', 'Alemán', 'Chino', 'Español', 'Portugués']
total_languages = len(set(languages))
print("Número total de idiomas:", total_languages)

# 4
language_counts = {'Inglés': 1500, 'Español': 500, 'Francés': 280, 'Chino': 1200, 'Árabe': 600, 'Hindi': 800, 'Portugués': 220, 'Bengalí': 270, 'Ruso': 260, 'Japonés': 125}
most_spoken_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:10]
print("Los 10 idiomas más hablados:", most_spoken_languages)

# 5
country_population = {'China': 1400, 'India': 1380, 'EEUU': 330, 'Indonesia': 270, 'Pakistán': 220, 'Brasil': 212, 'Nigeria': 206, 'Bangladesh': 165, 'Rusia': 144, 'México': 126}
most_populated_countries = sorted(country_population.items(), key=lambda x: x[1], reverse=True)[:10]
print("Los 10 países más poblados:", most_populated_countries)