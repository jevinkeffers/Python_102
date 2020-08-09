i = [[4, 8, 200], 
[15, 16, 300], 
[1, 2, 3]]

j = [[23, 42, 400], 
[69, 100, 500],
[1, 2, 3]]

result = [[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]

#iterate through rows
for x in range(len(i)):
    #iterate through columns
    for y in range(len(j)):
        result[x][y] = i[x][y] + j[x][y]
print(result)

#solved