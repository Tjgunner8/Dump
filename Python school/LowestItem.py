boxes = ["cat","dog","small dog","big dog"]
sales = [55,65,40,45]

boxiD = 0
Lowest = 100

for i in range(0,len(sales)):
    if sales[i] < Lowest: 
        Lowest = sales[i]
        boxiD = boxes[i]

print(Lowest,boxiD)