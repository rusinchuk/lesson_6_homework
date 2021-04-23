import requests

#Opening file
books_rest = requests.get('http://pulse-rest-testing.herokuapp.com/books')
print(books_rest.json()[0])
print(books_rest.text)
print(books_rest.status_code)
print(books_rest.headers)

#First script
payload = {'title': 'Kobzar', 'author': 'Taras Shevchenko'}
r = requests.post('http://pulse-rest-testing.herokuapp.com/books', data=payload)
print(r.text)
print(r.json()['id'])
id_my_book = r.json()['id']

books_rest = requests.get(f'http://pulse-rest-testing.herokuapp.com/books/{id_my_book}')
assert books_rest.json()['id'] == id_my_book and books_rest.json()['title'] == 'Kobzar' and books_rest.json()['author'] == 'Taras Shevchenko'
print('Book has been created successfully')

payload = {'title': "Zahar Berkut", 'author': "Ivan Franko"}
z = requests.put(f'http://pulse-rest-testing.herokuapp.com/books/{id_my_book}', data=payload)
print(z.text)

books_rest = requests.get(f'http://pulse-rest-testing.herokuapp.com/books/{id_my_book}')
assert books_rest.json()['id'] == id_my_book and books_rest.json()['title'] == "Zahar Berkut" and books_rest.json()['author'] == "Ivan Franko"
print('Book has been changed successfully')
print(books_rest.json())

z = requests.delete(f'http://pulse-rest-testing.herokuapp.com/books/{id_my_book}')
assert z.status_code == 204
print('Book has been deleted successfully')

#Second script

payload = {'title': 'Hamlet', 'author': 'William Shakespeare'}
books_rest = requests.post('http://pulse-rest-testing.herokuapp.com/books', data=payload)
print(books_rest.text)
print(books_rest.json()['id'])
id_my_book = books_rest.json()['id']

k = requests.get(f'http://pulse-rest-testing.herokuapp.com/books/{id_my_book}')
assert k.json()['id'] == id_my_book and k.json()['title'] == 'Hamlet' and k.json()['author'] == 'William Shakespeare'
print('Book has been created successfully')

payload = {'name': 'Horace', 'type': 'Main', 'level': 1, 'book': f'{id_my_book}'}
books_rest = requests.post('http://pulse-rest-testing.herokuapp.com/roles', data=payload)
id_person = books_rest.json()['id']

books_rest = requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/{id_person}')
assert books_rest.json()['id'] == id_person and books_rest.json()['name'] == 'Horace' and books_rest.json()['type'] == 'Main' and books_rest.json()[
    'level'] == 1
print('Role has been created successfully')

payload = {'name': 'Polonius', 'type': 'Secondary', 'level': 2, 'book': f'{id_my_book}'}
books_rest = requests.put(f'http://pulse-rest-testing.herokuapp.com/roles/{id_person}', data=payload)
assert books_rest.json()['id'] == id_person and books_rest.json()['name'] == 'Polonius' and books_rest.json()['type'] == 'Secondary' and books_rest.json()[
    'level'] == 2
print('Role has been changed successfully')
print(books_rest.json())

j = requests.delete(f'http://pulse-rest-testing.herokuapp.com/books/{id_my_book}')
assert j.status_code == 204
print('Book has been deleted successfully')

j = requests.delete(f'http://pulse-rest-testing.herokuapp.com/roles/{id_person}')
assert j.status_code == 204
print('Role has been deleted successfully')
















