groupmates = [
    {
        "name": "Иван",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Петр",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Андрей",
        "surname": "Сидоров",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 3, 3]
    }
]
def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)
