print("Calculator")
a = float(input("Enter the number a ="))
print(a)
b = float(input("Enter the number b ="))
print(b)

o = int(input("1.ADD,2.SUB,3.MUL,4.DIV, Enter the number for the operation : "))
print(o)

if o == 1 :
    add = a+b
    print("Addition of a and b = ",add)
    
elif o == 2 :
    sub = a-b
    print("Subtraction of a and b = ",sub)

elif o == 3 :
    mul = a*b
    print("Multiplication of a and b = ",mul)

elif o == 4 :
    div = a/b
    print("Division of a and b = ",div)
    
else:
    print("INVALID INPUT")
    
    
    