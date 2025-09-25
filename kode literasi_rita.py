# Data Anggaran
df_anggaran = id.read_excel(excel_path, sheet_name="Data Anggaran")

# Data Aparat
df_aparat = id.read_excel(excel_path, sheet_name="Data Aparat")

# Sensor Perangkat
df_sensor = id.read_excel(excel_path, sheet_name="Sensor Perangkat")

# Data Eksternal
df_eksternal = id.read_excel(excel_path, sheet_name="Data Eksternal")

# Contoh tampilkan jumlah baris per sheet
print("Jumlah data anggaran:", len(df_anggaran))
print("Jumlah data aparat:", len(df_aparat))
print("Jumlah sensor:", len(df_sensor))
print("Jumlah data eksternal:", len(df_eksternal))
