# Kenapa pakai def? 
# → Biar bisa dipanggil berulang (reusable), kayak fungsi di bash script.
def reverseString(s):
    # s itu list karakter, misal: ['h','e','l','l','o']
    # Kita balik pakai dua pointer: kiri mulai dari awal, kanan dari akhir.
    left = 0               # pointer kiri → indeks paling kiri (0)
    right = len(s) - 1     # pointer kanan → indeks paling kanan (terakhir)

    # Kenapa while left < right?
    # → Biar berhenti pas tengah. Kalau left == right, itu huruf tengah (ganjil), gak perlu tukar.
    while left < right:
        # Tukar isi posisi kiri dan kanan
        s[left], s[right] = s[right], s[left]
        # Majukan kiri, mundurkan kanan
        left += 1
        right -= 1
    # Fungsi ini tidak return apa-apa karena langsung ubah list asli (in-place)
    # Di Python, list itu "mutable" → bisa diubah isinya tanpa return.

# Kenapa pakai if __name__ == "__main__": ?
# → Biar kode di bawah ini CUMA jalan kalau file ini di-run langsung (bukan di-import).
# Mirip kayak skrip bash: kalau di-source, gak jalan; kalau di-run, jalan.
if __name__ == "__main__":
    test = ["h", "e", "l", "l", "o"]
    print("Sebelum:", test)
    reverseString(test)  # ubah langsung list-nya
    print("Sesudah:", test)
