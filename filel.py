with open("hi.txt","w") as f:
    f.write("palani\n")
    f.write("nikhl\n")
    f.write("rajesh\n")
    f.write("lokesh\n")
print("File created sucessfully")
with open("hi.txt","r") as f:
    content = f.read()
    print(content)