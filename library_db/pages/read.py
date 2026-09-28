import streamlit as s
s.title("READ ALL BOOK RECORDS")

from library_db import BookListCreateRetrieveUpdateDelete

c=BookListCreateRetrieveUpdateDelete()
records=c.list()
# print("hello")
# print(records)
s.table(records)
