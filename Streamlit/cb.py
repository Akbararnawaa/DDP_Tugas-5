import streamlit as st

nama = st.text_input("Masukkan nama Anda:")
umur = st.number_input("Masukkan umur Anda:")
alamat = st.text_input("Masukkan alamat Anda:")

submit_button = st.button("Submit")

