i = [[4, 8], 
[15, 16]]

j = [[23, 42], 
[69, 100]]

result = [[0, 0],
[0, 0]]

#iterate through rows
for x in range(len(i)):
    #iterate through columns
    for y in range(len(j)):
        result[x][y] = i[x][y] + j[x][y]

print(result)

#solved