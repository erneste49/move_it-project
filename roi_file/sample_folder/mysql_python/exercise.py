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

def register():
    # my_cursor.execute("USE user")
    # print("Database selected")
    fullname = input('Enter your name: ')
    email = input('Enter your email: ')
    pasword = input('Enter your password: ')
    
    my_cursor.execute(f"INSERT INTO user_table SET fullname='{fullname}', email = '{email}', password='{pasword}' ")
    print("contact added !")
    
    my_cursor.execute("SELECT * FROM user_table")
    for info in my_cursor:
        print(info)
    
    print("last row id:", my_cursor.lastrowid)
    connection1.commit()
        
    
    
    
register()

my_cursor.close()
connection1.close()