# 🌳 Binary Tree in Python - Konsep dan Traversal

## 📹 Video Referensi
**Judul:** Binary Trees in Python: Introduction and Traversal Algorithms  
**Link:** [https://www.youtube.com/watch?v=6oL-0TdVy28](https://www.youtube.com/watch?v=6oL-0TdVy28)

## 📘 Ringkasan

Binary Tree adalah struktur data hirarkis di mana setiap node memiliki maksimal dua anak: `left` dan `right`. Konsep dasar meliputi:
- **Root:** Node paling atas
- **Leaves:** Node paling bawah
- **Depth & Height:** Ukuran kedalaman pohon
- **Parent, Child, Ancestor:** Hubungan antar node

Jenis pohon yang dibahas:
- **Complete Tree:** Semua level terisi penuh kecuali level terakhir
- **Full Tree:** Setiap node memiliki 0 atau 2 anak

### 🔁 Traversal (Penelusuran)
Traversal digunakan untuk mengunjungi semua node. Tiga metode utama:
1. **Pre-order:** Root → Left → Right
2. **In-order:** Left → Root → Right
3. **Post-order:** Left → Right → Root

### 🔧 Implementasi
Kelas `Node` dan `BinaryTree` dibuat dengan Python. Masing-masing traversal diimplementasikan secara rekursif dalam fungsi:
- `pre_order_print`
- `in_order_print`
- `post_order_print`

Fungsi `print_tree(traversal_type)` memanggil traversal yang diinginkan dan mengembalikan string berisi urutan node.

---

📄 **Ringkasan tulisan tangan** tersedia di file `summary.jpg`  
💻 **Kode Python** dapat dilihat di `code.py`



## Summary 
Binary    Tree adalah struktur data pohon di mana setiap node memiliki maksimal dua anak: left dan right. Node paling atas disebut root, sedangkan node tanpa anak disebut leaves. Node dapat memiliki parent, child, dan ancestor. Selain itu, pohon dapat memiliki kedalaman (depth) dan tinggi (height), yang dihitung dari root ke leaves.
Jenis binary tree yang umum meliputi:
Complete Binary Tree: Semua level penuh kecuali level terakhir, yang terisi dari kiri ke kanan.
Full Binary Tree: Semua node memiliki 0 atau 2 anak.
Implementasi dimulai dengan mendefinisikan kelas Node yang menyimpan nilai, serta pointer left dan right. Kemudian dibuat kelas BinaryTree dengan atribut root.
Traversal (penelusuran) merupakan proses mengunjungi semua node:
Pre-order (Root-Left-Right): Cetak root, lalu kiri, lalu kanan.
In-order (Left-Root-Right): Cetak kiri, root, kanan. Biasanya menghasilkan urutan terurut jika datanya disusun.
Post-order (Left-Right-Root): Kunjungi anak-anak dulu baru root. Digunakan dalam penghapusan.
Ketiga metode traversal diimplementasikan secara rekursif. Fungsi tambahan seperti print_tree() digunakan untuk menampilkan hasil traversal sesuai jenisnya. Traversal disusun dalam bentuk string untuk menunjukkan urutan kunjungan node.
