#swap two number
# a=10
# b=20
# after swap 
# a=20
# b=10
 
a=int(input('Enter a value :'))
b=int(input('Enter b value :'))

temp=a
a=b
b=temp

print("after swap a is :{0} and b is {1}:".format(a,b))

