# Python code for a Weighted Grade Calculator

# input name
name  = input('Enter your name: ')

# input assignnment grades and weight of assignments
assingments = input('\nEnter assignment scores: ')
assignments = [float(assignment) for assignment in assingments.split()]
a_wgt = float(input('Enter the weight of your assignments: '))
# print(assignments)

# input quiz grades and weight of quizzes
quizzes = input('\nEnter your quiz scores: ')
quizzes = [float(quiz) for quiz in quizzes.split()]
q_wgt = float(input('Enter the weight of your quiz scores: '))
# print(quizzes)

# input test grades and weight of tests
tests = input('\nEnter your test scores: ')
tests = [float(test) for test in tests.split()]
t_wgt = float(input('Enter the weight of your test scores: '))
# print(tests)

# input finals grades and weight of finals
finals = float(input('\nEnter the score on your final: '))
f_wgt = float(input('Enter the weight of your final score: '))
# print(finals)

# Function calculates average
def avg(scores):
    total_sum = sum(scores)
    total_sum = float(total_sum)
    return total_sum / len(scores)

# Function calculate letter grade
def letter_grade(grade):
    if grade >= 90: return "A"
    elif grade >= 80: return "B"
    elif grade >= 70: return "C"
    elif grade >= 60: return "D"
    else : return "F"

# Averaging each grade category
a_grade = avg(assignments)
q_grade = avg(quizzes)
t_grade = avg(tests)

# Finding the total weighted grade
weighted_grade = ((a_wgt * a_grade) + (q_wgt * q_grade) +
                  (t_wgt * t_grade) + (f_wgt * finals))
average_grade = (round(weighted_grade, 2))
letter = letter_grade(average_grade)

# Outputting data
print(f"\n{name}: Your average grade is, {average_grade}, and your letter grade is, {letter}.")

