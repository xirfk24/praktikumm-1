def tampilkan_bilangan_segitiga(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# Contoh penggunaan
n = 6  # Jumlah baris dalam pola segitiga
tampilkan_bilangan_segitiga(n)