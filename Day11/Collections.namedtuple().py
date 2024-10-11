# Read the number of students
n = int(input())

# Read the column headers
columns = input().split()

# Find the index of the "MARKS" column
marks_index = columns.index("MARKS")

# Initialize a variable to store the total marks
total_marks = 0

# Read the marks for each student and accumulate the total marks
for _ in range(n):
    student_data = input().split()
    total_marks += int(student_data[marks_index])

# Calculate the average marks
average_marks = total_marks / n

# Print the average marks rounded to 2 decimal places
print(f"{average_marks:.2f}")
