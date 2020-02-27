biology=float(input('please enter your biology score'))
chemestry=float(input('please input your chemestry score'))
physics=float(input('please input your physics score'))
if biology<=40:
    print('Fail')

elif chemestry<=40:
    print('Fail')

elif physics<=40:
    print('Fail')
else:
    result1=biology + chemestry + physics
    result2= result1/3
    if result2>=70:
        print('First')
    elif result2>=60:
        print('2.1')
    elif result2>=50:
        print('2.2')
    elif result2>=40:
        print('Pass')
    else:
        print('Fail')
        