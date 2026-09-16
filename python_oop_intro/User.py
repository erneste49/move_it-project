
class User:
    """This class contains properties/attributes and actions that a user can perform"""
    #attributes of the User 
    id = 100
    fullname = "Omosare Daniel"
    email = "omodan@gmail.com"
    phone = "09022334542"
    
    #actions that a User can perform: methods
    def register_user(self):
        return f"{self.fullname} registered successfully with {self.email}"
    
    def login_user(self, username, password):
        response = self.get_profile_details()
        return f"""
        Verifying credentials: {username} and {password}
        User logged in successfully 
        {response}"""
    
    def get_profile_details(self):
        return f"Fullname: {self.fullname} - E-mail: {self.email} - Phone: {self.phone}"
    

#how to create an object of user class --below is an object line 26
user1 = User() 

#how to call members of a class from outside the class
#we can't call register_user() alone we must use an object created from the class to call the method
#print(user1.register_user())
#print(f"The name of the object created is {user1.fullname} with email of {user1.email} and phone number of {user1.phone}")
#print(user1.get_profile_details())
print(user1.login_user("roi","12345"))   
    
    