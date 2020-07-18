#that years that contain 366 days that year is called leap year
#after 4 years leap years are repeted
#nested if condition within another condtion
year=int(input('Enter a Years :'))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print('This is a Leap year {}'.format(year))
        else:
            print('This is a Not Leap year {}'.format(year))
    
    else:
        print('This is a Leap year {}'.format(year))
        

else:
    print('This is a Not a Leap year {}'.format(year))                
                
            
            
    