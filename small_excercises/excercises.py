# d = {"a": 1, "b":2, "c":3}
# d = dict((key, value) for key, value in d.items() if value <= 1)
# print(d)

# from pprint import pprint

# d = {"a": list(range(1,11)) , "b": list(range(11, 21))}
# pprint(d)

# import string
# print(string.ascii_lowercase)

# a = [1,3,4]
# b = [4,5,7]

# for i, j in zip(a,b):
#     print(i , j)

# import os

# if not os.path.exists("letters"):
#     os.makedirs("letters")

# with open("letters/" + "a.txt", "w") as file:
#     file.write("abc")

import json

with open("company1.json", "r+") as file:
    d = json.loads(file.read())
    d['employees'].append({"firstName": "Jim", "lastName": "Halpert"})
    file.seek(0)
    json.dump(d, file, indent = 4, sort_keys=True)
    file.truncate()


