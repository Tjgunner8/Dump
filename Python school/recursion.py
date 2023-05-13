def counter(ml,i):
    if i<len(ml):
        print(ml[i])
        i+=1
        counter(ml,i)
    return
ml = [7,8,9]
i=0
counter(ml,i)

def fact(n):
    if n==1:return 1
    return n*(fact(n-1))

print(fact(5))