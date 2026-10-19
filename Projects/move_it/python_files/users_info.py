import mysql.connector

class Users:
    
    def __init__(self):
        try:
            self.my_connection = mysql.connector.connect(
            user = "root",
            host = "localhost",
            password = "",
            database = "moveit_db" 
            )
            #print("Connection successful")
            self.my_cursor = self.my_connection.cursor()
            #print("cursor connected")
            
            # self.my_cursor.execute("USE moveit_db")
            #self.my_cursor.execute("SHOW tables")
            for list in self.my_cursor:
                print(list)
        except mysql.connector.Error as errors:
            print("Something went wrong: ", errors)
    
    def register_user(self, names, phone, email, address, pwd, pwdhint):
         self.my_cursor.execute(f"INSERT INTO users_infos SET fullname ='{names}', phone = '{phone}', email ='{email}', address='{address}', password='{pwd}', password_hint='{pwdhint}' ")
         
         self.my_connection.commit()
         return f"{names} successfully Registered"
    
    def login_user(self):
        pass
    
    def show_registered_users(self):
        self.my_cursor.execute("SELECT * FROM users_infos ")
        for each_user in self.my_cursor:
            print(each_user)
    
    def close_connection(self):
        self.my_connection.close()
        print("Thank you!.")
    
def input_info():
    name = input("Enter your fullname: ")
    phone =input("Enter your phone Number: ")
    email =input("Enter your email: ")
    address =input("Enter your address: ")
    pwd =input("choose your unique password: ")
    pwdhint =input("Enter your password hint: ")
    return name, phone, email, address, pwd, pwdhint
   
   
 
roi = Users()
user_data = input_info()   #assigning function to a variable/string
#print(roi.register_user("roi ernest", "09155511654", "roiernest01@gmail.com", "22 Shomolu Lagos State", "roi123ns", "nickname 123 me" ))   #supplying values as arguments for the parameter
#print(roi.register_user(*user_data))   #supply values for parameter by entering values from keyboard
print("-------------------------------------------------------------------------")  
roi.show_registered_users() #to view list of registered users in db
print("-------------------------------------------------------------------------")
roi.close_connection()    
print("")
print("")
 
   
   
class Sellers:
    
    def __init__(self):
        try:
            self.my_connection = mysql.connector.connect(
            user = "root",
            host = "localhost",
            password = "",
            database = "moveit_db" 
            )
            #print("Connection successful")
            self.my_cursor = self.my_connection.cursor()
            #print("cursor connected")
                    
            # self.my_cursor.execute("USE moveit_db")
            #self.my_cursor.execute("SHOW tables")
            #for list in self.my_cursor:
                #print(list)
        except mysql.connector.Error as errors:
            print("Something went wrong: ", errors)
        
        
seller1 = Sellers()  
print("------")
#seller1.__init__()
   
   
   
   
   







 
