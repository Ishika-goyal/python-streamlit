import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

chart_data=pd.DataFrame(np.random.randn(20,3),columns=['Line1','Line2','Line3'])
st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)
df=pd.read_csv('../iris.csv')
fig=plt.figure(figsize=(15,8))

st.dataframe(df)
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)
