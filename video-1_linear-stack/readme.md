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
💻 **Implementasi Python** dapat dilihat di file `code.py`.



## Summary
Video ini menjelaskan konsep dasar dan implementasi dari dua struktur data linier populer: Stack dan Queue. Keduanya bersifat dinamis, artinya ukurannya tidak perlu ditentukan di awal dan bisa bertambah atau berkurang sesuai kebutuhan. Perbedaan utamanya terletak pada urutan elemen yang dihapus.
Stack menggunakan prinsip LIFO (Last In First Out), seperti tumpukan piring: elemen terakhir yang dimasukkan akan menjadi yang pertama dikeluarkan. Implementasi stack melibatkan pointer top, dan metode dasar seperti isEmpty, peek, push, dan pop. Dalam push, node baru ditambahkan ke atas stack, dan pada pop, node paling atas diambil dan top dipindah ke node sebelumnya.
Queue, di sisi lain, menggunakan prinsip FIFO (First In First Out), seperti antrean bioskop: orang pertama yang datang akan dilayani terlebih dahulu. Queue menggunakan dua pointer: head untuk penghapusan dan tail untuk penambahan. Operasi dasar meliputi isEmpty, peek, add, dan remove. Saat add, node ditambahkan di akhir (tail), dan jika queue kosong, head akan menunjuk ke node baru tersebut. Saat remove, elemen pertama dihapus dengan memindahkan head ke node berikutnya.
Gayle juga menekankan pentingnya menangani null pointer saat queue atau stack kosong. Meskipun implementasinya tidak kompleks, ketelitian dalam mengatur pointer sangat penting agar tidak terjadi kesalahan logika.
