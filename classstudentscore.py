class students:
    def __init__(self,name,age,class_):
        self.name=name
        self.age=age
        self.class_=class_


    def average(self,biologyscore,chemestryscore,physicsscore):
        result=(biologyscore+chemestryscore+physicsscore)/3
        print(result)
Alex=students("Alex","21","1")
Daniel=students("Daniel","23","3")
biologyscore=int(input("please enter biology score"))
chemestryscore=int(input("please input chemesty score"))
physicsscore=int(input("please input physics score"))

Alex.average(biologyscore,chemestryscore,physicsscore)

print(Alex.name,Alex.age,Alex.class_)

        
