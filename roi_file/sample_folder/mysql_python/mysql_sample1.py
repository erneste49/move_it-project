import mysql.connector

print('mysql Import is working')


try:
    connection = mysql.connector.connect(
        user = "root",
        host = "localhost",
        password = "",
        database = "portal_db"
    )

    print('The database connection was successful', connection)
    print("Our sql_connector is connected", connection.is_connected() )
    # print("The server information is: ", connection.get_server_info() )
    # print("Version :", connection.get_server_version() )
    # print("**************mysql connector methods**************")
    # print(dir(connection))
    
    

    cursor = connection.cursor()
    print("Cursor connected successfully", cursor)
    
    cursor.execute("SHOW TABLES")
    for tables in cursor:
        print(tables)
        
    
    
    # cursor.execute("SHOW DATABASES")
    # for db in cursor:
    #     print(db)
    #print("Query Executed", cursor)
    
    #cursor.execute("INSERT INTO contact SET name='Atiku Abubakar', email = 'atk@yahoo.com' ")
    #print("contact added !")
    
    #u_name = 'peter A'
    #u_email = 'peter@gmail.com'
    
    # u_name = input('Enter your name')
    # u_email = input('Enter your email')
    # cursor.execute(f"INSERT INTO contact SET name='{u_name}', email = '{u_email}' ")
    # prnt("contact added !")
    
    # cursor.execute("SELECT * FROM contact")
    # for data in cursor:
    #     print(data)
    
#to get description about the table
    cursor.execute("DESCRIBE contact")
    for table in cursor:
        print(table)
    
    print("last row id:", cursor.lastrowid)
    connection.commit()
    
    cursor.close()
    connection.close()

except:
    print("connection failed, try again")
        
