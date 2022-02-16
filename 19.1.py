def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

print (mysum([1, 2, 3, 4, 5, 6, 7]))


def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

print (mysum([1, 2, 3, 4, 5, 6, 7]))
print ('==========')

def mysum(L):
    if not L: return 0
    return nonempty(L)

def nonempty(L):
    return L[0] + mysum(L[1:])

print (mysum([1.1, 2.2, 3.3, 4.4]))
print ('==========')

L = [1, 2, 3, 4, 5, 6, 7]
sum = 0
while L:
    sum += L[0]
    L = L[1:]

print (sum)
print ('==========')

L = [1, 2, 3, 4, 5, 6, 7]
sum = 0
for x in L: sum += x

print (sum)
print ('==========')

def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]
print (sumtree(L))
print(sumtree([1, [2, [3, [4, [5]]]]]))
print(sumtree([[[[[1], 2], 3], 4], 5]))
