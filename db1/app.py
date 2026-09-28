import streamlit as s
from library_db import BookListCreateRetrieveUpdateDelete

tab1,tab2,tab3,tab4,tab5=s.tabs(['add','view','retrieve','delete','update'])
b=BookListCreateRetrieveUpdateDelete()

with tab1:
    s.title("Add")

with tab2:
    s.title("View")
with tab3:
    s.title("Retrieve")
with tab4:
    s.title("Delete")
with tab5:
    s.title("Update")