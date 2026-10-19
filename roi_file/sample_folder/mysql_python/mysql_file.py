import mysql.connector

print('mysql Import is working')

connection1 = mysql.connector.connect(
        user = "root",
        host = "localhost",
        password = "",
        database = "user"
)
        
my_cursor = connection1.cursor()
print("Cursor connected successfully", my_cursor)

def register(fullname, email, password2):
    try:
        my_cursor.execute("USE user")
        print("Database selected")
        # fullname = input('Enter your name: ')
        # email = input('Enter your email: ')
        # pasword2 = input('Enter your password: ')
#adding many files        
        sql_query = "INSERT INTO user_table (fullname, email, password) VALUES (%s, %s, %s)"
        query_data_values = [
            ("jude", "jude@gmail.com", "55443" ),
            ("steve", "steve@gmail.com", "32134" ),
            ("paul", "paul@gmail.com", "71223" ),
            ("tom", "tom@gmail.com", "14432" ),
            (fullname, email, password2 )
            ]
#to add one query
        my_cursor.executemany(sql_query, query_data_values)
        print("query_data_added")
#to add multiple query
        # my_cursor.executemany(sql_query, query_data_values)
        # print("query_data_added")
        
        # my_cursor.execute(f"INSERT INTO user_table SET fullname='{fullname}', email = '{email}', password='{pasword}' ")
        # print("contact added !")
        
        my_cursor.execute("SELECT * FROM user_table WHERE id > 5")
        rows1 = my_cursor.fetchall()
        #rows2 = my_cursor.fetchmany(10)
        #rows3 = my_cursor.fetchone
        
        # for rows in my_cursor:
        #     print(rows)
        
        for rows in rows1:
            print(rows[1],rows[2] )
        
        # for row in rows2:
        #     print(row[1],row[2] )
        
        print("last row id:", my_cursor.lastrowid)
        connection1.commit()
    except mysql.connector.Error as er:
        print("An error occured when connecting and adding data", er)   
    
    
fullname = input('Enter your name: ')
email = input('Enter your email: ')
password2 = input('Enter your password: ')
    
register(fullname, email, password2)

my_cursor.close()
connection1.close()