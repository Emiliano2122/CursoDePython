# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variables = str(my_int_variable)
print(my_int_to_str_variables)
print(type(my_int_to_str_variables))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variables, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Emiliano", "Stasi", 'emilianostasi', 22
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Input
"""
name = input('¿Cual es tu nombre?')
age = input('¿Cuantos años tienes?')
print(name)
print(age)
"""

# Cambiamos su tipo
name = 22
age = "Emiliano"
print(name)
print(age)



# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))
