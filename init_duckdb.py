import duckdb

# Inisialisasi koneksi DuckDB dengan database persisten
con = duckdb.connect(database='mobile_pricing.db')

# Load data CSV ke DuckDB
con.execute("CREATE TABLE mobile_pricing AS SELECT * FROM read_csv_auto('Mobile Phone Pricing.csv')")

# Cek isi tabel
result = con.execute("SELECT * FROM mobile_pricing LIMIT 5").fetchall()
print(result)