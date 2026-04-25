import json as js
students='{"name":"nikhal","cgpa":8.5,"branch":"CSE"}',
'{"name":"nikhal","cgpa":8.5,"branch":"CSE"}','{"name":"nikhal","cgpa":8.5,"branch":"CSE"}'
with open("students.json","w")as f:
    js.dumps(students,indent=4)
with open("students.json","r")as f:
    data=js.loads(f)
    print(type(students))
    for i in data:
        print(i)
    print("student with cgpa>=7.5")
    for i in data:
        if i["cgpa"]>=7.5:
            print(i)