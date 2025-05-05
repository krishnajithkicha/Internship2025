def fibonacci_sequence(n):
    if n<=0:
        return 0
    elif n==1:
        return 0
    elif n>=2:
        a=0
        b=1
        print(a,b,end=" ")
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=" ")
n=int(input("Enter the number of terms in the Fibonacci sequence: "))
print("Fibonacci sequence:")
fibonacci_sequence(n)