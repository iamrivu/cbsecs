import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root")

print("..........................................................")
print("Interact with database(SQL/MySQL) from console")
print("..........................................................")
print("showdb -> Show databases")
print("showtable -> Show tables")
print("fetch -> Fetch all data from a table")
print("insert -> Insert data in a table")
print("update -> Update a table row")
print("delete -> Delete a table row")
print("q -> Exit this program")
print("..........................................................")
lup = 1
while lup == 1:
    print("\n")
    userInpt = input("Type your query : ")

    if userInpt == "showdb":
        def dbShow():
            conn = mydb.cursor()
            conn.execute("show databases")

            for i in conn:
                print (i)      
        dbShow()
    elif userInpt == "showtable":
        def dbTblShow():
            mydb = mysql.connector.connect(host="localhost", user="root", db="YOUR_DB_NAME")
            connQry = mydb.cursor()
            connQry.execute("show tables")

            for i in connQry:
                print(i)
        dbTblShow()
    elif userInpt == "fetch":
        def dbQuerySelect():
            mydb = mysql.connector.connect(host="localhost", user="root", db="YOUR_DB_NAME")
            connQry = mydb.cursor()
            connQry.execute("select * from YOUR_TABLE_NAME")

            for i in connQry:
                print(i)
        dbQuerySelect()
    elif userInpt == "insert":
        def dbQueryIn():
            mydb = mysql.connector.connect(host="localhost", user="root", db="YOUR_DB_NAME")
            connQry = mydb.cursor()
            connQry.execute("INSERT QUERY HERE")
            print("Data sucessfully inserted")
        dbQueryIn()
    elif userInpt == "update":
        def dbQueryUp():
            mydb = mysql.connector.connect(host="localhost", user="root", db="YOUR_DB_NAME")
            connQry = mydb.cursor()
            connQry.execute("UPDATE QUERY HERE")
            print("Data sucessfully updated")
        dbQueryUp()
    elif userInpt == "delete":
        def dbQueryDel():
            mydb = mysql.connector.connect(host="localhost", user="root", db="YOUR_DB_NAME")
            connQry = mydb.cursor()
            connQry.execute("DELETE QUERY HERE")
            print("Data sucessfully deleted")
        dbQueryDel()
    elif userInpt == "q":
        print("Successfully exited")
        break
    else:
        print("Invalid input!!")