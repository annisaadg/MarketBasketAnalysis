from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.frequent_patterns import fpgrowth
import streamlit as st
import pandas as pd
import numpy as np
import time
from xlsx2csv import Xlsx2csv

st.set_page_config(layout="wide",page_title="MBAV3")
st.write("""# MBA Versi 3""")

with st.spinner('Harap tunggu,sedang memuat data...'):
    time.sleep(3)

def get_data() -> pd.DataFrame:
    df = pd.read_csv('datasets/Online Retail.csv', sep = ',')
    return df

data = get_data()

def user_input_features_country():
    country = st.selectbox("Country",data["Country"].unique())
    return country

country = user_input_features_country()

data = data[data["Country"].str.contains(country)]
data.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
data = data[~data['InvoiceNo'].str.contains('C')]

def encode(x):
    if x <= 0:
        return 0
    elif x >= 1:
        return 1

if type(data) != type("No Result"):
    basket2 = (data.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().reset_index().fillna(0).set_index('InvoiceNo'))
    basket_sets2 = basket2.applymap(encode)

    support = 0.02
    frequent_items = fpgrowth(basket_sets2.astype('bool'), min_support=support , use_colnames=True)

    metric = "lift"
    min_threshold = 1

    rules = association_rules(frequent_items, metric=metric, min_threshold=min_threshold)[["antecedents","consequents","support","confidence","lift"]]
    rules.sort_values('confidence', ascending=False, inplace=True)

def parse_list(x):
    x = list(x)
    if len(x) == 1:
        return x[0]
    elif len(x) > 1:
        return ", " .join(x)

def return_antecedents_df():
    data = rules[["antecedents", "consequents"]].copy()
    data["antecedents"] = data["antecedents"].apply(parse_list)
    data["consequents"] = data["consequents"].apply(parse_list)

    return list(data["antecedents"].unique())

def user_input_features():
    item = st.selectbox("Item",return_antecedents_df())
    return item

item = user_input_features()

def return_item_df(item_antecendents):
    data = rules[["antecedents", "consequents"]].copy()
    data["antecedents"] = data["antecedents"].apply(parse_list)
    data["consequents"] = data["consequents"].apply(parse_list)

    return list(data.loc[data["antecedents"] == item_antecendents].iloc[0,:])

if type(data) != type("No Result"):
    st.markdown("Hasil Rekomendasi : ")  
    st.success(f"Jika Konsumen Membeli **{item}**, maka membeli **{return_item_df(item)[1]}** secara bersamaan")  