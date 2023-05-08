try:
    data = {"nama": "John", "usia": 25}
    print(data["alamat"])
except KeyError:
    print("Kunci tidak ditemukan")