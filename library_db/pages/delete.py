import streamlit as s
from library_db import BookListCreateRetrieveUpdateDelete
s.title("DELETE BOOK RECORD")
id=s.number_input("Enter id",min_value=0)
btn=s.button("Delete")
if btn:
    c=BookListCreateRetrieveUpdateDelete()
    records=c.delete(id)
    if records:
        s.success("Data Deleted Successfully")
    else:
        s.error("No Record Found")

