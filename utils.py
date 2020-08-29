def readInputFile():
    variety = 0
    denominations =[]
    purchase = 0
    with open('inputPS5.txt') as file:
        for line in file:
            data = line.split(":")
            if data[0].strip() == "Variety":
                variety = int(data[1].strip())
            if data[0].strip() == "Denominations":
                temp = data[1].strip().split()
                denominations = list(map(int, temp))
            if data[0].strip() == "Purchase":
                purchase = int(data[1].strip())
    return (variety, denominations, purchase)

def writeOutputFile(count):
    with open('outputPS5.txt','w') as file:
        file.write("Possible Combinations: "+str(count))
