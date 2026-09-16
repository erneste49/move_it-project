
students = [("Alejandro", ["CompSci", "Physics"]),
("Justin", ["Math", "CompSci", "Stats"]),
("Ed", ["CompSci", "Accounting", "Economics"]),
("Margot", ["InfSys", "Accounting", "Economics", "CommLaw"]),
("Peter", ["Sociology", "Economics", "Law", "Stats", "Music"])]



list_compSci_students = []
for single_list in students:
    student_name= single_list[0]
    student_subject = single_list[1]
    if 'CompSci' in student_subject:
        list_compSci_students.append(student_name)
print('The list of students that take computer science are: ')
for com_student_name in list_compSci_students:
    print(com_student_name)
    
#end of solution to first question


#below is solution to second question
print('The total number of students taking computer science are:', len(list_compSci_students))




    
