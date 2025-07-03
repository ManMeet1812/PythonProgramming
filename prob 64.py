import random as rn

dict = {}

x, y, z =10, 20, 30

dict[x, y, z] = x+y-z

x, y, z = 20, 30, 40
dict[x, y, z] = x+z-y

print(dict)

#######################################################
places = {("19.07'53.2", "72.54'51.0"):"Mumbai", ("28.33'34.1", "77.06'16.6"):"Delhi"}
print(places)
lat = []
long = []
plc = []

for i in places:
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i[0], i[1]])
    
print("Latitude: ",lat)
print("Longitude: ",long)
print("Places: ",plc)

data = {
    (1, "John", "Doe"): {"a": "geeks", "b": "software", "c": 75000},
    (2, "Jane", "Smith"): {"e": 30, "f": "for", "g": 90000},
    (3, "Bob", "Johnson"): {"h": 35, "i": "project", "j": "geeks"},
    (4, "Alice", "Lee"): {"k": 40, "l": "marketing", "m": 100000}
}

print(data[(1, "John", "Doe")]["a"])
print(data[(2, "Jane", "Smith")]["f"])
print(data[(4, "Alice", "Lee")]["k"])

data[(1, "John", "Doe")]["a"] = {"b": "marketing", "c": 75000}
data[(3, "Bob", "Johnson")]["j"] = {"h": 35, "i": "project"}

print(data[(1, "John", "Doe")]["a"])
print(data[(3, "Bob", "Johnson")]["j"])

