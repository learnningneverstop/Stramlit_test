# -*- coding: utf-8 -*-
# @Time     : 2024/9/8 14:24
# @Author   : tupeng
# @File     : streamlit_app.py
# @project  : PyCharm

import streamlit as st
import numpy as np
import altair as alt
import pandas as pd


st.header("st.write")
st.sidebar.write("This is a sidebar.")
st.sidebar.selectbox("Select a car:", ("Ford", "Volvo", "Toyota"))
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Good bye!')

# 样例一
st.write("Hello, **world!** :sunglasses: ")
# 样例二
st.write(1234)
# 样例三
df = pd.DataFrame({
  'first column': list(range(1, 11)),
  'second column': np.arange(10, 101, 10)
})
st.write("Bellow is a dataframe:",df, "Above is a dataframe!")
# 样例四
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# 样例五
st.markdown("### This is a markdown text."
            "***this is a bold text***")