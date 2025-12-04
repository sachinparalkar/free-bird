
def array_diff(a, b):
    data = []  
    
    dataSet1 = set(a)
    dataSet2 = set(b)
    
    set3 = dataSet1.intersection(dataSet2)
    print(set3)
    if len(set3) > 0:   
        for i in set3:
            if i in a:
                a.sort()
                start = a.index(i)
                end = len(a)

                for j in range(start, end):
                    if i in a:
                        a.remove(i)

            if i in b:
                b.sort()
                start = b.index(i)
                end = len(b)

                for j in range(start, end):
                    if i in b:
                        b.remove(i)


        data = a + b
    else: 
        data = a+b

    print(data)    
    return data

array_diff([1,2,3], [1,2])

def basic_test_cases():
    array_diff([1,2], [1])
    array_diff([1,2,2], [1])
    array_diff([1,2,2], [2])
    array_diff([1,2,2], [])
    array_diff([], [1,2])
    array_diff([1,2,3], [1, 2])