import mysql.connector

class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(user="root",password="root",host="localhost",database="library_db")
        self.cursor=self.connection.cursor()
        print("successfully connected")
    def list(self):
        query = "select * from books"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            # for row in records:
            #     print(row)
            return records
        else:
            # print("no records")
            return False
    def create(self,title,author,price,pages,language):
        query="insert into books(title,author,price,pages,language) values(%s,%s,%s,%s,%s)"
        data=(title,author,price,pages,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("Data inserted successfully")

    def retrieve(self,id):
        query = "select * from books where id=%s"
        data =(id,)
        self.cursor.execute(query,data)
        record = self.cursor.fetchone()
        if record:
            # print(record)
            return record
        else:
            # print("no records")
            return False
    def update(self,id,title,author,price,pages,language):
        query="update books set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data=(title,author,price,pages,language,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            return True
            # print("Data updated")
        else:
            return False
    def delete(self,id):
        query="delete from books where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0: # if no updation rowcount return 0
            # print("Data is deleted")
            return True
        else:
            # print("No record found")
            return False
book_instance=BookListCreateRetrieveUpdateDelete()
# book_instance.list()
# book_instance.create("python2","van de",400,300,"Eng")
# book_instance.retrieve(2)
# book_instance.update(3,"React","Derossom",800,1500,"Javascript")
# book_instance.delete(7)