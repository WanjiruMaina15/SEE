#ask user to input
score= int(input('Enter the studentsscore(0-100):'))
if score >=90:
    grade='A'
elif score >= 80:
    grade= 'B'
elif score >=70 :
    grade= 'C'
elif score >= 60:
    grade= 'D'
elif score >= 50:
    grade= 'E'
else:
    grade='F'
print(f'The students score is:{grade}')