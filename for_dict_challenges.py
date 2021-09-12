# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???
num_of_replays = {}
for i in range(len(students)):
    if students[i]['first_name'] not in num_of_replays:
        num_of_replays[students[i]['first_name']] = 1
    else:
        num_of_replays[students[i]['first_name']] += 1
for key,value in num_of_replays.items():
    print(key,':',value)  

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
num_of_replays = {}
for i in range(len(students)):
    if students[i]['first_name'] not in num_of_replays:
        num_of_replays[students[i]['first_name']] = 1
    else:
        num_of_replays[students[i]['first_name']] += 1

ans = max(num_of_replays, key=num_of_replays.get)
print(f'Самое частое имя среди учеников: {ans}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???
num_of_replays = {}
for i in range(len(school_students)):
    for student in school_students[i]:
        if student['first_name'] not in num_of_replays:
            num_of_replays[student['first_name']] = 1
        else:
            num_of_replays[student['first_name']] += 1
    print(f'Самое частое имя в классе {i+1}: {max(num_of_replays, key=num_of_replays.get)}')
    num_of_replays ={}


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???
for cl in school:
    male = 0
    female = 0
    for student in cl['students']:
        if is_male[student['first_name']] == True:
            male += 1
        elif is_male[student['first_name']] == False:
            female += 1 
    print(f"Класс {cl['class']}: девочки {female}, мальчики {male}")



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
new_school = []
for cl in school:
    male = 0
    female = 0
    for student in cl['students']:
        if is_male[student['first_name']] == True:
            male += 1
        elif is_male[student['first_name']] == False:
            female += 1 
    new_class = {}
    new_class['class'] = cl['class']
    new_class['male'] = male
    new_class['female'] = female
    new_school.append(new_class)
    
male_max_class =''
female_max_class =''
male = 0
female = 0
for cl in new_school:
    if cl['male'] >= male:
        male = cl['male']
        male_max_class = cl['class']
    if cl['female'] >= female:
        female = cl['female']
        female_max_class = cl['class']
print(f'Больше всего мальчиков в классе {male_max_class}')
print(f'Больше всего девочек в классе {female_max_class}')
