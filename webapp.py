import streamlit as st

st.title('PERHITUNGAN %RPD UNTUK DUA SAMPEL')
st.write('Dengan Memasukkan Nilai :green[Kadar Sampel 1] dan :green[Kadar Sampel 2]')
st.markdown('dengan rumus $\%RPD=(|kadar1-kadar2|/x̄ kadar)x100% $')

kadar1 = st.number_input('masukkan kadar pertama (dengan syarat nilai harus lebih besar)')
st.write(f'kadar pertama adalah {kadar1}')

kadar2 = st.number_input('masukkan kadar kedua')
st.write(f'kadar kedua adalah {kadar2}')

if st.button('hitung %RPD'):
	hasil1 = ((kadar1-kadar2)/((kadar1+kadar2)/2))*100
	st.success(f'hasil = {hasil1}')
else:
    st.write('silahkan klik tombol "hitung" jika ingin tahu hasilnya') 