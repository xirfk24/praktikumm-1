def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

awal = int(input("Masukkan angka awal: "))
akhir = int(input("Masukkan angka akhir: "))
prima = [num for num in range(awal, akhir + 1) if is_prime(num)]
print("Bilangan prima antara", awal, "dan", akhir, "adalah:", prima)

n = int(input("Masukkan tinggi segitiga: "))
for i in range(1, n+1):
    print(" "*(n-i) + "*" * (2*i-1))