student=[("palani",85,90,78),("rajesh",52,54,56),("nikhil",55,54,58)]
with open("marks.txt","w")as f:
    for i in student:
        f.write(f"{i[0]} {i[1]} {i[2]} {i[3]}\n")
print("completed")
with open("marks.txt","r")as f:
    for line in f:
        line=line.strip()
        word=line.split(" ")
        name=word[0]
        marks=[int(x) for x in word[1:]]
        avg=sum(marks)/len(marks)
        print(f"{name},AVg={avg}")