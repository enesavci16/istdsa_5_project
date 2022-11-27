
import main


import warnings

import streamlit as st
import main


a=get_recommendations(st.text_input("Entry jobs:"))
b=get_recommendations(st.text_input("Entry jobs:"))
c=get_recommendations(st.text_input("Entry jobs:"))

sonuc_1=a.intersection(b)
sonuc_2=a.intersection(c)
sonuc_3=b.intersection(c)
sonuc_4=a.intersection(b).intersection(c)
sonuc=sonuc_1.union(sonuc_2).union(sonuc_3).union(sonuc_4)

print(sonuc)
st.write(sonuc)