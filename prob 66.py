import sys

dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

print("Size of dic1: ", sys.getsizeof(dic1), "bytes")
print("Size of dic1: ", sys.getsizeof(dic2), "bytes")
print("Size of dic1: ", dic3.__sizeof__(), "bytes")

