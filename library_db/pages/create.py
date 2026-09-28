import streamlit as s
from library_db import BookListCreateRetrieveUpdateDelete
s.title("CREATE NEW BOOK RECORD")
title=s.text_input("Title")
author=s.text_input("Author")
price=s.number_input("Price",min_value=0)
pages=s.number_input("Pages",min_value=0)
language=s.text_input("Language")
btn=s.button("Add Book")
if btn:
    c=BookListCreateRetrieveUpdateDelete()
    c.create(title,author,price,pages,language)
    s.success("Record Created Successfully")