from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(layout="wide",page_title="MBAV2")
st.write("""# MBA Versi 2""")

with st.spinner('Harap tunggu,sedang memuat data...'):
    time.sleep(2)

def get_data() -> pd.DataFrame:
    df = pd.read_csv("datasets/datasets2Encode.csv")
    return df

data = get_data()

if type(data) != type("No Result"):
    basket = data.pivot_table(index='BillNo' , columns='Itemname', values='Quantity').fillna(0)
    support = 0.02
    frequent_items = apriori(basket, min_support=support , use_colnames=True)

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
    item = st.selectbox("Pilih Item/Product",return_antecedents_df())
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
