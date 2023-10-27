def kalkulator():
    try:
        operator = input("Masukkan operator aritmatika (+, -, *, /): ")
        if operator not in ('+', '-', '*', '/'):
            raise ValueError("Operator yang dimasukkan tidak valid.")

        angka = input("Berikan angka yang akan dioperasikan, pisahkan dengan spasi: ")
        angka = [float(x) for x in angka.split()]

        if not angka:
            raise ValueError("Tidak ada angka yang diberikan.")

        if operator == '+':
            hasil = sum(angka)
        elif operator == '-':
            hasil = angka[0] - sum(angka[1:])
        elif operator == '*':
            hasil = 1
            for num in angka:
                hasil *= num
        elif operator == '/':
            if 0 in angka[1:]:
                raise ValueError("Pembagian oleh nol tidak diperbolehkan.")
            hasil = angka[0]
            for num in angka[1:]:
                hasil /= num

        print(f"Hasil: {hasil}")
    except ValueError as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    kalkulator()