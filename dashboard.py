import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

file_path = 'ADANA SECIM.xlsx'

df = pd.read_excel(file_path)

st.set_option('deprecation.showPyplotGlobalUse', False)

districts = df['İlçe'].unique().tolist()

neighborhoods = {}
for district in districts:
    neighborhoods[district] = df[df['İlçe'] == district]['Mahalle adı'].unique().tolist()

st.title("Adana- Mahalle Seçim Sonuçları")

selected_district = st.selectbox("İlçe Seçiniz", districts)

if selected_district:
    selected_neighborhood = st.selectbox("Mahalle Seçiniz", neighborhoods[selected_district])

if selected_district and selected_neighborhood:
    filtered_df = df[
        (df['İlçe'] == selected_district) & (df['Mahalle adı'] == selected_neighborhood)
    ]
    
    vote_counts = filtered_df.iloc[:, 8:].sum()

    # Create a colorful pie chart
    plt.figure(figsize=(6, 6))
    vote_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title(f"{selected_district} - {selected_neighborhood} Oy Dağılımı")
    st.pyplot(plt.show())
    



