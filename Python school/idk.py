
def readFile():
    fileData = []
    fo = open("sports_data.csv","r")
    for line in fo:
        line = line.strip("\n")
        templist = line.split(",") 
        fileData.append(templist)
    fo.close()
    return fileData
FileData = readFile()

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

def getFemaleHeight(fileData, femaleHeight):
    for i in range(1,len(fileData)):
        if fileData[i][0] == False:
            femaleHeight.append(fileData[i][2])
    return femaleHeight 

def dataSort(femaleHeight):
    femaleHeight = femaleHeight.sort()
    return femaleHeight
    
    


femaleHeight = []

fileData = readFile()
print (fileData)  
fileData = parseData(fileData)
print (fileData)

femaleHeight = getFemaleHeight(fileData, femaleHeight)
print('Female Heights',femaleHeight)

