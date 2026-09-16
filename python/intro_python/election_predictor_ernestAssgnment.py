party = 'APC'
print('WELCOME TO ELECTION PARTICIPATION WEBSITE')
candidate_name = input('please enter your name: ')
print('Welcome', candidate_name)
candidate_dob = input('What year were you born in: ')
age = 2026 - int(candidate_dob)
political_party = input('Which political party do you belong to? ')

if age >= 70:
    print('Hello', candidate_name, 'You are', age, 'years old, Therefore you can contest in the Election.')
elif age >= 70 or political_party.upper() == party:
    print('Hello', candidate_name,'You are', age, 'years old, and belong to', political_party.upper(), 'party, Therefore you can contest in the Election.')
elif age < 70 and political_party != party:
    print('Hello', candidate_name,'You are', age, 'years old, which is below the required age, Therefore you cannot contest in the Election.')
elif age == "" or candidate_dob == "" or political_party == "":
    print('You need to be above 70 years to compete or belong to Apc')
    

