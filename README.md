Panduan menggunakan skrip/kode untuk integerasi python dan duckdb.

1. Metode membuat environtment virtual.

#bash membuat env
python -m venv nama_env

#bash mengaktifkan env
.\nama_env\Scripts\activate

2. Langkah lanjutan install library pendukung.

#bash ritual install pip
pip install duckdb

3. Langkah lanjutan untuk test koneksi python dan duckdb.

#bash menjalankan skrip
python load_data.py

4. Langkah lanjutan untuk testing 

#bash untuk membuat database persisten
python init_data.py

#bash untuk menjalankan test rata-rata
python rata_rata.py

#bash untuk uji tanpa membuat database persisten
python kode_gabungan_rata_rata.py

5. Selesai
