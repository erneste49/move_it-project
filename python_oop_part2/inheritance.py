
class User:
    
    def __init__(self, name):
        self._name = name
        
        
    def login(self):
        print(f"{self.name}  just Logged in ")
        
    def recover_password(self):
        print("Recovere password")
        
    def logout(self):
        print(f"{self.name} just Logged out!.")



class Admin(User):
    
    def __init__(self, name, email):
        super().__init__(name)
        self.__email = email    #making email a private member by adding __ to it
        print("This of the constructor in User class")
        
        
    def __login(self):      #making login() method a private member which can only be called within a class
        #self.recover_password()     #to call method in admin class
        super().recover_password()
        print("Admin login")
        
    def recover_password(self):
        self.__login()
        print(f"{self._name} - {self.__email} You need to send a message to the management to recover admin password")
        
    def add_new_user(self):
        print("New user added ")
    
admin1 = Admin("Ernest", "ernest@gmail.com")
#admin1.__login()   #gave an error because it is a private member 
# admin1.logout()
admin1.recover_password()
# print(admin1.name)
# print(admin1.__email)

user1 = User("roi")
#user1.login()
