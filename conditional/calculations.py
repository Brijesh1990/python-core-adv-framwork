#w.a.p to print airthmatic calculations
#enter a choice e.g 1 press addtions 2 press substraction 3 press multiplication 4 press division

choice=int(input("Enter a choice :"))
a=int(input("Enter a values :"))
b=int(input("Enter b values :"))
    
if choice==1:
    c=a+b
    print("Addition of {0} and {1} is {2}".format(a,b,c))

elif choice==2:
    c=a-b
    print("Substarctions of  {0} and {1} is {2}".format(a,b,c))    

elif choice==3:
    c=a*b
    print("Multiplications of a {0} and b {1} is c {2}".format(a,b,c))
    
elif choice==4:
    c=a/b
    print("Division of a {0} and b {1} is c {2}".format(a,b,c))
    
else:
    exit()
        

       
         
 
 
 
    
    
