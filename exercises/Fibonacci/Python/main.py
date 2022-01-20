n = int(input("Enter an integer :"))
x0 = 0
x1 = 1

i=1
while i < n/2:
    x0=x0+x1
    x1=x0+x1
    i+=1

if n%2==1:
    print(f"The {n}th Fibonacci number is: {x0}")
else:
    print(f"The {n}th Fibonacci number is: {x1}")
