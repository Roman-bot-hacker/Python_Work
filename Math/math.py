import copy
def math_main(num, count):
    newArr=[]
    for i in num:
        print(str(i))
        if (is_math_2_enabled(i)):
            k=copy.deepcopy(i)
            k.append(count)
            newArr.append(k)
            newArr.append([i,[count]])
        else:
            print(str(i))
            i=math_2(i, count)
            for z in i:
                newArr.append(z)
    print(str(newArr))
    return newArr

def is_math_2_enabled(num):
    indicator=True
    if(len(num)>1):
        for i in num:
            if(isinstance(i,list)):
                indicator=False
    return indicator

def math_2(num, count):
    newArr=[]
    print(str(num))
    last=copy.deepcopy(num)
    last.append([count])
    newArr.append(last)
    print(str(last))
    for i in num:
        k=copy.deepcopy(i)
        newArr2=[]
        for z in num:
            if(k!=z):
                newArr2.append(z)
            else:
                k.append(count)
                newArr2.append(k)
        newArr.append(newArr2)
    print(str(newArr))
    return newArr

if __name__=="__main__":
    k=int(input())
    i=1
    result = []
    result.append([1])
    z=1
    while z<=k-1:
        result=math_main(result, z + 1)
        print(result)
        z+=1
    k=1
    for i in result:
        print(str(k)+" "+str(i))
        k+=1


