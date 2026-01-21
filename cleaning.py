import pandas as pd

def clean_data():
    df = pd.read_excel("data/data_kebun.xlsx")
    print(df.dtypes)
    df.columns = df.columns.str.strip().str.lower()
    
    #Menghapus data kosong
    df - df.dropna()

    #Format Tanggal
    df["tanggal"] = pd.to_datetime(df["tanggal"])

    #Produksi Int
    df["produksi"] = pd.to_numeric(df["produksi"], errors="coerce")  
    return df