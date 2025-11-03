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
