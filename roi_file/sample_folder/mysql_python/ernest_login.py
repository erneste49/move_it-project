import mysql.connector
print('mysql imported successfully')

db_connection = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "",
    database = "portal_db"
    )
print("mysql connection was successful")

my_cursor = db_connection.cursor()
print("my_cursor connected succesfully", my_cursor)

def signup(fname, email, pwd):
    try:    
        my_cursor.execute('USE portal_db')
        print("Database Table selected")
        my_cursor.execute(f"INSERT INTO user_information SET fullname= '{fname}', user_email = '{email}', user_password = '{pwd}'")
        print("User added to database")
            
    except mysql.connector.Error as er:
        print("Encountered error while connecting and adding data to database", er)
    
    print("last row id:", my_cursor.lastrowid)
    db_connection.commit()
    


def sign_in(email, pwd):
    try:
        query = "SELECT user_email, user_password FROM user_information WHERE user_email = %s AND user_password = %s"
        my_cursor.execute(query, (email,pwd))
        user = my_cursor.fetchone()
        if user:
            print("login Successful")
        else:
            print("Invalid user Login / user not found")
    except mysql.connector.Error as er:
        print("An error occured while trying to login", er)
    else:
        print("Thank you")
        
        
def display_list():
    my_cursor.execute("SELECT * FROM user_information")
    for info in my_cursor:
        print(info)
       
if __name__ == "__main__":
    uName = input("Enter fullname: ")
    uEmail = input("Enter email address: ")
    uPassword = input("Enter password: ")   




sign_in(uEmail, uPassword)
#signup(uName, uEmail, uPassword)
#display_list()

# my_cursor.close()
db_connection.close()
