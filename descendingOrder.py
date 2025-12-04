def descending_order(num):
    print(num)
    numStr = str(num)
    myList = list(numStr)
    
    myList.sort(reverse=True)
    print(myList)

    dataStr = ''.join(myList)
    print(dataStr)
    myNumber = int(dataStr)
    print(myNumber)
    return myNumber
    


    
    #myNumber = int(dataStr)

descending_order(15)
#descending_order(123456789)
