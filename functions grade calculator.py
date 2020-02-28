name=(input('Please input student name'))
homework=int(input('Please input homework score'))
assessment=int(input('Please input assessment score'))
finalexam=int(input('Please input final exam score'))
result1=homework+assessment+finalexam
score=result1/3 
def ictgrade(score_example):
    if score_example>=70:
        return 'A*'
    elif score_example>=60:
        return 'A'
    elif score_example>=50:
        return 'B'
    elif score_example>=40:
        return 'C'
    else:
        return 'Fail'
    
test = ictgrade(score)
print(test)