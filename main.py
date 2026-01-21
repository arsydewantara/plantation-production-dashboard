from cleaning import clean_data
from db import get_connection

df = clean_data()
conn = get_connection()
cursor = conn.cursor()

print(df.columns)

for _, row in df.iterrows():
    sql = """
    INSERT INTO produksi_harian(tanggal, afdeling, produksi, keterangan)
    VALUES(%s,%s,%s,%s)
    """
    data = (row["tanggal"],
            row["afdeling"],
            row["produksi"],
            row["keterangan"])
    cursor.execute(sql,data)

conn.commit()
print("Data berhasil dimasukkan ke DATABASE")