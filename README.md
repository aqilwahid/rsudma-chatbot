![alt text](<images/Logo Chatbot-2.png>)
# 💬 RSUD MA-Ai-BOT 🤖
Chatbot AI RSUD MA untuk WhatsApp 🤖💬 yang dibuat menggunakan teknik _Fine-tuning_ untuk informasi terkait RSUD MA, termasuk informasi umum tentang layanan kesehatan, kebijakan standar pelayanan, dan profil direktur. Data ini bertujuan untuk mendukung chatbot dalam memberikan respons yang akurat dan kontekstual kepada pengguna. _Retrieval-Augmented Generation_ untuk data dinamis seperti database inventory RSUD MA. Proyek ini memanfaatkan model pembelajaran mendalam canggih dari gemma2-9b-cpt-sahabatai-v1-instruct.

## Pipeline Proyek 
1. Pembuatan korpus
    * Pengumpulan data
    * Cleaning data
    * Formating alpaca style
    * Formating gemma prompt style
2. _Fine-tuning_ model
    * ![alt text](<images/W&B Chart.png>)
    * Model:gemma2-9b-cpt-sahabatai-v1-instruct digunakan sebagai dasar _fine-tuning_.
    * Output: Model dapat memberikan respons spesifik terkait informasi RSUD MA.
3. _Retrieval-Augmented Generation_ (RAG) untuk Data Dinamis
    * Mengakses database Menggunakan MySQL.
    * Membuat Backend API
    * Data diindeks menggunakan FAISS.
4. Implementasi WhatsApp
    * Integrasi dengan library seperti pywhatkit komunikasi otomatis.
5. Keamanan dan Pembatasan Akses
    * _Access Control List_ (ACL)

## 💻 Update 28-12-2024
![alt text](image-3.png)
Proyek ini masih dalam tahap pengembangan, untuk saat ini developer sedang berada di tahap penyempurnaan RAG.

## Fitur yang tersedia
| Features | Available |
| ----- | ----- |
| Desain dan Perancangan Chatbot | ✅ |
| Chatbot dengan pengetahuan local | ✅ |
| Integrasi chatbot ke sistem data | ✅ |
| Pengecekan Stok Real-Time | ✅ |
| Custom notifikasi | ✅ |
| Decrypted code | ✅ |
| Exclusive API offers | ✅ |
