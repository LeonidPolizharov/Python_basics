from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Василий', 'Семен']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen = zip_longest(tutors, classes[:len(tutors)])

print(gen)
for i in gen:
    print(i)

# print(next(gen))  # для проверки на "исчерпаемость"
