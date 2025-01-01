if __name__ == '__main__':
    n = int(input())
    student_data = []

    for _ in range(n):
        name = input()
        score = float(input())
        student_data.append([name, score])

    # Find the second lowest grade
    grades = set(student[1] for student in student_data)
    second_lowest_grade = sorted(grades)[1]

    # Find students with the second lowest grade
    students_with_second_lowest_grade = [student[0] for student in student_data if student[1] == second_lowest_grade]

    # Sort the names alphabetically
    students_with_second_lowest_grade.sort()

    # Print each name on a new line
    for name in students_with_second_lowest_grade:
        print(name)
