try:
    list_besar = [0] * 100000000000
except MemoryError:
    print("Tidak dapat mengalokasikan memori yang diperlukan")