# Nivel 1

#1
def add_two_numbers(a, b):
    return a + b

# 2
def area_of_circle(r):
    import math
    return math.pi * r * r

# 3
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "Todos los elementos deben ser números."

# 4
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 5
def check_season(month):
    seasons = {
        'Otoño': ['Septiembre', 'Octubre', 'Noviembre'],
        'Invierno': ['Diciembre', 'Enero', 'Febrero'],
        'Primavera': ['Marzo', 'Abril', 'Mayo'],
        'Verano': ['Junio', 'Julio', 'Agosto']
    }
    for season, months in seasons.items():
        if month in months:
            return season
    return "Mes no válido"

# 6
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

#7
def solve_quadratic_eqn(a, b, c):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No hay soluciones reales"
    elif discriminant == 0:
        return -b / (2*a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

# 8
def print_list(lst):
    for item in lst:
        print(item)

# 9
def reverse_list(lst):
    return lst[::-1]

# 10
def capitalize_list_items(lst):
    return [item.upper() for item in lst]

# 11
def add_item(lst, item):
    lst.append(item)
    return lst

# 12
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# 13
def sum_of_numbers(n):
    return sum(range(n + 1))

# 14
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# 15
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

# Nivel 2

# 16
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = sum(1 for i in range(n + 1) if i % 2 != 0)
    return f"The number of evens are {evens}. The number of odds are {odds}."

# 17
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 18
def is_empty(param):
    return not bool(param)

# 19
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    lst.sort()
    n = len(lst)
    mid = n // 2
    return (lst[mid] if n % 2 != 0 else (lst[mid - 1] + lst[mid]) / 2)

def calculate_mode(lst):
    from collections import Counter
    return Counter(lst).most_common(1)[0][0]

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    import math
    return math.sqrt(calculate_variance(lst))

# Nivel 3

# 21
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 22
def all_unique(lst):
    return len(lst) == len(set(lst))

# 23
def same_data_type(lst):
    return all(isinstance(i, type(lst[0])) for i in lst)

# 24
def is_valid_variable(var):
    import keyword
    return var.isidentifier() and not keyword.iskeyword(var)

# 25
def most_spoken_languages(n=10):
    language_counts = {'Inglés': 1500, 'Español': 500, 'Francés': 280, 'Chino': 1200, 'Arabe': 600}
    return sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:n]

# 26
def most_populated_countries(n=10):
    country_population = {'China': 1400, 'India': 1380, 'EEUU': 330, 'Indonesia': 270, 'Brasil': 212}
    return sorted(country_population.items(), key=lambda x: x[1], reverse=True)[:n]