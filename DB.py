import sqlite3


def Select_All():
    conn = sqlite3.connect('DataBase/Product_DB.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    results = cursor.fetchall()
    return results
    conn.close()

def Select_By_Id(text):
    conn = sqlite3.connect('DataBase/Product_DB.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * from product WHERE ID={}".format(text))
    results = cursor.fetchall()
    return results
    conn.close()

def Update_Line(Booker, Date, Costs, Status, Email, Id):
    conn = sqlite3.connect('DataBase/Product_DB.sqlite')
    cursor = conn.cursor()
    cursor.execute("update product set Заказчик='{}',Дата='{}',Оплата='{}',Статус='{}',Email='{}' where ID={}"
                   .format(Booker, Date, Costs, Status, Email, Id))
    conn.commit()
    conn.close()

def Insert_Line(Booker, Date, Costs, Status, Email):
    conn = sqlite3.connect('DataBase/Product_DB.sqlite')
    cursor = conn.cursor()
    cursor.execute("insert into product (Заказчик, Дата, Оплата, Статус, Email) values ('{}','{}',{},'{}','{}')"
                   .format(Booker, Date, Costs, Status, Email))
    conn.commit()
    conn.close()

def Remove_Line(text):
    conn = sqlite3.connect('DataBase/Product_DB.sqlite')
    cursor = conn.cursor()
    cursor.execute("delete from product where ID={}"
                   .format(text))
    conn.commit()
    conn.close()

def Get_Date():
    conn = sqlite3.connect('DataBase/Product_DB.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT Дата FROM product")
    results = cursor.fetchall()
    return results
    conn.close()