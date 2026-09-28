import streamlit as s
from library_db import BookListCreateRetrieveUpdateDelete
s.title("READ A BOOK RECORD")
id=s.number_input("Enter the id",min_value=0)
btn=s.button("Display")
if btn:
    c=BookListCreateRetrieveUpdateDelete()
    records=c.retrieve(id)
    if records:
        s.write("Title",records[1])
        s.write("Author", records[2])
        s.write("Price", records[3])
        s.write("Pages", records[4])
        s.write("language",records[5])
    else:
        s.error("No record found")
