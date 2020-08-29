from funfair import *
from utils import *

def main():
    print("Executing main program")
    inputs = readInputFile()
    print(inputs)
    variety = inputs[0]
    denominations = inputs[1]
    purchase = inputs[2]
    print("Printing Output of Recursive Approach with O(2^n), n purchase amount")
    print(countRecursive(denominations, variety, purchase))
    print("Printing Output of Tabulation 1 Approach with O(mn), m variety, n purchase amount")
    print(countTabulation1(denominations, variety, purchase))
    print("Printing Output of Memoization Approach with O(n), n purchase amount")
    print(countMemoization(denominations, variety, purchase))
    writeOutputFile(countMemoization(denominations, variety, purchase))
    print("Done!!!")

if __name__ == '__main__':
    main()