print("check for isosceles_angle or not enter :<1>")
print("check for right_angle_triangle or not enter :<2>")
print("check for equilateral_triangle or not enter :<3>")
a=eval(input("enter number"))
match a:
    case 1:
        print("enter isosceles triangle lenth")
        b=eval(input())
        c=eval(input())
        d=eval(input())
        if(b==c and b!=d ):
            print("isosceles triangle")
        elif(c==d and c!=b ):
            print("isoceles triangle")
        elif(d==b and d!=c ):
            print("isosceles triangle")
        else:
            print("not isosceles triangle")
    case 2:
        print("enter right angle triangle lenth")
        b=eval(input("enter base:<>"))
        c=eval(input("enter height:<>"))
        e=eval(input("enter hypotenuse:<>"))
        d=(b*b+c*c)**(1/2)
        if(d==e):
            print("it is right angle triangle ")  
        else:
            print(" it is not right angle triangle")
    case 3:
        print("check equilateral triangle or not")
        b=eval(input())
        c=eval(input())
        d=eval(input())
        
        if(b==c==d):
            print("it is equilateral triangle")
        else:
            print("it is equilateral triangle")
    case _:
        print(" ")          
        
        