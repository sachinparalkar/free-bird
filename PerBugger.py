def persistence(n):
        
    if n>=0 and n<10:
        return n
    else:
        while n>=10:
            digits = digitList(n)    
            print(digits)
            n = getNumber(digits)
            print(n)
        return n
        
def digitList(n):
    numList = []

    while(n>0):
        currentDigit = n%10
        n = int(n/10)

        print(type(currentDigit))
        numList.append(currentDigit)
        
    return numList

def getNumber(numList):
    newNum = 1
    for digit in numList:
        newNum = newNum*digit
    
    return newNum

persistence(39)
#persistence(4)
#persistence(25)
#persistence(999)
