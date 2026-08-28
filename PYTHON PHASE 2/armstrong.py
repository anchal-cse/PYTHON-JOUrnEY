# A number is called an Armstrong number if it is equal to the sum of cubes of its digits. For example, 153 is an Armstrong number since 1^3 + 5^3 + 3^3 = 153.
x = int(input("Enter a number: "))
temp = x
total = 0
while temp != 0: #153
   digit = temp % 10 # 153%10 = 3
   total += digit ** 3 # 0 + 3^3 = 27
   temp //= 10 # 153//10 = 15

if total == x:
   print("armstrong")
else :   
   print("not a armstrong")