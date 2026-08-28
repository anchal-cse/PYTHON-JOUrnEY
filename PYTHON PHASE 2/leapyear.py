year= int(input("enter the year "))
if (year%400==0 or year%4==0 and year%100!=0):
    print(F'{year} is a leap year')
else:
    print("not a leap year") #2024 divisible by 4 and 400 but not with 100