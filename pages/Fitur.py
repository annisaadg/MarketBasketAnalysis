from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time
import base64

st.set_page_config(layout="wide",page_title="Fitur")
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Fitur ",
    ("Stock Recommendation","Bundling Package Recommendation")
)

if(add_selectbox == "Stock Recommendation"):
    st.write("""# Stock Recommendation""")


    df = pd.read_excel("datasets/Test2.xlsx")

    with st.spinner('Harap tunggu,sedang memuat data...'):
        time.sleep(1)

    data = df.copy()
    def get_top5_item():
        data = df.copy()
        top5items = pd.DataFrame(data["Item"].value_counts())
        top5items = top5items.reset_index()
        top5items.columns = ["Item", "Count"]
        return top5items

    plt.figure(figsize=(13,5))
    sns.set_palette("muted")

    sns.barplot(x = data["Item"].value_counts()[:20].index,
                y = data["Item"].value_counts()[:20].values)
    plt.xlabel(""); plt.ylabel("")
    plt.xticks(size = 13, rotation = 45)
    plt.title('20 Produk Terlaris', size = 17)


    # Add figure in streamlit app
    st.pyplot(plt)

elif (add_selectbox == "Bundling Package Recommendation"):
    st.write("""# Bundling Package Recommendation""")
    file_ = open("./img/PK1.png", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    file_ = open("./img/PK2.png", "rb")
    contents2 = file_.read()
    data_url2 = base64.b64encode(contents2).decode("utf-8")
    file_.close()

    file_ = open("./img/PK3.png", "rb")
    contents3 = file_.read()
    data_url3 = base64.b64encode(contents3).decode("utf-8")
    file_.close()

    file_ = open("./img/PK4.png", "rb")
    contents4 = file_.read()
    data_url4 = base64.b64encode(contents4).decode("utf-8")
    file_.close()

    url = f'''\
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>'''

    st.markdown(f'{url}<div class="card-group"><div class="card"><img class="card-img-top" src="data:image/gif;base64,{data_url}"></div><div class="card"><img class="card-img-top" src="data:image/gif;base64,{data_url2}"></div></div><br><div class="card-group"><div class="card"><img class="card-img-top" src="data:image/gif;base64,{data_url3}"></div><div class="card"><img class="card-img-top" src="data:image/gif;base64,{data_url4}"></div></div>',
        unsafe_allow_html=True)

