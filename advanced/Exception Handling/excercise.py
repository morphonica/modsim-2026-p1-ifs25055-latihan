try:
    x = int(input("Masukkan angka: "))
    print(10 / x)
except ZeroDivisionError:
    print("Tidak bisa dibagi nol")
except ValueError:
    print("Input harus angka")
