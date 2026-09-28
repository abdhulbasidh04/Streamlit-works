import mysql.connector

class BloodDonor():
    def __init__(self):
        self.connection = mysql.connector.connect(user="root", password="root", host="localhost", database="blooddb")
        self.cursor = self.connection.cursor()
        print("successfully connected")
    def post(self,name,blood_group,phone,city,last_donation):
        query="insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s)"
        data=(name,blood_group,phone,city,last_donation)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("Data inserted successfully")
    def get(self):
        query="select * from donor"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            return records
        else:
            return False
    def get_id(self,id):
        query="select * from donor where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record = self.cursor.fetchone()
        if record:
            return record
        else:
            return False
    def put(self,id,name,blood_group,phone,city,last_donation):
        query="update donor set name=%s,blood_group=%s,phone=%s,city=%s,last_donation=%s where id=%s"
        data=(name,blood_group,phone,city,last_donation,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            return True
        else:
            return False
    def delete(self,id):
        query="delete from donor where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            return True
        else:
            return False
b=BloodDonor()