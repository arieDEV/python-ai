def isPalindrome(s):
    # Bersihkan string: ambil CUMA huruf & angka, dan jadikan kecil semua
    # Kenapa .lower()? Biar 'A' == 'a' → jadi case-insensitive.
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    # Penjelasan bagian atas:
    #   ch in s → ambil tiap karakter
    #   if ch.isalnum() → cek: huruf atau angka? kalau iya, ambil
    #   ch.lower() → ubah jadi huruf kecil
    #   ''.join(...) → gabung semua jadi satu string (karena hasilnya list karakter)

    # Sekarang cek: apakah cleaned == dibaca terbalik?
    # [::-1] artinya: ambil semua, tapi dari belakang → reverse string
    return cleaned == cleaned[::-1]
    # Kenapa return? Karena fungsi ini harus kasih jawaban True/False ke pemanggil.

if __name__ == "__main__":
    test = "A man, a plan, a canal: Panama"
    result = isPalindrome(test)
    print(f'"{test}" → Palindrome? {result}')
