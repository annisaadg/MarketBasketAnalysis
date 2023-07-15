from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.frequent_patterns import fpgrowth
import streamlit as st
import pandas as pd
import time


st.set_page_config(layout="wide",page_title="Performance")
st.write("""# Performance""")

with st.spinner('Harap tunggu,sedang memuat data...'):
    time.sleep(3)

def get_data() -> pd.DataFrame:
    df = pd.read_csv("./datasets/datasets2Encode.csv")
    return df

data = get_data()

def rulesbyapriori(data):
    basket = data.pivot_table(index='BillNo' , columns='Itemname', values='Quantity').fillna(0) 

    start_time = time.time()
    support = 0.02
    frequent_items = apriori(basket, min_support=support , use_colnames=True)
    end_time = time.time()
    diffTime = end_time - start_time

    metric = "lift"
    min_threshold = 1

    rules = association_rules(frequent_items, metric=metric, min_threshold=min_threshold)[["antecedents","consequents","support","confidence","lift"]]
    rules.sort_values('confidence', ascending=False, inplace=True)

    return rules,diffTime

def rulesbyfpgrowth(data):
    basket = data.pivot_table(index='BillNo' , columns='Itemname', values='Quantity').fillna(0) 

    start_time = time.time()
    support = 0.02
    frequent_items = fpgrowth(basket, min_support=support , use_colnames=True)
    end_time = time.time()
    diffTime = end_time - start_time
    metric = "lift"
    min_threshold = 1

    rules = association_rules(frequent_items, metric=metric, min_threshold=min_threshold)[["antecedents","consequents","support","confidence","lift"]]
    rules.sort_values('confidence', ascending=False, inplace=True)

    return rules,diffTime

def parse_list(x):
    x = list(x)
    if len(x) == 1:
        return x[0]
    elif len(x) > 1:
        return ", " .join(x)

aprio = rulesbyapriori(data)[0]
aprioTime = rulesbyapriori(data)[1]
aprio["antecedents"] = aprio["antecedents"].apply(parse_list)
aprio["consequents"] = aprio["consequents"].apply(parse_list)

fpgrow = rulesbyfpgrowth(data)[0]
fptime = rulesbyfpgrowth(data)[1]
fpgrow["antecedents"] = fpgrow["antecedents"].apply(parse_list)
fpgrow["consequents"] = fpgrow["consequents"].apply(parse_list)

st.markdown("## Apriori")
st.write(aprio)
st.markdown(f'Waktu Estimasi pencarian Frequent Itemset : {aprioTime} seconds')
st.markdown("## fpgrowth")
st.write(fpgrow)
st.markdown(f'Waktu Estimasi pencarian Frequent Itemset : {fptime} seconds')
