# 📘 Stacks and Queues - Ringkasan & Implementasi

## 📹 Video Referensi
**Judul:** Data Structures: Stacks and Queues  
**Pembicara:** Gayle Laakmann McDowell  
**Link:** [https://www.youtube.com/watch?v=wjI1WNcIntg](https://www.youtube.com/watch?v=wjI1WNcIntg)

## 🧠 Ringkasan Materi

Video ini membahas dua struktur data penting: **Stack (LIFO)** dan **Queue (FIFO)**.  
Keduanya merupakan struktur data linier dan fleksibel dalam ukuran, artinya tidak perlu menentukan kapasitas sejak awal.

### 📌 Stack (Last In First Out)
- Analogi: Tumpukan piring.
- Elemen terakhir yang masuk adalah yang pertama keluar.
- Operasi dasar:
  - `isEmpty()` → Mengecek apakah stack kosong.
  - `peek()` → Melihat elemen paling atas tanpa menghapusnya.
  - `push()` → Menambahkan elemen ke atas stack.
  - `pop()` → Menghapus dan mengembalikan elemen paling atas.
- Menggunakan pointer `top`.

### 📌 Queue (First In First Out)
- Analogi: Antrean di bioskop.
- Elemen pertama yang masuk adalah yang pertama keluar.
- Operasi dasar:
  - `isEmpty()` → Mengecek apakah queue kosong.
  - `peek()` → Melihat elemen paling depan.
  - `add()` → Menambahkan elemen di akhir (tail).
  - `remove()` → Menghapus elemen dari depan (head).
- Menggunakan pointer `head` dan `tail`.

### ⚠️ Catatan Teknis
- Null pointer harus diperiksa untuk menghindari error saat stack/queue kosong.
- Implementasi berbasis node dengan pointer antar node.

---

📝 **Ringkasan tulisan tangan** tersedia di file `summary.jpg`.  
💻 **Implementasi Python** dapat dilihat di file `stack_queue.py`.

