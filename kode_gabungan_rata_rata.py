import duckdb

# Inisialisasi koneksi DuckDB
con = duckdb.connect(database=':memory:')  # Gunakan ':memory:' untuk database in-memory

# Load data CSV ke DuckDB
con.execute("CREATE TABLE mobile_pricing AS SELECT * FROM read_csv_auto('Mobile Phone Pricing.csv')")

# Query untuk menampilkan rata-rata harga baterai
avg_price = con.execute("SELECT AVG(battery_power) AS avg_price FROM mobile_pricing").fetchone()
print(f"Rata-rata harga baterai: {avg_price[0]}")