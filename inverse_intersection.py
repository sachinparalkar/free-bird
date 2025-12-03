data1 = [1,2,3,3,4,4,4,5]
data2 = [3,5,7]

def deleteMatch(data1, data2):
    data3= []

    dataSet1 = set(data1)
    dataSet2 = set(data2)

    print(dataSet1)
    print(dataSet2)

    if(len(dataSet1) <= len(dataSet2)):
        for i in dataSet1:
            if i not in dataSet2:
                data3.append(i)
            else:
                dataSet2.remove(i)
        data3.extend(list(dataSet2))
               
    else:
        for i in dataSet2:
            if i not in dataSet1:
                data3.append(i)
            else:
                dataSet1.remove(i)
        data3.extend(list(dataSet1))
    return data3

print(deleteMatch(data1, data2))

    


    
    
    