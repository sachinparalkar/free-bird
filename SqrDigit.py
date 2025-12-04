def square_digits(num):
    # Your code here
    resList= list()

    if(num==0):
        return 0
    else:
        while(num>0):
            digit = num%10
            print(digit)
            resList.append(str(digit*digit))
            num = int(num/10)
        
    resStr = ''.join(resList)
    print(resStr)
    #resNum = int(resStr)
    #return resNum

square_digits(0)