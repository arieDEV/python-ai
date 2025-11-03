Mantap, Arie! 👊  
Kita **mulai Hari 1** dengan **penjelasan super jelas dalam kode**, langsung di **komentar**, tanpa teori bertele-tele.  
Fokus: **3 soal LeetCode Easy** → tapi **setiap baris dijelaskan kenapa ada**, dengan bahasa *mantan sysadmin* (langsung ke inti, no fluff).

---

### 📁 Struktur Hari Ini:
- Buat folder `day01/`
- Buat 3 file:
  - `reverse_string.py`
  - `valid_palindrome.py`
  - `group_anagrams.py`

---

## ✅ Soal 1: **Reverse String**  
🔗 [https://leetcode.com/problems/reverse-string/](https://leetcode.com/problems/reverse-string/)  
> Input: `["h","e","l","l","o"]` → Output: `["o","l","l","e","h"]`  
> Ubah isi list **langsung**, jangan bikin list baru.

### 📄 `reverse_string.py`
```python
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
```

---

## ✅ Soal 2: **Valid Palindrome**  
🔗 [https://leetcode.com/problems/valid-palindrome/]  
> Input: `"A man, a plan, a canal: Panama"` → Output: `True`  
> Abaikan non-huruf/angka, dan abaikan besar/kecil.

### 📄 `valid_palindrome.py`
```python
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
```

---

## ✅ Soal 3: **Group Anagrams**  
🔗 [https://leetcode.com/problems/group-anagrams/]  
> Input: `["eat","tea","tan","ate","nat","bat"]`  
> Output: `[["eat","tea","ate"],["tan","nat"],["bat"]]`  
> Anagram = hurufnya sama, cuma urutan beda.

### 📄 `group_anagrams.py`
```python
def groupAnagrams(strs):
    # Pakai dictionary buat kelompokkan kata
    # Key: bentuk "standar" dari kata (misal: "eat" → "aet")
    # Value: list kata yang punya bentuk standar itu
    anagram_map = {}

    for word in strs:
        # Buat "signature" dengan urutkan hurufnya
        # "eat" → sorted jadi ['a','e','t'] → join jadi "aet"
        # Kenapa sorted()? Karena semua anagram punya urutan huruf yang sama kalau disortir.
        signature = ''.join(sorted(word))
        # Kenapa join? Karena sorted() hasilnya list → harus jadi string biar bisa jadi key dict.

        # Kalau signature belum ada di dict, buat list baru
        if signature not in anagram_map:
            anagram_map[signature] = []
        # Masukkan kata asli ke list-nya
        anagram_map[signature].append(word)

    # Kembalikan semua nilai (list of lists)
    # .values() → ambil semua list dalam dict
    # list(...) → ubah ke list biasa (bukan dict_values object)
    return list(anagram_map.values())

if __name__ == "__main__":
    test = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = groupAnagrams(test)
    print("Grouped anagrams:", result)
```

---

## 🔚 Langkah Selanjutnya (Hari Ini!)
1. Buat folder `day01/`
2. Simpan ketiga file di atas
3. Jalankan satu per satu:
   ```bash
   python day01/reverse_string.py
   python day01/valid_palindrome.py
   python day01/group_anagrams.py
   ```
4. Cek output → harus sesuai ekspektasi
5. Push ke GitHub:
   ```bash
   git init
   git add day01/
   git commit -m "Day 1: 3 LeetCode problems with sysadmin-style explanations"
   git push
   ```

---

> 💡 **Catatan buat mantan sysadmin**:  
> - `def` = seperti fungsi di bash, tapi lebih powerful  
> - `return` = seperti `echo` di fungsi bash → kirim hasil keluar  
> - `if __name__ == "__main__"` = seperti `[[ "${BASH_SOURCE[0]}" == "${0}" ]]` → pastikan jalan cuma kalau di-run  
> - `join` = seperti `IFS=,` di bash → gabung array jadi string  
> - `sorted()` = seperti `sort` di bash → urutkan  

---

Kirim link GitHub-nya!  
Besok kita lanjut **Hari 2: parsing log file** — ini bakal berasa kayak kerjaan sysadmin, tapi pake Python. 🔥
