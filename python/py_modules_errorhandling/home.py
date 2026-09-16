import onboarding as onboard

# calling the signup function twicw
onboard.signup('ola', '1234')
onboard.signup('ade', '4444')

# printing the usernames and passwords list
print(onboard.usernames)
print(onboard.passwords)

# logging in user "ola" with one right password and one wrong password using the login function
onboard.login('ola', '1234')
onboard.login('ola', '4444')

# resetting user ola password using reset_password function
onboard.reset_password('ola', '1234', '2323')

#printing usernames and passwords list with updated values
print(onboard.usernames)
print(onboard.passwords)

# trying to login user ola with the old and new password that was reset
onboard.login('ola', '1234')
onboard.login('ola', '2323')







