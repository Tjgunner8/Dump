
def sum_mult(num,n):
    total = 0
    i = 0
    cat = num//n
    if num%n != 0:
        while i <= cat: 
            total = total + i*n
            i += 1
        return total 
    else:
        for i in range(1,cat):
            total += i*n
            print(total)
            return  total
print(sum_mult(15,5))