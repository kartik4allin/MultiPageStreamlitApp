import streamlit as st
from st_pages import Page, show_pages, hide_pages

show_pages([
    Page("main.py","Main"),
    Page("nextpage.py","NextPage"),
    Page("thankyou.py","ThankYouPage")
])
hide_pages(['Main'])
hide_pages(['NextPage'])
hide_pages(['ThankYouPage'])

st.page_link("main.py", label="Home", icon="🏠")

st.write("You are in Thank You Page")