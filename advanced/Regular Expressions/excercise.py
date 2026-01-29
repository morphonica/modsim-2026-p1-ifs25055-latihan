import re

text = "Python123"
result = re.search(r"\d+", text)

if result:
    print("Mengandung angka")
else:
    print("Tidak mengandung angka")
