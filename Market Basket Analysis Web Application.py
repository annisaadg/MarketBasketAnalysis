import streamlit as st
import base64
import streamlit.components.v1 as components

st.set_page_config(layout="wide",page_title="Intro")
#st.write("""# Market Basket Analysis Web Application""")

file_ = open("./img/original.jpg", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("./img/BG.png", "rb")
contents2 = file_.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file_.close()

url = f'''\
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>'''

st.markdown(f'{url}<div class="jumbotron" style="height:380px; background: url(data:image/gif;base64,{data_url2}); background-size:100% 100%; -webkit-background-size: 100% 100%; opacity: 0.9;"><h1 style="color:white"; class="text-center">Market Basket Analysis WebApp</h1><p align="center" style="color:white";>Proyek 2 Proyek Pengembangan Aplikasi Saintifik Aplikasi Sains Data</p></div></div>',
    unsafe_allow_html=True)

st.markdown(f'<div style="text-align:justify">Market Basket Analysis (MBA) atau Analisis Keranjang Belanja merupakan metode analisis data yang digunakan dalam dunia bisnis untuk memahami pola pembelian konsumen. Dengan menggunakan MBA, perusahaan dapat mempelajari hubungan antara produk yang dibeli oleh konsumen, sehingga dapat menemukan peluang untuk meningkatkan penjualan dan keuntungan mereka. Dalam web Market Basket Analysis, informasi mengenai pembelian produk dapat diperoleh dari data transaksi yang tersimpan dalam data set yang telah dimasukan. Dengan demikian, kita dapat menganalisis data tersebut untuk memahami kebiasaan pembelian konsumen  untuk membuat keputusan yang lebih baik. Pada web ini, kami akan menampilkan hasil dari Market Basket Analysis.</div>',unsafe_allow_html=True)
