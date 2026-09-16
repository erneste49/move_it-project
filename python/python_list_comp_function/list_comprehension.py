# using former method 
##p = [2, 4, 5, 6, 8, 10]
##new = []
##for x in p:
##    new.append(x ** 2)
##print(p)
##print(new)

#using list comprehension method
##p = [2, 4, 5, 6, 8, 10]
##new = [x**2 for x in p]
##print(p)
##print(new)


##a= [20, 22, 40]
##b = [new // 2 for new in a]   
##print('Original list ', a)
##print('new list ', b)


# using if condition in list comprehension
##p = [2, 4, 5, 6, 8, 10]
##new = [x**2 for x in p if x%4==0]
##
##print(p)
##print(new)


# ** Using If statement **

##a= [20, 22, 40]
##b = [new // 2 for new in a if new!=22]   
##print('Original list ', a)
##print('new list ', b)



# adding 2 to even numbers and adding 3 to odd numbers
##numbers = [1,2,3,4,5,6,7,8,9,10]
##result = [num + 2 if num%2==0 else num + 3 for num in numbers]
##print(numbers)
##print(result)


##students = ['Sarah', 'Bem']
##feedback = ['Sarah is a female' if stud == 'Sarah' else 'Ben is a male'  for stud in students]
##print(feedback)



##budget = [12, 8, 11]
##new_budget = [amount + (amount* 5/100) for amount in budget]
##print('Original budget:', budget)
##print('Padded budget:', new_budget)


##web_visit = [1200, 1920, 566, 876, 504]
##assum1 = [ av//30 for av in web_visit]
##
##print('Assuming there are 30days in each month', assum1)
##
##assum2 = [ av2//30 if av2 != web_visit[1] else av2 // 28  for av2 in web_visit]
##print('Assuming there are 30days in each month except feb', assum2)



# using list comprehension to change list of tuple to just list
##cars = [('camry', 'corolla'), ('explorer', 'focus'), ('g-wagon', '4matic')]
##new_carlist = []
### using traditional for loop
##for car in cars:
##    for c in car:
##        new_carlist.append(c)
##print(new_carlist)
##print(cars)

#using list comprehension
##print([c for car in cars for c in car])



##products = [ ('purse', 'necklace'), ('Barbie', 'Bricks game', 'play dough'), ('Hair brush', 'Phones') ]
##
##new_list = [ i for item in products for i in item]
##print(new_list)


sc= 30
final_year = [23, 45, 59, 12]
new_final_year = [score + sc  for score in final_year]
print('Original score', final_year)
print("Boosted scores by 30 =", new_final_year)

list2 = [score + sc for score in final_year if score >= 20]
print('The scores above 20 that were boosted are: ', list2)




















