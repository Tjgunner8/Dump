import turtle


def formatFile(): 
    FileData = []
    with open("sports_data.csv","r") as f:
        for line in f:
            templist = line.strip("\n").split(",")
            FileData.append(templist)
    return FileData

FileData = formatFile()

def parseData(FileData):
    for i in range(1,len(FileData)):
        if FileData[i][0] == "FALSE":
            FileData[i][0] = False
        else:
            FileData[i][0] = True
        FileData[i][1] = int(FileData[i][1])
        FileData[i][2] = int(FileData[i][2])
        FileData[i][3] = int(FileData[i][3])
        FileData[i][4] = float(FileData[i][4])
        FileData[i][5] = float(FileData[i][5])
    return FileData

FileData = parseData(FileData)

def getfemaleHeight(FileData,height): 
    for i in range(1,len(FileData)):
        if FileData[i][0] == False:
            height.append(FileData[i][2])

def getmaleHeight(FileData,height): 
        for i in range(1,len(FileData)):
            if FileData[i][0] == True:
                height.append(FileData[i][2])



height = []

maleH = getmaleHeight(FileData,height)
femaleH = getfemaleHeight(FileData,height)


def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return



def meanHeight(data): 
    total = 0
    for i in range(len(data)):
        total += data[i]
    mean = round(total/len(data),2)
    return mean
def bar_graph(var1, value):
    var1.begin_fill()
    var1.left(90)
    var1.forward(value)
    var1.write(" " + str(value))

    var1.right(90)
    var1.forward(1)
    var1.right(90)
    var1.forward(value)
    var1.left(90)
    var1.end_fill()
    var1.forward(10)


a = turtle.Screen()
a.bgcolor("black")
var1 = turtle.Turtle()
var1.color("green", "white")

var1.pensize(3)
var1.speed(100000000000000000)
var1.penup()
var1.goto(-400,0)
var1.pendown()
var2 = turtle.Turtle()
var2.color("red", "white")
var2.pensize(3)
var2.speed(100000000000000000)
var2.penup()
var2.goto(-400,-200)
var2.pendown()
measureheight = femaleH
measure2 = maleH
for i in measureheight:
    bar_graph(var1, i)
for j in measure2:
    bar_graph(var2,j)

a.mainloop()


print(maleH,"\n",femaleH)