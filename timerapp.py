import streamlit as st
import time as t
from datetime import time 
setTimer=st.time_input('Set timer',value=time(0,0,0))
progressPercent=st.empty()
def convertToSec(value):
    m,s,mm=value.split(':')
    totalSec=   int(m)*60+int(s)+int(mm)/1000
    return totalSec
if(str(setTimer)=='00:00:00'):
    st.write('Please set timer')
else:
    totalSec=convertToSec(str(setTimer))
    bar=st.progress(0)
    per=totalSec/100
    for i in range(100):
        bar.progress(i+1)
        progressPercent.write(str(i+1)+"%")
        t.sleep(per)