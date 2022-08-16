replace=""
flag=True
print("******* welcome to the zodiac calculator *******")
num1=int(input("enter first number:"))
print(num1)
num2=int(input("enter second number:"))
print(num2)
print(" these are the operators you can use :")
print("1. Addition")
print("2. substraction")
print("3. multiplication")
print("4. division")
print("5. modulus")
result=0
operator=input("choose an option from these(1,2,3,4,5):")
if operator=="1":
    replace1="addition"
    result=num1+num2
if operator == "2":
    if num1<num2:
        flag=false
        print("do not subtract the first number less than second")
    else:
        flag=True
        replace1="subtraction"
        result=num1-num2
if operator == "3":
    if num2==0 or num1==0:
        flag="do not print"
        print("cannot multiply by zero")
    else:
         replace1="multiplication"
         result=num1*num2
    print("the result of multiplication of ",num1 ,"and",num2,"is",result)
if operator == "4":
    if num2==0 or num1==0:
        flag="do not print"
        print("cannot devide by zero")
    else:
         replace1="division"
         result=num1//num2
    print("the result of division of ",num1,"and",num2,"is",result)
if operator == "5":
    if num2==0
        flag="do not print"
        print("cannot  do modulus")
    replace1="modulus"
    result=num1%num2
    print("the result of modulus of",num1 "and",num2 "is",esult)
if flag==True:
    print("the result of", replace1,"of",num1,"and",num2,"is",result)

