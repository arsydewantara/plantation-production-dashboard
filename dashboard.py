import streamlit as st
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kebun_db"
)

df = pd.read_sql("SELECT * FROM produksi_harian",
conn)

st.title("Dashboard Produksi Kebun")
st.dataframe(df)
st.bar_chart(df.groupby("afdeling")["produksi"].sum())