M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

print (M[1])
print (M[1][2])
print ([row[1] for row in M])
print ([M[row][1] for row in (0, 1, 2)])
print ([M[i][i] for i in range(len(M))])
print ('========')

print ([M[row][col] * N[row][col] for row in range(3) for col in range(3)])
print ([[M[row][col] * N[row][col] for col in range(3)] for row in range(3)])
print ('========')

res = []
for row in range(3):
    tmp = []
    for col in range(3):
        tmp.append(M[row][col] * N[row][col])
    res.append(tmp)

print (res)

