import streamlit as st 

st.title('PERHITUNGAN %RPD UNTUK SAMPEL DUPLO')
st.write('Dengan Memasukkan Nilai :green[Kadar Sampel 1] dan :green[Kadar Sampel 2]')

teori = st.text_input('Ketikkan "Teori" pada kolom dibawah,  jika ingin mengetahui teori singkat tentang %RPD')
if st.button('Submit'):
	st.info('Presesi adalah tingkat keterulangan hasil analisis untuk sampel yang homogen. Presisi salah satunya dapat dinyatakan sebagai RPD (Relative Percent Difference) untuk pengukuran duplo. Presisi (%RPD) adalah ukuran keragaman dari pengulangan hasil pengujian dari contoh uji yang menggunakan personil metode dan alat yang sama dalam suatu interval waktu')

st.markdown('Dengan rumus $\%RPD=(|Kadar1-Kadar2|/x̄ Kadar)x100%$')

kadar1 = st.number_input(':green[Masukan kadar pertama]')
st.write(f'Kadar pertama adalah {kadar1}')

kadar2 = st.number_input(':green[Masukan kadar kedua]')
st.write(f'Kadar kedua adalah {kadar2}')

if kadar1<kadar2:
	st.error('This is an error', icon="🚨")
	st.info('Masukan kadar pertama lebih besar kadar kedua')

if st.button('Hitung %RPD'):
	hasil1 = ((kadar1-kadar2)/((kadar1+kadar2)/2))*100
	st.success(f'Hasil (Dalam %) = {hasil1}')
else:
	st.write('Silakan klik tombol "hitung" jika ingin tahu hasilnya') 
	
if hasil1<5:
	st.info('%RPD < 5% dalam preparasi sampel ditanyakan sangat bagus')
else:
    st.write('%RPD > 6% dalam preparasi sampel dinyatakan kurang bagus, kemungkinan terjadi kesalahan dalam preparasi')

import time
import streamlit as st

with st.spinner('Wait for it...'):
    time.sleep(2)
st.success('Done!')