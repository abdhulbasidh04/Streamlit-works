import streamlit as s
from blooddb import BloodDonor

tab1,tab2,tab3,tab4,tab5=s.tabs(["Add","View","Retrieve","Update","Delete"])
b=BloodDonor()

with tab1:
    s.title("ADD New Donor")
    name=s.text_input("Enter the Name")
    blood_group=s.text_input("Enter the Blood Group")
    phone=s.number_input("Phone Number",min_value=0)
    city=s.text_input("City")
    last_donation=s.date_input("Enter the date")
    btn=s.button("Add")
    if btn:
        b.post(name,blood_group,phone,city,last_donation)
        s.success("Data Inserted Successfully")
with tab2:
    s.title("View All Records")
    btn=s.button("Display")
    if btn:
        records=b.get()
        s.table(records)
with tab3:
    s.title("View A Donor Record ")
    id = s.number_input("Enter the id", min_value=0)
    btn = s.button("View")
    if btn:
        records = b.get_id(id)
        if records:
            s.write("Name: ", records[1])
            s.write("Blood Group: ", records[2])
            s.write("Phone: ", records[3])
            s.write("City: ", records[4])
            s.write("Last Donation", records[5])
        else:
            s.error("No record found")
with tab4:
    s.title("Update Record")
    id=s.number_input("Enter the donor id",min_value=0)
    name=s.text_input("Enter the donor Name")
    blood_group=s.text_input("Enter the Blood_Group")
    phone=s.number_input("Phone donor Number",min_value=0)
    city=s.text_input("city")
    last_donation=s.date_input("Enter the last_date")
    btn=s.button("Update")
    if btn:
        records=b.put(id,name,blood_group,phone,city,last_donation)
        if records:
            s.success("Data Updated Successfully")
        else:
            s.error("No Data Found")
with tab5:
    s.title("DELETE RECORD")
    id = s.number_input("Enter id", min_value=0)
    btn = s.button("Delete")
    if btn:
        records = b.delete(id)
        if records:
            s.success("Data Deleted Successfully")
        else:
            s.error("No Record Found")
