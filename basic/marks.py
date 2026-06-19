class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
        self.marks=[]
    def add_marks(self,subject,score):
        dic={"subject":subject,"score":score}
        self.marks.append(dic)
    def get_average(self):
        total=0
        for item in self.marks:
            total=total+item['score']
        self.avg=total/len(self.marks)
        return self.avg
    
    def get_grade(self):
        if(self.avg >=91):
            self.grade="a"
        elif(self.avg >=81):
            self.grade="b" 
        elif(self.avg >=71):
            self.grade="c"
        elif(self.avg >=61):
            self.grade="d"
        elif(self.avg >=51):
            self.grade="e"
        else:
            self.avg <=40
        return self.grade 
    def __str__(self):
        return f"{self.name}{self.marks} \n avg:{self.get_average} \ngrade{self.get_grade}"
s=Student("nikhil","597")
s.add_marks("maths",98)
s.add_marks("telugu",59)
s.add_marks("physics",90)
print(s.get_average())
print(s.get_grade())
print(s)