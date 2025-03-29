# Crear un diccionario vacío llamado dog
dog = {}

# 1
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

# 2
student = {
    'first_name': 'John',  # Primer nombre
    'last_name': 'Doe',  # Apellido
    'gender': 'Male',  # Género
    'age': 21,  # Edad
    'marital_status': 'Single',  # Estado civil
    'skills': ['Python', 'Java'],  # Habilidades
    'country': 'USA',  # País
    'city': 'New York',  # Ciudad
    'address': '123 Main St'  # Dirección
}

#3
student_length = len(student)
print("Longitud del diccionario de estudiante:", student_length)

# 4
skills = student['skills']
print("Habilidades:", skills)
print("Tipo de habilidades:", type(skills))


# 5
student['skills'].extend(['C++', 'JavaScript'])
print("Habilidades actualizadas:", student['skills'])


# 6
keys_list = list(student.keys())
print("Claves del diccionario:", keys_list)

#7
values_list = list(student.values())
print("Valores del diccionario:", values_list)

# 8
student_tuples = list(student.items())
print("Diccionario como lista de tuplas:", student_tuples)

# 9
del student['marital_status']
print("Diccionario después de eliminar marital_status:", student)

# Eliminar uno de los diccionarios
del dog
# print(dog)  # Esto generaría un error ya que dog ya no existe