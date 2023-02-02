import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
from datetime import datetime, timedelta

apptitle = 'Internship 1 - Helmi Salsabila - 1194018'
st.set_page_config(page_title=apptitle, page_icon=":eyeglasses:")

st.title('Website')
st.title('Peramalan Waktu Pengiriman Outbound')

st.markdown("""
 * Universitas Logistik dan Bisnis Internasional
 * Helmi Salsabila - 1194018
""")

# Membaca model
rfr = pkl.load(open('rfr.pkl', 'rb'))

st.markdown("## Silahkan Inputkan Data")

# Algoritma
menu = st.selectbox('Model', ['RandomForestRegressor'])

def calculate_outbound_date(product_id, qty, inbound_date):
    res = int(rfr.predict([[product_id, qty]])[0])
    date = datetime.strptime(inbound_date, "%Y-%m-%d")
    outbound_date = date + timedelta(days=res)
    return outbound_date

forecasting = ''
if menu == 'RandomForestRegressor':
    def inputan():
        input_product_id = st.number_input('Product ID', 0)
        st.markdown("""
                    Contoh Product ID:
                    * 92247686
                    """)
        input_qty = st.number_input('Quantity', 0)
        inbound_date = st.date_input('Inbound Date', datetime.now())
        data = {
            'product_id': input_product_id, 
            'qty': input_qty,
            'inbound_date': str(inbound_date) 
        }
        return data
    
    inputan_user = inputan()
    res = int(rfr.predict([[inputan_user['product_id'], inputan_user['qty']]]))
    date = calculate_outbound_date(inputan_user['product_id'], inputan_user['qty'], inputan_user['inbound_date'])
    st.write('Hasil Prediksi: ', res)
    st.write('Prediksi Outbound: ', date)

