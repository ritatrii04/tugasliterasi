# Data Anggaran
df_anggaran = pd.read_excel(excel_path, sheet_name="Data Anggaran")

# Data Aparat
df_aparat = pd.read_excel(excel_path, sheet_name="Data Aparat")

# Sensor Perangkat
df_sensor = pd.read_excel(excel_path, sheet_name="Sensor Perangkat")

# Data Eksternal
df_eksternal = pd.read_excel(excel_path, sheet_name="Data Eksternal")

# Contoh tampilkan jumlah baris per sheet
print("Jumlah data anggaran:", len(df_anggaran))
print("Jumlah data aparat:", len(df_aparat))
print("Jumlah sensor:", len(df_sensor))
print("Jumlah data eksternal:", len(df_eksternal))
