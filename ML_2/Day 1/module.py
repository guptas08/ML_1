def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

#write a function to find fibonacci series upto x
def fib(x):
    #logic
    first=1
    second=1
    series=[first,second]
    for i in range(x+1):
        if i==first+second:
            series.append(i)
            first=second
            second=i
    return series