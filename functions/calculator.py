def add(x,y):
    result = x+ y
    return result

def subtract(x,y):
    result = x- y
    return result

def divide(x,y):
    result = x/ y
    return result
def multiply(x,y):
    result = x* y
    return result
def remainder(x,y):
    result = x% y
    return result
def powerof(x,y):
    result = x** y
    return result

def getsum(*numberz):
    total=0
    for num in numberz:
        total+=num
    return total


def numbers():
    list=[]
    for number in range(2000,3201):
        if number %7==0 and number %5!=0:
            list.append(number)
    print(list)

numbers()