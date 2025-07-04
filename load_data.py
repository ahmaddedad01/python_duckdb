import duckdb

# Menyambungkan, menjalankan kueri, mengambil hasilnya, lalu mencetaknya.
# Jika salah satu langkah gagal, program akan error.
print(duckdb.connect(database=':memory:').execute("SELECT 'menyambung'").fetchone()[0])