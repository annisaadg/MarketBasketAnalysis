from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(layout="wide",page_title="MBAV1")
st.write("""# Market Basket Analysis""")


df = pd.read_excel("datasets/Test2.xlsx")

with st.spinner('Harap tunggu,sedang memuat data...'):
    time.sleep(2)

def get_data(period_day = ''):
    data = df.copy()
    filtered = data.loc[
        data["period_day"].str.contains(period_day)
    ]
    return filtered if filtered.shape[0] else "No Result"

def user_input_features_period():
    period_day = st.selectbox("Period Day",["Morning", "Afternoon", "Evening","Night"])
    return period_day

period_day = user_input_features_period()

data = get_data(period_day.lower())

def encode(x):
    if x <= 0:
        return 0
    elif x >= 1:
        return 1

if type(data) != type("No Result"):
    item_count = data.groupby(["Transaction", "Item"])["Item"].count().reset_index(name="Count")
    item_count_pivot = item_count.pivot_table(index='Transaction', columns='Item', values='Count', aggfunc='sum').fillna(0)
    item_count_pivot = item_count_pivot.applymap(encode)

    support = 0.01
    frequent_items = apriori(item_count_pivot, min_support=support , use_colnames=True)

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

