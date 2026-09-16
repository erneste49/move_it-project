
chatup_users = {
"David":['Funke','Abim','Ben','Roman'],
"Farid":['Olumide','Tade','Grace'],
"Peace":['Glory','Ada','Funke','Falz']
}

new_user = {"Ernest":['Abim','Ben','Funke','Falz']}
nameof_user = 'Ernest'

print(nameof_user,'connect with other users on this platform. ')
print('suggested friends:')

friend = 0
for user1 in chatup_users['David']:
    if user1 in new_user['Ernest']:
        friend += 1
print('David : has', friend, 'mutual friends')

friend = 0
for user2 in chatup_users['Farid']:
    if user2 in new_user['Ernest']:
        friend += 1
print('Farid : has', friend, 'mutual friends')

friend = 0
for user3 in chatup_users['Peace']:
    if user3 in new_user['Ernest']:
        friend += 1
print('Peace : has', friend, 'mutual friends')
