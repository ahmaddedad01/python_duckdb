import duckdb

# Inisialisasi koneksi DuckDB dengan database persisten
con = duckdb.connect(database='mobile_pricing.db')

# Query untuk menampilkan rata-rata harga
avg_price = con.execute("SELECT AVG(battery_power) AS avg_price FROM mobile_pricing").fetchone()
print(f"Rata-rata harga baterai: {avg_price[0]}")