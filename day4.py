print ("enter the value of a")
a = int(input())
print("enter the value of b")
b = int(input())
print ("enter the value of c")
c = int(input())
if a == b and a == c:
    print ("all the numbers are equal")
elif a > b and a > c:
    print ("a is the greatest")
elif b > a and b > c:
    print (" b is the gratest")
else:
    print ("c is the greatest")
    