import mysql.connector

class Participant:
     
    def __init__(self):
        try:
            self.my_connection = mysql.connector.connect(
            user = "root",
            host = "localhost",
            password = "",
            database = "user"
            )
            #print("connection to Database successful")
            self.my_cursor = self.my_connection.cursor()
            #print("cursor connected")
        except mysql.connector.Error as error:
            print("Error connecting to Database or Cursor", error)
            
    
    def register_participant(self, Userfullname, Useremail, Userpassword):
        self.my_cursor.execute(f"INSERT INTO user_table SET fullname='{Userfullname}', email='{Useremail}', password='{Userpassword}' ")     
        self.my_connection.commit()
        return f"Participant with name {Userfullname} was Successfully Registered"
    
    
    def login_participant(self, Useremail, Userpassword ):
        try:
            query1 = "SELECT * FROM user_table WHERE email = %s AND password = %s"
            self.my_cursor.execute(query1, (Useremail, Userpassword))
            user = self.my_cursor.fetchone()
            if user:
                return f"You are logged in"
            else:
                return "Invalid login credentials"
        except mysql.connector.Error as error:
            print("An error occured", error)
    
    
    def show_db(self):
        self.my_cursor.execute("SELECT * FROM user_table")
        for record in self.my_cursor:
            print(record)
         
            
    def close_database(self):
        #self.my_cursor.close()
        self.my_connection.close()
        print("Thank you!")
            
       
    
user1 = Participant()

#print(user1.register_participant("ernest eze", "ernest@gmail.com", "e12e22"))  #used to register new participant
print('---------------------------------------------------------------')
print(user1.login_participant("ernest@gmail.com", "e12e22"))   #used to login participant with correct information
print('---------------------------------------------------------------')
print(user1.login_participant("ernest@gmail.com", "e12e23"))    #attempting to login participant with wrong password
print('---------------------------------------------------------------')
user1.show_db()     #used to show table records in database

user1.close_database()  #used to close the connection
