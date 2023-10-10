import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
graphSelected=st.sidebar.radio('Select A Graph',options=('Sin','cos','tan'))
x_axis=np.linspace(0,4*np.pi,100)
tanx_axis=np.linspace(0,10000)

if graphSelected=='Sin':
    fig=plt.figure()
    plt.plot(x_axis,np.sin(x_axis))
    st.write(fig)
elif graphSelected=='cos':
    fig=plt.figure()
    plt.plot(x_axis,np.cos(x_axis))
    st.write(fig)
elif graphSelected=='tan':
    fig=plt.figure()
    plt.plot(tanx_axis,np.tan(tanx_axis))
    st.write(fig)

