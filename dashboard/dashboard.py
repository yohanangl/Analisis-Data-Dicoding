
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df= pd.read_csv("all_data.csv")


st.title('Dashboard Data Penyewaan Sepeda')
tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])
col1, col2, col3 = st.columns([2, 2, 2])

with tab1:
    st.header("Pengaruh Cuaca terhadap Tingkat Penggunaan Sepeda")
    st.header("Barplot")
    weather = all_df.groupby('weathersit_x')['cnt_y'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=weather, x='weathersit_x', y='cnt_y', palette='viridis')

    plt.title('Pengaruh Cuaca terhadap Tingkat Penggunaan Sepeda')  
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Cerah', 'Berawan', 'Hujan Ringan', 'Hujan Lebat'])
 
    st.pyplot(plt)

    st.header("Boxplot")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=all_df, x='weathersit_x', y='cnt_y', palette='viridis')

    plt.title('Distribusi Penggunaan Sepeda Berbagi Berdasarkan Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Peminjaman Sepeda')  

    st.pyplot(plt)

with tab2:
    st.header("Hubungan Antara Kelembaban, Kecepatan Angin, dan Jumlah Peminjaman Sepeda")
    st.header("Scatterplot")

    plt.figure(figsize=(10, 6))
    plt.scatter(all_df['temp_x'], all_df['windspeed_x'], c=all_df['cnt_x'], cmap='viridis', alpha=0.6)

    plt.title('Hubungan Antara Kelembaban, Kecepatan Angin, dan Jumlah Peminjaman Sepeda')
    plt.xlabel('Kelembaban')
    plt.ylabel('Kecepatan Angin')
    plt.colorbar(label='Jumlah Peminjaman Sepeda')

    st.pyplot(plt)

    st.header("Boxplot")

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=all_df, x='weathersit_x', y='cnt_y', hue='temp_x', palette='viridis')

    plt.title('Distribusi Penggunaan Sepeda Berdasarkan Cuaca, Kelembaban, dan Kecepatan Angin')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    plt.legend(title='Tingkat Kelembaban')
    plt.xticks(ticks=[0, 1], labels=['Cerah', 'Hujan'])

    st.pyplot(plt)
