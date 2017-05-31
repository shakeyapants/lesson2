# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

lst = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]}, {'school_class': '4b', 'scores': [3, 3, 3, 2, 3]}]

school_total = 0
num_scores = 0

for dic in lst:
    scores = dic.get('scores')
    num_scores += len(scores)
    total = 0
    for score in scores:
        total += score
    school_total += total
    average = total / len(scores)
    print('In ' + dic.get('school_class') + ' average score is ' + str(average))

school_average = school_total/num_scores

print('The average score in school is ' + str(school_average))
