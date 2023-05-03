import streamlit as st

st.header(':blue[ini adalah aplikasi penjumlahan]')

st.write('silahkan input angka yang akan dihitung! :sunglasses:')

number1 = st.number_input('masukkan bilangan pertama')
st.write(f'bilangan pertama adalah {number1}')

number2 = st.number_input('masukkan bilangan kedua')
st.write(f'bilangan kedua adalah {number2}')

if st.button('hitung'):
	hasil = number1+number2
	st.success(f'hasil penjumlahan dari {number1} + {number2} = {hasil}', icon="✅")
else:
    st.write('silahkan klik tombol "hitung" jika ingin tahu hasilnya')