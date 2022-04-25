"""
 стр. 327 Ссылки или копии
"""

rec = {'name' : 'Bob',
        'jobs' : ['developer', 'manager'],
        'web' : 'www.bobs.org/Bob',
        'home': {'state': 'Overworked', 'zip': 12345}}
print(rec)
print('-' * 30)

print(rec['name'])
print('-' * 30)
print(rec['jobs'])
print('-' * 30)
print(rec['jobs'][1])
print('-' * 30)
print(rec['home']['zip'])

db = []

db.append(rec)
e = db[0]['jobs']
print(f'Достали работу из бд: {e}')
