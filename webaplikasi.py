import streamlit as st

st.sidebar.title('Navigasi')
menu = st.sidebar.radio('Menu', ['Teori', 'Perhitungan'])

if menu == 'Teori':
    st.title('PERHITUNGAN %RPD UNTUK SAMPEL DUPLO')
    st.info('Presesi adalah tingkat keterulangan hasil analisis untuk sampel yang homogen. Presisi salah satunya dapat dinyatakan sebagai RPD (Relative Percent Difference) untuk pengukuran duplo. Presisi (%RPD) juga merupakan ukuran keragaman dari perulangan hasil pengujian dari contoh uji yang menggunakan personil metode dan alat yang sama dalam satu interval waktu. Untuk pengukuran preparasi sampel secara duplo perhitungan nya menggunakan relative percent difference ( %RPD ) untuk mengetahui tingkat ketelitian dari suatu preparasi yang telah dilakukan dengan rentang <5% yaitu semakin kecil nilai %RPD maka semakin teliti,  apabila >5% maka preparasi yang dilakukan kurang bagus karena tingkat ketelitian lebih besar dari rentang yang telah ditentukan atau terjadi nya kesalahan pada saat preparasi sampel. %RPD spesifik digunakan untuk perhitungan sampel pada pengukuran menggunakan alat spektrofotometri uv-vis.')
    st.markdown('Dengan rumus $\%RPD=(|Kadar1-Kadar2|/\\bar{Kadar})\\times100%$')


elif menu == 'Perhitungan':
    st.title('PERHITUNGAN %RPD UNTUK SAMPEL DUPLO')
    st.write('Dengan Memasukkan Nilai :green[Kadar Sampel 1] dan :green[Kadar Sampel 2]')
    
    kadar1 = st.number_input(':green[Masukkan kadar pertama]')
    st.write(f'Kadar pertama adalah {kadar1}')
    
    kadar2 = st.number_input(':green[Masukkan kadar kedua]')
    st.write(f'Kadar kedua adalah {kadar2}')
    
    if st.button('Hitung %RPD'):
        if kadar1 + kadar2 != 0:
            hasil1 = (abs(kadar1 - kadar2) / ((kadar1 + kadar2) / 2)) * 100
            st.success(f'Hasil (Dalam %) = {hasil1}')
        else:
            st.warning('Penyebut rumus tidak boleh nol')
    else:
        st.write('Silakan klik tombol "Hitung" untuk mendapatkan hasilnya')
    
    if 'hasil1' in locals() and hasil1 is not None:
        if hasil1 <= 5:
            st.info('%RPD < 5% preparasi sampel yang dilakukan dinyatakan semakin teliti')
        else:
            st.write('%RPD > 5% preparasi sampel yang dilakukan dinyatakan kurang teliti, kemungkinan terjadi kesalahan dalam preparasi')
