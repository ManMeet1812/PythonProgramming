list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

print(sorted(list, key=lambda i: i['age']))
print(sorted(list, key=lambda i:(i['age'], i['name'])))
print(sorted(list, key=lambda i: i['age'], reverse = True))
