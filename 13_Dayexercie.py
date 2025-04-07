

import random

# 1
def random_user_id():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

# 2
def user_id_gen_by_user():
    num_chars = int(input("Ingrese el número de caracteres: "))
    num_ids = int(input("Ingrese el número de IDs a generar: "))
    return [''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=num_chars)) for _ in range(num_ids)]

# 3
def rgb_color_gen():
    return f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})"

# Nivel 2

# 4
def list_of_hexa_colors(n):
    return [f"#{''.join(random.choices('0123456789abcdef', k=6))}" for _ in range(n)]

# 5
def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

# 6
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Tipo de color no válido"

# Nivel 3

# 7
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

#8
def unique_random_numbers():
    return random.sample(range(10), 7)

# 9
def filter_negative_and_zero(numbers):
    return [num for num in numbers if num <= 0]

# 10
def flatten_list(nested_list):
    return [item for sublist in nested_list for inner_list in sublist for item in inner_list]

# 11
def create_tuples():
    return [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]

# 12
def transform_countries(countries):
    return [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]

# 13
def countries_to_dict(countries):
    return [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]

# 14
def names_to_strings(names):
    return [f"{first} {last}" for sublist in names for first, last in sublist]

# 15
calculate_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None