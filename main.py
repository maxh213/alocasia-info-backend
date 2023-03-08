
from plant import Plant

def get_first_name(full_name):
    first_name = ""
    has_the_first_name_finished = False

    for letter in full_name:
        if letter == " ":
            has_the_first_name_finished = True
        
        if has_the_first_name_finished == False:
            first_name = first_name + letter

    return first_name


# list = [ "Alocasia acuminata", "Alocasia acumina", "Alocasia amazonica" ]

# for x in list:
#     if x == "Alocasia acuminata":
#         print(x)


# object = Plant("Alocasia acuminata", "2020-01-01", 10.00)

# print(object.name)
# print(object.date)
# print(object.cost)

name = "jack jackiny"

first_name = get_first_name(name)

print(first_name)


print(get_first_name("nellie napalm"))

