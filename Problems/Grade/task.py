student_score = abs(int(input()))
max_score = abs(int(input()))
grade = student_score / max_score
if grade < 0.6:
    print('F')
elif 0.6 <= grade < 0.7:
    print('D')
elif 0.7 <= grade < 0.8:
    print('C')
elif 0.8 <= grade < 0.9:
    print('B')
else:
    print('A')