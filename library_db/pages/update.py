import streamlit as s
from library_db import BookListCreateRetrieveUpdateDelete
s.title("UPDATE BOOK RECORD")
id=s.number_input("Enter the id",min_value=0)
title=s.text_input("Title")
author=s.text_input("Author")
price=s.number_input("Price",min_value=0)
pages=s.number_input("Pages",min_value=0)
language=s.text_input("Language")
btn=s.button("Update")
if btn:
    c=BookListCreateRetrieveUpdateDelete()
    records=c.update(id,title,author,price,pages,language)
    if records:
        s.success("Record Updated Successfully")
    else:
        s.error("No record found")