
while True: 
    biT = input("enter your bit number: ").strip()
    mask = input("enter your mask number: ").strip()
    if len(biT) == len(mask):
        break
    else:
        print("please enter numbers with the same number of bits")
masked = []        


def cypher(): 
    while True: 
        print("Please select what cypher you'd like: AND NOT OR XOR")
        cypherC = input( ).upper()
        if cypherC == "AND" or "NOT" or "OR" or "XOR":
            break
        else:
            print("please enter a valid cypher method")     
    return cypherC

def AND():
    for i in range(len(biT)): 
        if biT[i] == mask[i]: 
            masked = masked.append(biT[i])    
        else: 
            masked.append("0")
            


if cypher() == "AND":
    AND()
elif cypher() == "NOR":
    print("DOG")
elif cypher() == "OR":
    print("triangle")
elif cypher() == "XOR":
    print("square")


