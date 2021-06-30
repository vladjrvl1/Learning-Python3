# cars = []
# for pesron in users:
#     cars.append(person['car'])
#
# print(cars)
jack = {
    'name': 'jack',
    'car': 'bmw',
}
john = {
    'name': 'john',
    # 'car': 'audi',
}
users = [jack, john]
new_cars = [person.get('car', '') for person in users]
# (values) = [ (expression) for (value) in (collection) ]
# (values) = []
# for (value) in (collection):
#     values.append( (expression) )


# Фильтрация

names = [
    'jack', 'john', 'oleg', 'ula'
]
j_names = [name for name in names if name.startswith('j')]

# j_names = []
# for name in names:
#     if name.startswith('j'):
#         j_names.append(name)


