import streamlit as st
forms=st.form("form1")
forms.text_input("First Name")
forms.form_submit_button("Submit")

with st.form('form2',clear_on_submit=True):
    col1,col2=st.columns(2)
    f_name=col1.text_input('First Name' )
    l_name=col2.text_input('Last Name')
    st.text_input('Enter Address')
    st.text_input('Password')
    st.text_input('Confirm Password')
    day,mon,year=st.columns(3)
    day.text_input('Date')
    mon.text_input('month')
    year.text_input('Year')
    submit_form=st.form_submit_button('Submit')
    if submit_form:
        if f_name=="" and l_name=="":
            st.error("Please Fill all the fields")
        else:
            st.success("Submitted successfully")