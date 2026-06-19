num1=float(input("enetr the num1:"))
num2=float(input("enter the num2:"))
operation=input("enter the operatiion(+,-,*,/):")
if operation=='+':
    result=num1+num2
elif operation=='-':
    result=num1-num2
elif operation=='*':
    result=num1*num2
elif operation=='/':
    if num2 !=0:
        result=num1/num2
    else:
        result="invalid operation"
else:
    result=("invalid division")
print("result",result)
