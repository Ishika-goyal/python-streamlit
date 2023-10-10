import streamlit as st
import pandas as pd
st.title('Welcome to streamlit tutorial Hello :green[ Geeks] :mortar_board:')
st.header("This is header",divider='rainbow')
st.subheader("This is :blue[subheader]")
st.text("Hello world")
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
           :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
st.caption('A caption with _italics_ and :blue[blue color ] with an emoji :sunglasses:')
st.success("successfully submitted")
st.info("Information in this area")
st.warning("This is inappropriate")
st.error("error message displayed")
st.exception(ZeroDivisionError('division by 0 not possible '))
st.write('range(1,10)')
st.code('x=10\n'
            'for i in range(x):\n'
            '\tprint(i)')

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.write(edited_df(edited_rows))
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")