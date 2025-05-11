import streamlit as st
from backend import route_query


st.set_page_config(page_title="Knowledge Assistant", page_icon="🧠")
st.title("🧠 Knowledge Assistant")

query = st.text_input("Enter your question:")
if query:
    route, result = route_query(query)
    st.markdown(f"**Decision Path:** {route}")
    st.markdown(f"**Answer:** {result}")
