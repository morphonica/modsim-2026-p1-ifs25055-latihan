import json

data = {
    "nama": "Andi",
    "umur": 20
}

with open("data.json", "w") as file:
    json.dump(data, file)

print("Data disimpan")
