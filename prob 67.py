from operator import itemgetter

dv = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 21}]

print (sorted(dv, key=itemgetter('age', 'name')))

dv1 = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

print (sorted(dv1, key=itemgetter('age', 'name')))

dv2 = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

print (sorted(dv2, key=itemgetter('age'), reverse=True))