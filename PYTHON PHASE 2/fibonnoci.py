nterm = int(input("enter no of terms : "))
n1 , n2 = 0 ,1
if nterm<=0 :
   print("enter positive valve")
elif nterm==1 :
   print(n1)
else:
  print("fibonnaci series")
  print(n1,n2 ,end=" ")
  for i in range(3,nterm+1):
    nth=n1+n2 
    print(nth,end=" ")
    n1=n2
    n2=nth
    