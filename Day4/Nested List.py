if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])
    
    # Extract all grades and find the second lowest
    grades = sorted(set([grade for name, grade in students]))
    second_lowest_grade = grades[1]
    
    # Find all students with the second lowest grade
    second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    
    # Print each name on a new line
    for student in second_lowest_students:
        print(student)